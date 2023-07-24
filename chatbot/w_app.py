from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
app.secret_key = 'secret_key'  # Replace with your secret key

# Create the LoginManager instance
login_manager = LoginManager()
login_manager.init_app(app)

# Define a User class for authentication
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Simulated user data
users = {'admin': 'password'}  # Replace with your user data

# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and users[username] == password:
            print("Correct username and password")
            user = User(username)
            login_user(user)
            return redirect(url_for('protected'))
        else:
            print('Invalid username or password')
            error_message = 'Invalid username or password'
            return render_template('login.html', error_message=error_message)
    
    print('Rendering login page')
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Protected route - requires authentication
@app.route('/protected')
@login_required
def protected():
    return render_template('index.html')

# Set up the user_loader callback function
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Set the login view
login_manager.login_view = 'login'

if __name__ == '__main__':
    app.run(debug=True)
