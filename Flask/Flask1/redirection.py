from flask import *

app = Flask(__name__)


@app.route('/computer')
def computer():
    return 'welcome to computer science department'


@app.route('/electronics')
def electronics():
    return 'welcome to electronics department'


@app.route('/mechanical')
def mechanical():
    return 'welcome to mechanical department'


@app.route('/user/<dept>')
def user(dept):
    if dept == 'cs':
        return redirect(url_for('computer'))
    if dept == 'ec':
        return redirect(url_for('electronics'))
    if dept == 'mech':
        return redirect(url_for('mechanical'))

@app.route('/')  # refers to this function
def func1():
    return "select department in url user/<dept>"


if __name__ == '__main__':
    app.run(debug=True)