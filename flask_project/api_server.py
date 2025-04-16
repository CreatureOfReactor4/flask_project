from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Jonas", "email": "jonas@example.com"},
    {"id": 2, "name": "Laura", "email": "laura@example.com"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    return jsonify(user) if user else jsonify({"error": "Vartotojas nerastas"}), 404

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    if "name" not in data or "email" not in data:
        return jsonify({"error": "Trūksta duomenų"}), 400

    new_user = {"id": len(users) + 1, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)