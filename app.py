from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

app.secret_key = 'jff6sdrg76gduoiwenjr'

if __name__ == '__main__':
    app.run(debug=True)