from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_API_URL = 'https://official-joke-api.appspot.com/'

@app.route('/random_joke', methods=['GET'])
def get_random_joke():
    response = requests.get(BASE_API_URL + 'random_joke')
    return jsonify(response.json())

@app.route('/jokes_by_category/<category>', methods=['GET'])
def get_jokes_by_category(category):
    response = requests.get(BASE_API_URL + f'jokes/{category}/ten')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)