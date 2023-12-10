from flask import Flask, render_template, request
from agent.agent import get_ai_response
from agent.text2voice import get_tts_elevenlabs

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("./templates/index.html")

@app.route("/send_message", methods = ["POST"])
def send_message():
    human_input = request.form["human_input"]
    message = get_ai_response(human_input)
    get_tts_elevenlabs(message)
    return message

if __name__ == "__main__":
    app.run(debug=True)