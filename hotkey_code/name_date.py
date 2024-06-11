import pyperclip
import keyboard
import time
from datetime import datetime

def paste_name_with_date():
    # Get the current clipboard content
    full_name = pyperclip.paste().strip()
    print(f"Original name: {full_name}")  # Debug print

    # Get the current date
    now = datetime.now()
    current_date = f"{now.month}/{now.day}/{now.year}"
    print(f"Current date: {current_date}")  # Debug print

    # Combine the name and the date
    combined_details = f"{full_name} {current_date}"
    print(f"Combined details: {combined_details}")  # Debug print
    
    # Copy the combined details to the clipboard
    pyperclip.copy(combined_details)
    
    # Simulate Ctrl+V to paste the content
    time.sleep(0.5)  # Small delay to ensure the clipboard is ready
    keyboard.press_and_release('ctrl+v')

