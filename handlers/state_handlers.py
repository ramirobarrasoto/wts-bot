from utils.sheet_service import append_to_sheet
from handlers.submenu_builders import (
    handle_submenu_technical,
    handle_submenu_replenishment,
    handle_submenu_cleaning,
    handle_submenu_amenities
)

def handle_state(message, state, user_data):
    dispatcher = {
        "waiting_for_room": handle_waiting_for_room,
        "waiting_for_category": handle_waiting_for_category,
        "waiting_for_subcategory": handle_waiting_for_subcategory,
       # "waiting_for_comment": handle_waiting_for_comment,
    }

    handler = dispatcher.get(state)

    if handler:
        return handler(message, user_data)
    else:
        return "Let's start again. Please tell me the room number.", "waiting_for_room"
    

def handle_waiting_for_room(message, user_data):
    user_data["room_number"] = message.strip()
    response = (
        f"✅ Room {user_data['room_number']} registered.\n"
        "What would you like to report?\n"
        "1. 🛠️ Technical issue\n"
        "2. 🧻 Replenishment request\n"
        "3. 🧽 Extra cleaning\n"
        "4. 🧴 Amenities delivery"
    )
    return response, "waiting_for_category"

def handle_waiting_for_category(message, user_data):
    option = message.strip()
    options_map = {
        "1": ("Technical issue", handle_submenu_technical),
        "2": ("Replenishment request", handle_submenu_replenishment),
        "3": ("Extra cleaning", handle_submenu_cleaning),
        "4": ("Amenities delivery", handle_submenu_amenities)
    }

    if option in options_map:
        category, submenu_func = options_map[option]
        user_data["category"] = category
        return submenu_func(), "waiting_for_subcategory"
    else:
        return "Invalid option. Please reply with 1, 2, 3 or 4.", "waiting_for_category"
    
def handle_waiting_for_subcategory(message, user_data):
    user_data["subcategory"] = message.strip()
    return "Got it! You can now reply with an optional comment or photo for backup.", "waiting_for_comment"

def handle_waiting_for_comment(message, user_data):
    user_data["comment"] = message.strip()

    append_to_sheet([
        user_data["room_number"],
        user_data["category"],
        user_data["subcategory"],
        user_data["comment"]
    ])

    return f"✅ Report saved for Room {user_data['room_number']}. Thank you!", "done"

