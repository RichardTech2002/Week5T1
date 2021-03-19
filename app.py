from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def Write():
    return render_template('FlaskTemplate1.HTML')


