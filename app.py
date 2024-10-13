from flask import Flask, request, jsonify
from weather_service import fetch_weather
from ratelimit import limits
import requests

app = Flask(__name__)

# Rate limiting: 100 requests per hour
HOUR = 3600


@limits(calls=100, period=HOUR)
@app.route("/weather", methods=["GET"])
def get_weather():
    location = request.args.get("location")
    date1 = request.args.get("date1")
    date2 = request.args.get("date2")

    if not location:
        return jsonify({"error": "Location is required"}), 400

    try:
        weather_data = fetch_weather(location, date1, date2)
        return jsonify(weather_data)
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": str(e)}), 503
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
