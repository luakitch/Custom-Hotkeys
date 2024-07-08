import pyperclip
import keyboard
import time
from datetime import datetime
import re

def extract_info_and_paste():
    # Get the current clipboard content
    text = pyperclip.paste().strip()

    # Extract patient name
    name_start = text.find("Patient name") + len("Patient name")
    name_end = text.find("Member number")
    full_name = text[name_start:name_end].strip().title()

    # Use today's date
    now = datetime.now()
    current_date = now.strftime("%d %b %Y")
    if current_date[0] == '0':
        current_date = current_date[1:]

    # Extract relevant text section
    coverage_start = text.find("Coverage status")
    clinical_notes_start = text.find("Clinical notes")
    relevant_text = text[coverage_start:clinical_notes_start]

    # Extract service codes and map to abbreviations
    service_code_map = {
        "S5140": "SFC",
        "T2022": "IHCC",
        "S5161": "PERS",
        "S5160": "PERS Install",
        "S5125": "ATTC",
        "B4150": "NUTS",
        "S5130": "HMK"
    }

    # Find all procedure codes in the relevant text
    service_codes = re.findall(r'\bS\d{4}\b|\bT\d{4}\b|\bB\d{4}\b', relevant_text)
    service_abbrs = [service_code_map.get(code, "UNKNOWN") for code in service_codes]
    services = ' '.join(service_abbrs)

    # Combine the name, services, and date
    combined_details = f"Anthem {full_name} {services} {current_date}"
    print(f"Combined details: {combined_details}")  # Debug print

    # Copy the combined details to the clipboard
    pyperclip.copy(combined_details)

    # Simulate Ctrl+V to paste the content
    time.sleep(0.5)  # Small delay to ensure the clipboard is ready
    keyboard.press_and_release('ctrl+v')

