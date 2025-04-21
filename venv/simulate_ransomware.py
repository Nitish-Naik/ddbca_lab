from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simulated decryption key
CORRECT_KEY = "unlock123"

HTML_TEMPLATE = '''
<!doctype html>
<title>Ransomware</title>
<h2 style="color:red; text-align:center;">💀 Your Files Have Been Encrypted! 💀</h2>
<p style="text-align:center;">Enter the decryption key below to recover them.</p>
<form method="POST" style="text-align:center;">
    <input type="text" name="key" placeholder="Enter decryption key" required>
    <button type="submit">Decrypt</button>
</form>
{% if message %}
    <p style="text-align:center; color:{{ color }};">{{ message }}</p>
{% endif %}
'''

@app.route("/", methods=["GET", "POST"])
def ransomware():
    message = None
    color = "red"
    if request.method == "POST":
        key = request.form.get("key")
        if key == CORRECT_KEY:
            message = "✅ Decryption successful! Your files are restored."
            color = "green"
        else:
            message = "❌ Incorrect key. Your files remain encrypted."
    return render_template_string(HTML_TEMPLATE, message=message, color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
