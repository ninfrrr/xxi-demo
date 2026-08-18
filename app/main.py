import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "unknown")

MOVIES = [
    {"title": "The Odyssey", "showtime": "13:00", "studio": "Studio 1"},
    {"title": "Spider-Man: Brand New Day", "showtime": "15:00", "studio": "Studio 2"},
    {"title": "The Matrix Resurrections", "showtime": "17:00", "studio": "Studio 3"},
    {"title": "Dune", "showtime": "19:00", "studio": "Studio 4"},
]

@app.route("/")
def home():
    return "Cinema XXI - Movie Info Service"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/movies")
def movies():
    return jsonify(cinema="XXI", now_showing=MOVIES), 200

@app.route("/version")
def version():
    return jsonify(version=APP_VERSION), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

