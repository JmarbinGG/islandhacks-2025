import os
import pandas as pd
import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Allow React frontend to call Flask API

@app.route("/")
def home():
    return "Welcome to the Student Life AI Backend!"

@app.route("/api/ping")
def ping():
    return jsonify({"message": "Pong from Flask backend!"})

@app.route("/api/test")
def test():
    return jsonify({"message": "Flask backend working!"})

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    grades = data.get("grades")
    sleep = data.get("sleep")
    extra = data.get("extracurriculars")

    # Pretend AI logic
    suggestion = "Try to get 1 more hour of sleep and limit activities to 2 per week."
    return jsonify({"result": suggestion})

if __name__ == "__main__":
    app.run(port=5000, debug=True)