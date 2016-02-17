from flask import Flask, render_template, request, session
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    if not request.form['username'] or not request.form['password']:
        errors = 'Invalid username or password'

        return render_template('login.html', errors=errors)

    session['username'] = request.form['username']
    session['password'] = request.form['password']
    session['logged?'] = True

    return render_template('home.html')

app.secret_key = 'jff6sdrg76gduoiwenjr'

if __name__ == '__main__':
    app.run(debug=True)