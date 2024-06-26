from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

AZURE_PROXY_URL = "https://polite-ground-030dc3103.4.azurestaticapps.net"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')  # Extract user input from JSON
    response = requests.post(AZURE_PROXY_URL, json={"input": user_input})

    try:
        response_data = response.json()  # Attempt to parse JSON response from Azure Proxy
        response_text = response_data.get('response', 'No response from AI')
    except ValueError as e:
        response_text = f"Error parsing JSON response from Azure Proxy: {str(e)}"

    return jsonify({'response': response_text})  # Return JSON response to frontend




