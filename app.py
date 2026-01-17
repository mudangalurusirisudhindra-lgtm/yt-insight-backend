from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # TEMP response (testing)
    return jsonify({
        "summary": "This is a demo summary. Backend is working.",
        "key_points": [
            "Point one",
            "Point two",
            "Point three"
        ],
        "keywords": ["AI", "YouTube", "NLP"]
    })

