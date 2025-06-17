from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Simulate login validation
    if username == "admin" and password == "securepassword":
        app.logger.info(f"Successful login for user: {username}")
        return {"message": "Login successful"}, 200
    else:
        app.logger.warning(f"Failed login attempt for user: {username}")
        return {"message": "Login failed"}, 401

@app.route('/')
def home():
    return "Threat Detection Web App Running"
