from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = ""
VALID_TOKEN = "56756756756"

def check_ip(ip):
    url = f"https://ipqualityscore.com/api/json/ip/{API_KEY}/{ip}"
    response = requests.get(url)
    return response.json()

def check_email(email):
    url = f"https://ipqualityscore.com/api/json/email/{API_KEY}/{email}"
    response = requests.get(url)
    return response.json()

@app.route("/ip/<string:ip>", methods=["GET"])
def verify_ip(ip):
    token = request.args.get("token")
    if token != VALID_TOKEN:
        return jsonify({"error": "Invalid token"}), 401

    result = check_ip(ip)
    return jsonify(result)

@app.route("/email/<string:email>", methods=["GET"])
def verify_email(email):
    token = request.args.get("token")
    if token != VALID_TOKEN:
        return jsonify({"error": "Invalid token"}), 401

    result = check_email(email)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
