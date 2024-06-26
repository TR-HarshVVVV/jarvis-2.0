# src/app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Your chat functionality here
    return 'Chat functionality placeholder'

if __name__ == '__main__':
    app.run(debug=True)


