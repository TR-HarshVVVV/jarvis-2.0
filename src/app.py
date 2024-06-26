from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

AZURE_PROXY_URL = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/chat"

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.json.get('input')
        response = requests.post(AZURE_PROXY_URL, json={"input": user_input})
        response_text = response.json().get('response', 'No response from AI')
        return jsonify(response_text)
    else:
        return 'Method not allowed', 405

