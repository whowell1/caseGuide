import os
from datetime import datetime

def main():
    while True:
        case_number = input("Enter the case number or type 'exit()' to quit: ")
        if case_number.lower() == 'exit()':
            break
        
        case_directory = create_investigation_directory(case_number)
        file_path = os.path.join(case_directory, f"{case_number}.md")
        
        while True:
            case_type = select_case_type()
            summary = gather_case_details(case_type, file_path)
            actions = input("What actions did you take? ")
            
            save_to_file(file_path, case_type, summary, actions)

            go_back = input("Would you like to go back and change the case type? (yes/no): ")
            if go_back.lower() != 'yes':
                break

def create_investigation_directory(case_number):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Investigations', case_number)
    os.makedirs(desktop_path, exist_ok=True)
    return desktop_path

def select_case_type():
    case_types = {
        '1': 'Phishing',
        '2': 'Network',
        '3': 'Host',
        '4': 'Cloud',
        '5': 'Other'
    }
    while True:
        print("Select the type of case:")
        for key, value in case_types.items():
            print(f"{key}. {value}")
        choice = input("Enter the corresponding number: ")
        if choice in case_types:
            return case_types[choice]

def gather_case_details(case_type, file_path):
    if case_type == "Phishing":
        return gather_phishing_details(file_path)
    elif case_type == "Network":
        return gather_network_details()
    elif case_type == "Host":
        return gather_host_details(file_path)
    elif case_type == "Cloud":
        return gather_cloud_details()
    else:
        return gather_other_details()

def gather_phishing_details(file_path):
    email_from = input("Who was the email from? ")
    email_to = input("Who got the email? ")
    email_subject = input("What was the subject of the email? ")

    phishing_subtype = select_phishing_subtype()
    malicious = input("Was the email malicious? (yes/no): ")

    if malicious.lower() == 'yes':
        urls = input("Enter the list of URLs separated by commas: ").split(',')
        info_about_urls = input("Enter OSINT on URLs (separated by commas): ").split(',')
        urls.extend(info_about_urls)
        urls_defanged = [defang_url(url.strip()) for url in urls]
        if phishing_subtype == 'Credential Harvester':
            alerted_link = input("What is the alerted link? ")
            successful_deliveries = input("How many successful deliveries were there? ")
            emails_blocked = input("How many emails got blocked? ")
            technical_summary = (
                f"CSIRT received a potential phishing email.\n\n"
                f"- From: {email_from}\n"
                f"- To: {email_to}\n"
                f"- Subject: {email_subject}\n"
                f"- URLs: {', '.join(urls_defanged)}\n"
                f"- Alerted Link: {alerted_link}\n"
                f"- Successful Deliveries: {successful_deliveries}\n"
                f"- Emails Blocked: {emails_blocked}\n"
                f"- Malicious Intent: yes\n"
            )
            summary = (
                f"Phishing ({phishing_subtype})\n\n"
                f"Technical Summary:\n\n{technical_summary}"
            )
        else:
            technical_summary = (
                f"CSIRT received a potential phishing email.\n\n"
                f"- From: {email_from}\n"
                f"- To: {email_to}\n"
                f"- Subject: {email_subject}\n"
                f"- URLs: {', '.join(urls_defanged)}\n"
                f"- Malicious Intent: yes\n"
            )
            summary = (
                f"Phishing ({phishing_subtype})\n\n"
                f"Technical Summary:\n\n{technical_summary}"
            )
    else:
        false_positive_reason = input("Why is this a false positive? ")
        technical_summary = (
            f"CSIRT received a potential phishing email.\n\n"
            f"- From: {email_from}\n"
            f"- To: {email_to}\n"
            f"- Subject: {email_subject}\n"
            f"- Reason it is a False Positive: {false_positive_reason}\n"
        )
        summary = (
            f"Phishing ({phishing_subtype})\n\n"
            f"Technical Summary:\n\n{technical_summary}"
        )

    return summary

def select_phishing_subtype():
    subtypes = {
        '1': 'Toad',
        '2': 'Credential Harvester'
    }
    while True:
        print("Was it a potential Toad or Credential Harvester? (1 for Toad, 2 for Credential Harvester): ")
        choice = input("Enter the corresponding number: ")
        if choice in subtypes:
            return subtypes[choice]

def defang_url(url):
    return url.replace('.', '[.]').replace('https', 'hxxps')

def gather_network_details():
    operating_system = select_operating_system()
    root_cause = input("What was the root cause of the alert? ")
    rule = input("What was the rule of detection? ")
    summary = input("Write a technical summary: ")
    return f"Operating System: {operating_system}\n\n{summary}"

def select_operating_system():
    operating_systems = {
        '1': 'Windows',
        '2': 'Mac',
        '3': 'Linux'
    }
    while True:
        print("Enter the operating system: (1 for Windows, 2 for Mac, 3 for Linux): ")
        choice = input("Enter the corresponding number: ")
        if choice in operating_systems:
            return operating_systems[choice]

def gather_host_details(file_path):
    detection_type = input("Enter the type of detection: ")
    rule = input("What was the rule of detection? ")
    description = input("Write a description of the detection: ")

    notes = ""
    while True:
        note = input("Enter a note (or type 'done' to finish): ")
        if note.lower() == 'done':
            break
        notes += f"- {note}\n"

    root_cause = input("What was the root cause of the alert? ")

    screenshot_requested = False
    while not screenshot_requested:
        user_input = input("Press 'ss' to take a screenshot (or type 'done' to skip): ")
        if user_input.lower() == 'ss':
            screenshot_path = take_screenshot(file_path)
            print(f"Screenshot saved to {screenshot_path}")
            screenshot_requested = True
        elif user_input.lower() == 'done':
            screenshot_requested = True

    summary = (
        f"Detection Type: {detection_type}\n\n"
        f"- Rule of Detection: {rule}\n\n"
        f"- Description: {description}\n\n"
        f"Notes:\n{notes}\n"
        f"Root Cause: {root_cause}"
    )
    return summary

def take_screenshot(file_path):
    import pyautogui
    screenshot = pyautogui.screenshot()
    screenshot_path = f"{os.path.dirname(file_path)}/screenshot.png"
    screenshot.save(screenshot_path)
    return screenshot_path

def gather_cloud_details():
    root_cause = input("What was the root cause of the alert? ")
    rule = input("What was the rule of detection? ")
    summary = input("Write a technical summary: ")
    return f"Root Cause: {root_cause}\n\n{summary}"

def gather_other_details():
    root_cause = input("What was the root cause of the alert? ")
    rule = input("What was the rule of detection? ")
    summary = input("Write a technical summary: ")
    return f"Root Cause: {root_cause}\n\n{summary}"

def save_to_file(file_path, case_type, summary, actions):
    with open(file_path, 'a') as file:
        file.write("Case Summary\n\n")
        file.write(f"Case Type: {case_type}\n\n")
        file.write(f"Actions Taken: {actions}\n\n")
        file.write(f"Technical Summary:\n\n{summary}\n\n")
    print(f"Case summary saved to {file_path}")

if __name__ == "__main__":
    main()
