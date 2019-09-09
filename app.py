from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "lucy"
Bootstrap(app)

@app.route('/')
def search():
    return render_template('index.html')

@app.route('/about')
def start_dashboard():
    return render_template('about.html')

@app.route('/works')
def start_dashboard_2():
    return render_template('works.html')


if __name__ == '__main__':
    app.run()