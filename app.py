from flask import request
from flask import render_template
from flask import Flask
from Lucy import get_response


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = get_response(user_input)
    return response


if __name__ == '__main__':
    app.run(debug=True)
