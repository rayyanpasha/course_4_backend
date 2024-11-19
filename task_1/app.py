from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample constellation data
constellations = [
    {'id': 1, 'name': 'Orion', 'hemisphere': 'Northern', 'main_stars': ['Betelgeuse', 'Rigel', 'Bellatrix'], 'area': 594, 'origin': 'Greek'},
    {'id': 2, 'name': 'Scorpius', 'hemisphere': 'Southern', 'main_stars': ['Antares', 'Shaula', 'Sargas'], 'area': 497, 'origin': 'Greek'}
]

# Helper function to return error messages with HTTP cat image URLs
def error_response(message, status_code):
    return jsonify({
        "error": message,
        "cat_image": f"https://http.cat/{status_code}"
    }), status_code

# 1. View all constellations
@app.route('/constellations', methods=['GET'])
def get_all_constellations():
    return jsonify(constellations), 200

# 2. View a specific constellation by name
@app.route('/constellations/<name>', methods=['GET'])
def get_constellation(name):
    for constellation in constellations:
        if constellation['name'].lower() == name.lower():
            return jsonify(constellation), 200
    return error_response("Constellation not found", 404)

# 3. Add a new constellation
@app.route('/constellations', methods=['POST'])
def add_constellation():
    new_constellation = request.get_json()
    if not new_constellation or 'name' not in new_constellation:
        return error_response("Invalid data", 400)

    for constellation in constellations:
        if constellation['name'].lower() == new_constellation['name'].lower():
            return error_response("Constellation already exists", 409)

    constellations.append(new_constellation)
    return jsonify({"message": "Constellation added successfully"}), 201

# 4. Delete a constellation
@app.route('/constellations/<name>', methods=['DELETE'])
def delete_constellation(name):
    for constellation in constellations:
        if constellation['name'].lower() == name.lower():
            constellations.remove(constellation)
            return jsonify({"message": "Constellation deleted"}), 200
    return error_response("Constellation not found", 404)

# 5. Filter constellations by hemisphere and area
@app.route('/constellations/filter', methods=['GET'])
def filter_constellations():
    hemisphere = request.args.get('hemisphere')
    area = request.args.get('area', type=int)
    filtered = [c for c in constellations if (not hemisphere or c['hemisphere'].lower() == hemisphere.lower()) and (not area or c['area'] > area)]
    
    return jsonify(filtered), 200

# 6. View the main stars of a constellation specified by name
@app.route('/constellations/<name>/stars', methods=['GET'])
def get_main_stars(name):
    for constellation in constellations:
        if constellation['name'].lower() == name.lower():
            return jsonify({"main_stars": constellation['main_stars']}), 200
    return error_response("Constellation not found", 404)

# 7. Partially update a constellation specified by name
@app.route('/constellations/<name>', methods=['PATCH'])
def update_constellation(name):
    updates = request.get_json()
    for constellation in constellations:
        if constellation['name'].lower() == name.lower():
            for key, value in updates.items():
                if key in constellation:
                    constellation[key] = value
            return jsonify(constellation), 200
    return error_response("Constellation not found", 404)

# 8. View an image for a constellation (hardcoded placeholder image link)
@app.route('/constellations/<name>/image', methods=['GET'])
def get_constellation_image(name):
    # Hardcoded placeholder image URL for each constellation
    image_url = f"https://imageplaceholder.com/constellation/{name.lower()}"
    return jsonify({"image_url": image_url}), 200

# 9. Get constellations within a specific area range
@app.route('/constellations/area', methods=['GET'])
def get_constellations_by_area():
    min_area = request.args.get('min_area', type=int)
    max_area = request.args.get('max_area', type=int)
    
    if not min_area or not max_area:
        return error_response("Both min_area and max_area are required", 400)
    
    filtered = [c for c in constellations if min_area <= c['area'] <= max_area]
    
    if not filtered:
        return error_response("No constellations found in the specified area range", 404)
    
    return jsonify(filtered), 200


if __name__ == '__main__':
    app.run(debug=True)
