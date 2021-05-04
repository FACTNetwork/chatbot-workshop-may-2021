from flask import Flask

from flask import render_template
from flask import request
from flask import session

import json
import string

# Load temporary participant data from JSON file.
with open("participants.json", "r") as f:
    participant_data = json.load(f)

# Initialize Flask.
app = Flask(__name__)

# Set a secret key for session management reasons.
# Flask internals...
app.secret_key = "factnetwork"

# Determine how to respond to a message from the user.
def interpret_message(message):
    # The name the bot will reply with.
    bot_name = "Bot"

    return "{}: I can't talk properly yet.".format(bot_name)
    
@app.route("/")
def home():
    # Send the front end web page.
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def process_message():
    return interpret_message(request.form["message"])
