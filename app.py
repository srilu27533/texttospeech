from flask import Flask, render_template, request
import os
import pyttsx3


def text_to_speech(text, gender):
    
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()
    
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
