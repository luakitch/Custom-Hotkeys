import time
import keyboard
import pyperclip


def reformat_name():
    full_name = pyperclip.paste().strip()
    print(f"Original name: {full_name}")  # Debug print

    name_parts = full_name.split()
    if len(name_parts) >= 2:
        first_name = ' '.join(name_parts[:-1])
        last_name = name_parts[-1]
        
        first_name = first_name.title()
        last_name = last_name.title()
        
        formatted_name = f"{last_name}, {first_name}"
        print(f"Formatted name: {formatted_name}")  # Debug print
        
        pyperclip.copy(formatted_name)
        # Simulate Ctrl+V to paste the content
        time.sleep(0.5)  # Small delay to ensure the clipboard is ready
        keyboard.press_and_release('ctrl+v')
    else:
        print("Name format is incorrect.")  # Debug print