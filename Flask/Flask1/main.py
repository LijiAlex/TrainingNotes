from flask import Flask

app = Flask(__name__)  # creating the Flask class object


@app.route('/')  # refers to this function
def func1():
    return "Welcome to programming made easy"


@app.route('/home')  # refers to this function
def home():
    return "Let's learn flask"


@app.route('/home/<nam>')
def name(nam):
    return "hello,"+nam


if __name__ == '__main__':
    app.run(debug=True)