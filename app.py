from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can talk to the API

@app.route('/check', methods=['POST'])
def check_number():
    data = request.get_json()
    number = data.get('number', None)

    if number is None or not isinstance(number, int):
        return jsonify({'error': 'Invalid input. Please send an integer.'}), 400

    result = 'even' if number % 2 == 0 else 'odd'
    return jsonify({'number': number, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
