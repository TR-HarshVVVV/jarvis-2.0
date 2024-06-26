from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

AZURE_PROXY_URL = "https://polite-ground-030dc3103.4.azurestaticapps.net"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = requests.post(AZURE_PROXY_URL, json={"input": user_input})
    response_text = response.json().get('response', 'No response from AI')

    return jsonify(response_text)

if __name__ == '__main__':
    app.run(debug=True)



