import re
import time
import keyboard
import pyperclip


def extract_contact_details():
    text = pyperclip.paste().strip()
    print(f"Original text: {text}")  # Debug print

    # Remove line breaks to handle phone numbers split across lines
    text = text.replace('\n', ' ').replace('\r', ' ')
    print(f"Text after removing line breaks: {text}")  # Debug print

    # Extract name
    name_match = re.search(r'([A-Za-z]+) ([A-Za-z]+)', text)
    if name_match:
        first_name = name_match.group(1).title()
        last_name = name_match.group(2).title()
        formatted_name = f"{last_name}, {first_name}"
    else:
        formatted_name = ""
    print(f"Extracted name: {formatted_name}")  # Debug print
    
    # Extract phone number, handling cases with spaces
    phone_matches = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text.replace(" ", ""))
    if phone_matches:
        phone_number = ''.join(phone_matches).replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        if len(phone_number) == 10:  # Format phone number
            phone_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
    else:
        phone_number = ""
    print(f"Extracted phone number: {phone_number}")  # Debug print
    
    # Extract email
    email_match = re.search(r'\S+@\S+\.\S+', text)
    email = email_match.group(0) if email_match else ""
    print(f"Extracted email: {email}")  # Debug print
    
    # Combine extracted details with tabs
    combined_details = f"{formatted_name}\t{phone_number}\t{email}"
    print(f"Combined details: {combined_details}")  # Debug print
    
    pyperclip.copy(combined_details)
    # Simulate Ctrl+V to paste the content
    time.sleep(0.5)  # Small delay to ensure the clipboard is ready
    keyboard.press_and_release('ctrl+v')