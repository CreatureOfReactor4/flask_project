from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_METEO_URL = "https://api.meteo.lt/v1"

@app.route("/places", methods=["GET"])
def get_places():
    try:
        response = requests.get(f"{BASE_METEO_URL}/places")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": "Nepavyko gauti miestų sąrašo", "details": str(e)}), 500

@app.route("/forecast/<string:city>", methods=["GET"])
def get_forecast(city):
    try:
        response = requests.get(f"{BASE_METEO_URL}/places/{city}/forecasts/long-term")
        if response.status_code == 404:
            return jsonify({"error": "Miestas nerastas"}), 404
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": "Nepavyko gauti orų prognozės", "details": str(e)}), 500

@app.route("/")
def index():
    return jsonify({
        "message": "Sveiki! Naudokite /places norėdami gauti miestų sąrašą, arba /forecast/<miestas> orams."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
