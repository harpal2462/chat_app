from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin

app = Flask(__name__)
app.config.from_object('config.Config') 

db = SQLAlchemy()  
bcrypt = Bcrypt(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize db with the app
db.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    # def is_active(self):
    #     # You can customize this method based on your use case (e.g., check if the user is banned or suspended)
    #     return True  # By default, return True for active users

    # def get_id(self):
    #     return str(self.id)  # Return the user ID as a string

    def __repr__(self):
        return f'<User {self.username}>'


# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def index():
    return render_template('index.html', username=current_user.username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return 'Login Failed, Check username or password.'

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# Real-time Chat with Socket.IO
@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)  # Broadcast the message to all connected users


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    socketio.run(app, debug=True)
