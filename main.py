
import keyboard

from hotkey_code.case_manager_details import extract_contact_details
from hotkey_code.extract_patient_info import extract_patient_info
from hotkey_code.united_save_info import extract_info_and_paste
from hotkey_code.reformat_name import reformat_name




# Define hotkeys for the functionsDed Text Here 8 Jul 2024 UNKNOWN
keyboard.add_hotkey('ctrl+shift+r', reformat_name)
keyboard.add_hotkey('ctrl+shift+e', extract_contact_details)
keyboard.add_hotkey('ctrl+shift+d', extract_info_and_paste)
keyboard.add_hotkey('ctrl+alt+p', extract_patient_info)

# Keep the script running
print("Press Ctrl+Shift+R to reformat the selected name.")
print("Press Ctrl+Shift+E to extract and reformat contact details.")
print("Press Ctrl+Shift+D to paste the name along with the current date.")
print("Press Ctrl+Alt+P to extract and paste patient information.")
keyboard.wait('ctrl+alt+shift+d')  # Press 'esc' to stop the script
