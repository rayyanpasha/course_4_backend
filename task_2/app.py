from flask import Flask, jsonify, request

app = Flask(__name__)

valid_token = "rayyan"

users = [{"username": "rayyan", "password": "123"}]

@app.route('/', methods=['GET'])
def index():
    return jsonify("welcome everyone"), 200

@app.route('/basic-auth', methods=['POST'])
def auth():
    auth = request.authorization
    print(auth)

    for user in users:
        if user["username"] == auth.username and user["password"] == auth.password:
            return jsonify({"message": "Access granted!"}), 200
    return jsonify({"message": "Access denied!"}), 403


@app.route('/bearer-auth', methods=['GET'])
def bearer_auth():
    # Get the Authorization header
    auth_header = request.headers.get('Authorization')
    
    # Validate the format of the header
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"message": "Missing or invalid token"}), 401

    # Extract the token from the header
    token = auth_header.split(' ')[1]  # Split the string and get the second part (the token)

    # Validate the token (replace with your validation logic)
    if token == "secureBearerToken123":
        return jsonify({"message": "Access granted!"}), 200

    return jsonify({"message": "Invalid token"}), 403

if __name__ == '__main__':
    app.run(debug=True)
