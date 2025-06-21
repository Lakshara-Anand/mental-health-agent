from flask import Flask, request, jsonify
from mood_utils import detect_mood
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    user_text = data.get("text", "")
    mood = detect_mood(user_text)
    return jsonify({"mood": mood})

if __name__ == '__main__':
    app.run(debug=True)