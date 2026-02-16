from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/python")
def hello_world():
    return jsonify({"message": "Hello, World!"})


@app.route("/api/test", methods=["GET", "POST"])
def test_endpoint():
    if request.method == "POST":
        data = request.get_json() or {}
        return jsonify(
            {
                "status": "success",
                "method": "POST",
                "received_data": data,
                "message": "Flask is working!",
            }
        )
    return jsonify(
        {"status": "success", "method": "GET", "message": "Flask API is working!"}
    )


@app.route("/api/calculate-points", methods=["POST"])
def calculate_points():
    data = request.get_json() or {}
    points = data.get("points", [])

    total = sum(points)
    average = total / len(points) if points else 0

    return jsonify({"total": total, "average": round(average, 2), "count": len(points)})


@app.route("/api/health")
def health_check():
    return jsonify({"status": "healthy", "service": "flask-api"})
