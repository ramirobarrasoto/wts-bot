from utils.sheet_service import append_to_sheet
from datetime import datetime

append_to_sheet([
    "Room 305",
    "Amenities delivery",
    "Requested shampoo and toothbrush",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
])

print("✅ Report sent to Google Sheets.")
