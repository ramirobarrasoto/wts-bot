def handle_greeting(message):
    response = "Hi! Please tell me the room number you're reporting for housekeeping."
    next_state = "waiting_for_room"
    return response, next_state
