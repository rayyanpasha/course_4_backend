from flask import Flask, request, jsonify

app = Flask(__name__)

# Buggy data storage
users = {}  # Missing initial data
posts = []  # Using list instead of a dictionary for unique IDs

# Route 1: Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return users  # Bug 1: Not using jsonify for response

# Route 2: Get a user by ID
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    # Bug 2: Missing ID validation
    return {"name": users[user_id]}  # Bug 3: KeyError if user_id doesn't exist

# Route 3: Create a new user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    # Bug 4: No validation for input data
    users[len(users) + 1] = data['name']  # Bug 5: ID generation is not string and may cause inconsistency
    return {"message": "User created successfully!"}  # Bug 6: Response not using jsonify

# Route 4: Get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return posts  # Bug 7: Response not using jsonify

# Route 5: Get a post by ID
@app.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
    post_id = int(post_id)  # Bug 8: TypeError if post_id is not a number
    for post in posts:
        if post['id'] == post_id:
            return post  # Bug 9: Response not wrapped in jsonify
    return {"message": "Post not found!"}  # Bug 10: Missing proper HTTP status code

# Route 6: Create a new post
@app.route('/post', methods=['POST'])
def create_post():
    data = request.json
    # Bug 11: Missing validation for 'content' key
    posts.append({"id": len(posts) + 1, "content": data["content"]})
    return {"message": "Post created!"}  # Bug 12: Response not using jsonify

# Route 7: Delete a post by ID
@app.route('/post/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    post_id = int(post_id)  # Bug 13: TypeError if post_id is not a number
    for post in posts:
        if post['id'] == post_id:
            posts.remove(post)
            return {"message": "Post deleted"}  # Bug 14: Response not using jsonify
    return {"message": "Post not found!"}  # Bug 15: Missing proper HTTP status code

# Route 8: Update a user
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    # Bug 16: Missing validation if user_id exists
    users[user_id] = data['name']  # Bug 17: Potential KeyError without validation
    return {"message": "User updated!"}  # Bug 18: Response not using jsonify

# Route 9: Delete all users
@app.route('/users', methods=['DELETE'])
def delete_users():
    users.clear()  # Bug 19: Dangerous operation with no confirmation
    return {"message": "All users deleted"}  # Bug 20: Response not using jsonify

if __name__ == '__main__':
    app.run(debug=True)
