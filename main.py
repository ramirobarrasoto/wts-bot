from flask import Flask, request, Response
from handlers.greeting_handler import handle_greeting
from handlers.state_handlers import handle_state

user_states = {}

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def webhook():
    data = request.form  

    user = data.get('From')        
    message = data.get('Body').strip() 

    if user not in user_states:
        user_states[user] = {
            "state": "greeting",
            "room_number": None,
            "category": None,
            "suboption": None,
            "comment": None
        }

    state = user_states[user]["state"]

    if state == "greeting":
        response_text, next_state = handle_greeting(message)
    else:
        response_text, next_state = handle_state(message, state, user_states[user])

    user_states[user]["state"] = next_state

    twilio_response = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{response_text}</Message>
</Response>"""

    return Response(twilio_response, mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)
