import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allows any website to talk to your server

@app.route('/')
def home():
    return "Mirror Server is Online!", 200

@app.route('/generate-try-on', methods=['POST'])
def handle_request():
    # This is a 'Mock' response for your first test
    # It proves the button on the shop talked to your server!
    return jsonify({
        "status": "success",
        "message": "The Mirror has received your photo!"
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
