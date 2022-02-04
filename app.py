from flask import Flask, render_template, request
from main.py import text_to_speech
import os
    
app = Flask(__name__)
@app.route("/")
def FUN_root():
    return render_template("frontend.html")


@app.route('/regact', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        text_to_speech(text, gender)
        return render_template('frontend.html')
    else:
        return render_template('frontend.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
