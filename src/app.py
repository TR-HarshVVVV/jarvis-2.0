from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world! This is Jarvis 2.0.'

if __name__ == '__main__':
    app.run(debug=True)
