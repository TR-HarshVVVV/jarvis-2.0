from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_name = request.json.get('name')  # Extract user name from JSON
    prompt = f"My name is {user_name} and I am participating in the Microsoft Developer AI Learning Hackathon."
    response_text = (
        f"That's great, {user_name}! The Azure Cosmos DB Developer Learning Hackathon sounds like an exciting "
        "opportunity. If you have any questions or need assistance related to Cosmic Works products, customers, "
        "or sales orders, feel free to ask. Good luck with the hackathon!"
    )
    
    return jsonify({'response': response_text})  # Return JSON response to frontend

if __name__ == '__main__':
    app.run(debug=True)


