from flask import Flask, redirect, request, url_for, jsonify, session
import requests

app = Flask(__name__)
# GitHub OAuth configuration
CLIENT_ID = "Ov23lieI6YKVhd2Tfxxb"
CLIENT_SECRET = "3988b414382e873e80ae3e2c08f50dc3b3321e3a"
AUTHORIZATION_BASE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
API_BASE_URL = "https://api.github.com/user"

valid_token = "rayyan"

users = [{"username": "rayyan", "password": "123"}]

@app.route('/', methods=['GET'])
def index():
    return '''
        <h1>home hai bhai </h1>
        <a href="/oauth">Login with Github</a>
'''

@app.route('/oauth')
def oauth():
    authorization_url = f"{AUTHORIZATION_BASE_URL}?client_id={CLIENT_ID}&scope=user"
    return redirect(authorization_url)

# Login route to initiate the OAuth flow
@app.route('/login')
def login():
    return redirect(url_for('oauth'))

# Callback route to handle GitHub's response
@app.route('/callback')
def callback():
    # Get the authorization code from the request
    code = request.args.get('code')
    if not code:
        return "Authorization failed.", 400

    # Exchange the authorization code for an access token
    token_response = requests.post(
        TOKEN_URL,
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
        }
    )

    token_json = token_response.json()
    access_token = token_json.get("access_token")
    if not access_token:
        return "Failed to obtain access token.", 400

    # Use the access token to fetch the user's information
    user_response = requests.get(
        API_BASE_URL,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }
    )

    user_data = user_response.json()
    return f"Logged in as: {user_data.get('login')}"
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
