from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OPENAI_API_KEY = "sk-proj-21LQkEcfwv7rDnC8KqRgT3BlbkFJTJWlXFf1diXVgs8Fpllk"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')  # Extract user input from JSON
    
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": f'My name is {user_input} and I am participating in the Microsoft Developer AI Learning Hackathon.',
        "max_tokens": 100
    }
    
    try:
        response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes

        try:
            response_data = response.json()  # Attempt to parse JSON response from OpenAI
            response_text = response_data['choices'][0]['text'].strip()
        except ValueError as e:
            response_text = f"Error parsing JSON response from OpenAI: {str(e)}"
    except requests.exceptions.RequestException as e:
        response_text = f"Request to OpenAI failed: {str(e)}"

    return jsonify({'response': response_text})  # Return JSON response to frontend

if __name__ == '__main__':
    app.run(debug=True)


