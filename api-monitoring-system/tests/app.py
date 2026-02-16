from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/metrics/history")
def metrics_history():
    hours = request.args.get("hours")
    if not hours or not hours.isdigit():
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"message": f"Showing data for {hours} hours"}), 200

@app.route("/api/test/alert", methods=["POST"])
def test_alert():
    data = request.get_json()
    if not data or "<script>" in data.get("api_name", ""):
        return jsonify({"error": "XSS detected"}), 400
    return jsonify({"message": "Alert received"}), 200

if __name__ == "__main__":
    app.run(debug=True)
