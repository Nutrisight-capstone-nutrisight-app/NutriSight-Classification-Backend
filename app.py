from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"message" : "NutriSight API v0.1.0 : Request Success"}), 200

@app.route('/predict', methods=['POST'])
def post_predict():
    
    return jsonify({"message" : "Success"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 