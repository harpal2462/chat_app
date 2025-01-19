# Flask Chat App

A simple real-time chat application built with **Flask**, **Flask-SQLAlchemy**, and **Socket.IO**. This app supports basic features such as user registration, login, and real-time messaging between users. It is designed to be easy to extend, allowing for additional features like chat rooms, group messaging, etc.

---

## Features

- **User Authentication**: Users can sign up and log in using their username and email.
- **Real-Time Chat**: Real-time messaging between users using **Socket.IO**.
- **SQLite Database**: Stores user data and messages locally using **SQLAlchemy** with SQLite.
- **Basic User Interface**: Simple, clean chat interface with real-time updates.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/harpal2462/chat_app.git 
   cd chat-app
   ```
2. **Create a virtual environment (recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**:
   ```bash
   python app.py
   ```
---

## Usage
- **Sign Up**: Users can create a new account with a unique username and email.
- **Login**: Users can log in with their existing username and email.
- **Chat**: Once logged in, users can start chatting with others in real time.

