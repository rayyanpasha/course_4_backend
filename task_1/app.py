from flask import Flask, request, jsonify , redirect

app = Flask(__name__)

# Sample constellation data
constellations = [
    {'id': 1, 'name': 'Orion', 'hemisphere': 'Northern', 'main_stars': ['Betelgeuse', 'Rigel', 'Bellatrix'], 'area': 594, 'origin': 'Greek'},
    {'id': 2, 'name': 'Scorpius', 'hemisphere': 'Southern', 'main_stars': ['Antares', 'Shaula', 'Sargas'], 'area': 497, 'origin': 'Greek'},
    {'id': 3, 'name': 'Ursa Major', 'hemisphere': 'Northern', 'main_stars': ['Dubhe', 'Merak', 'Phecda'], 'area': 1280, 'origin': 'Greek'},
    {'id': 4, 'name': 'Cassiopeia', 'hemisphere': 'Northern', 'main_stars': ['Schedar', 'Caph', 'Ruchbah'], 'area': 598, 'origin': 'Greek'},
    {'id': 5, 'name': 'Crux', 'hemisphere': 'Southern', 'main_stars': ['Acrux', 'Mimosa', 'Gacrux'], 'area': 68, 'origin': 'Latin'},
    {'id': 6, 'name': 'Lyra', 'hemisphere': 'Northern', 'main_stars': ['Vega', 'Sheliak', 'Sulafat'], 'area': 286, 'origin': 'Greek'},
    {'id': 7, 'name': 'Aquarius', 'hemisphere': 'Southern', 'main_stars': ['Sadalsuud', 'Sadalmelik', 'Sadachbia'], 'area': 980, 'origin': 'Babylonian'},
    {'id': 8, 'name': 'Andromeda', 'hemisphere': 'Northern', 'main_stars': ['Alpheratz', 'Mirach', 'Almach'], 'area': 722, 'origin': 'Greek'},
    {'id': 9, 'name': 'Pegasus', 'hemisphere': 'Northern', 'main_stars': ['Markab', 'Scheat', 'Algenib'], 'area': 1121, 'origin': 'Greek'},
    {'id': 10, 'name': 'Sagittarius', 'hemisphere': 'Southern', 'main_stars': ['Kaus Australis', 'Nunki', 'Ascella'], 'area': 867, 'origin': 'Greek'}
]

# Helper function to return error messages with HTTP cat image URL

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
    return redirect(f"https://http.cat/404"), 404

# 3. Add a new constellation
@app.route('/constellations', methods=['POST'])
def add_constellation():
    new_constellation = request.get_json()
    if not new_constellation or 'name' not in new_constellation:
        return redirect(f"https://http.cat/404"), 404
    for constellation in constellations:
        if constellation['name'].lower() == new_constellation['name'].lower():
           return redirect(f"https://http.cat/404"), 404

    constellations.append(new_constellation)
    return jsonify({"message": "Constellation added successfully"}), 201

# 4. Delete a constellation
@app.route('/constellations/<name>', methods=['DELETE'])
def delete_constellation(name):
    for constellation in constellations:
        if constellation['name'].lower() == name.lower():
            constellations.remove(constellation)
            return jsonify({"message": "Constellation deleted"}), 200
    return redirect(f"https://http.cat/404"), 404

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
    return redirect(f"https://http.cat/404"), 404

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
    return redirect(f"https://http.cat/404"), 404

# # 8. View an image for a constellation (hardcoded placeholder image link)
# @app.route('/constellations/<name>/image', methods=['GET'])
# def get_constellation_image(name):
#     # Hardcoded placeholder image URL for each constellation
#     image_url = f"https://imageplaceholder.com/constellation/{name.lower()}"
#     return jsonify({"image_url": image_url}), 200

# 9. Get constellations within a specific area range
@app.route('/constellations/area', methods=['GET'])
def get_constellations_by_area():
    min_area = request.args.get('min_area', type=int)
    max_area = request.args.get('max_area', type=int)

    if not min_area or not max_area:
        return redirect(f"https://http.cat/404"), 404
    
    filtered = [c for c in constellations if min_area <= c['area'] <= max_area]
    
    if not filtered:
        return redirect(f"https://http.cat/404"), 404
    
    return jsonify(filtered), 200


if __name__ == '__main__':
    app.run(debug=True)
