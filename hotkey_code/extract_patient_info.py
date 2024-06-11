import pyperclip
import keyboard
import re
import time

def reformat_name(full_name):
    if full_name:
        parts = full_name.strip().split()
        if len(parts) == 2:
            return f"{parts[1]}, {parts[0]}"
        elif len(parts) > 2:
            first_name = parts[0]
            last_name = parts[-1]
            middle_names = ' '.join(parts[1:-1])
            return f"{last_name}, {first_name} {middle_names}"
    return full_name or ""

def extract_patient_info():
    # Get the current clipboard content
    text = pyperclip.paste().strip()
    print(f"Original text: {text}")  # Debug print

    # Regex patterns
    name_pattern = r"Date:\s*\d{1,2}/\d{1,2}/\d{4}\s+([A-Za-z\s]+)"
    phone_pattern = re.compile(r"(Home|Mobile):\s*\((\d{3})\)\s*(\d{3})-(\d{4})")
    ssn_pattern = re.compile(r'(\d{3})-(\d{2})-(\d{4})')
    dob_pattern = re.compile(r"DOB:\s*(\d{1,2}/\d{1,2}/\d{4})")
    rid_pattern = re.compile(r"RID:\s*(\d+)")
    care_name_pattern = r"care manager, ([A-Za-z\s]+) at"
    care_email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    care_phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    
    # Extracted information
    pat_name = None
    phone_num = None
    ssn = None
    dob = None
    rid = None
    case_worker_name = None
    case_worker_phone_num = None
    case_worker_email = None
    address = None
    provider_address_pattern = re.compile(r"^Absolute Caregivers, Llc$", re.IGNORECASE)

    # Process each line in the text
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Patient Phone Number
        if "Home:" in line or "Mobile:" in line:
            match = phone_pattern.search(line)
            if match:
                phone_num = f"({match.group(2)}) {match.group(3)}-{match.group(4)}"
        
        # Patient Name
        if re.match(r"\bDate:\s*\d{1,2}/\d{1,2}/\d{4}\b", line):
            pat_name_line = lines[i + 5]  # Assuming name is 5 lines after the date line
            pat_name = pat_name_line.strip()

        # Patient Address
        if i > 2 and not provider_address_pattern.match(lines[i - 2]):  # Ensure we skip provider address
            if re.match(r"^\d{3,4} .*", line):
                address = line.strip() + " " + lines[i + 1].strip()

        # SSN    
        if "SSN: " in line:
            match = re.search(ssn_pattern, line)
            if match:
                ssn = f"{match.group(1)}{match.group(2)}{match.group(3)}"  # Remove dashes

        # DOB
        if "DOB: " in line:
            match = re.search(dob_pattern, line)
            if match:
                dob = match.group(1)
        
        # RID
        if "RID: " in line:
            match = re.search(rid_pattern, line)
            if match:
                rid = match.group(1)
        
        # Caregiver information
        if "If you have questions or concerns" in line:
            care_giver_block = ' '.join(lines[i:])
            name_match = re.search(care_name_pattern, care_giver_block)
            email_match = re.search(care_email_pattern, care_giver_block)
            phone_matches = re.findall(care_phone_pattern, care_giver_block.replace(" ", ""))
            case_worker_name = name_match.group(1).strip() if name_match else None
            case_worker_email = email_match.group() if email_match else None
            if phone_matches:
                phone_number = ''.join(phone_matches).replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
                if len(phone_number) == 10:  # Format phone number
                    case_worker_phone_num = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
            else:
                case_worker_phone_num = None
    
    # Format the information for Excel
    abs_num = f"ABS-{rid[-7:]}" if rid else ""
    formatted_pat_name = reformat_name(pat_name)
    formatted_case_worker_name = reformat_name(case_worker_name)
    age_formula = "=IFERROR((TODAY()-[@[DoB (MM/DD/YYYY)]])/365,\"N/A\")"
    
    # Ensure all details are strings
    details = [
        abs_num, "", formatted_pat_name, address, "", phone_num, dob, age_formula, "", "", "", "", "", ssn, "", rid, "", "", "", "", "", "", "", "N/A",
        formatted_case_worker_name, case_worker_phone_num, case_worker_email
    ]
    details = [str(detail) if detail is not None else "" for detail in details]
    
    combined_details = "\t".join(details)
    print(f"Combined details: {combined_details}")  # Debug print
    
    # Copy the combined details to the clipboard
    pyperclip.copy(combined_details)
    
    # Simulate Ctrl+V to paste the content
    time.sleep(0.5)  # Small delay to ensure the clipboard is ready
    keyboard.press_and_release('ctrl+v')