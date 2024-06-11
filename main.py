
import keyboard

from hotkey_code.case_manager_details import extract_contact_details
from hotkey_code.name_date import paste_name_with_date
from hotkey_code.reformat_name import reformat_name




# Define hotkeys for the functions
keyboard.add_hotkey('ctrl+shift+r', reformat_name)
keyboard.add_hotkey('ctrl+shift+e', extract_contact_details)
keyboard.add_hotkey('ctrl+shift+d', paste_name_with_date)

# Keep the script running
print("Press Ctrl+Shift+R to reformat the selected name.")
print("Press Ctrl+Shift+E to extract and reformat contact details.")
print("Press Ctrl+Shift+D to paste the name along with the current date.")
keyboard.wait('esc')  # Press 'esc' to stop the script
