from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('Website.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("message")
    print("Received message:", text)  # Check if the message is received correctly
    response = get_response(text)  # Assuming get_response is defined elsewhere
    print("Generated response:", response)  # Check the generated response
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)