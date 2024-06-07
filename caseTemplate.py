import os

def main():
    case_number = input("Enter the case number: ")
    case_directory = create_case_directory(case_number)
    file_path = create_investigation_file(case_directory, case_number)
    
    while True:
        case_type = select_case_type()

        use_template = input("Would you like to use the case template? (yes/no): ")
        
        if use_template.lower() == 'yes':
            if case_type == 'Phishing':
                summary = read_template_file(case_type, phishing=True)
            else:
                summary = read_template_file(case_type, phishing=False)
        else:
            summary = gather_case_details(case_type)
        
        actions = input("What actions did you take? ")
        
        save_to_file(file_path, case_type, summary, actions)

        go_back = input("Would you like to go back and change the case type? (yes/no): ")
        if go_back.lower() != 'yes':
            break

def create_case_directory(case_number):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Investigations')
    case_path = os.path.join(desktop_path, f"Case_{case_number}")
    os.makedirs(case_path, exist_ok=True)
    return case_path

def create_investigation_file(case_directory, case_number):
    return os.path.join(case_directory, f"{case_number}.md")

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

def read_template_file(case_type, phishing=False):
    if phishing:
        template_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Investigations', 'case_template_phishing.md')
        if not os.path.exists(template_path):
            create_template_file(template_path, phishing=True)
    else:
        template_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Investigations', 'case_template.md')
        if not os.path.exists(template_path):
            create_template_file(template_path, phishing=False)
    
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
    
    return template_content.replace("{{case_type}}", case_type)

def create_template_file(template_path, phishing=False):
    with open(template_path, 'w') as template_file:
        if phishing:
            template_file.write(
                "## Case Type\n{{case_type}}\n\n"
                "## Email From\nWho was the email from?\n\n"
                "## Email To\nWho got the email?\n\n"
                "## Subject\nWhat was the subject of the email?\n\n"
                "## Alerted Link\nWhat was the alerted link?\n\n"
                "## Number of Emails Sent\nEnter the number of emails sent:\n\n"
                "## Emails Blocked\nHow many emails were blocked?\n\n"
                "## Emails Sent\nHow many emails were sent?\n\n"
                "## Emails Removed\nHow many emails were removed?\n\n"
                "## Number of Clicks\nEnter the number of clicks:\n\n"
                "## Job Description of User Alerted\nWhat is the job description of the person that alerted?\n\n"
                "## Reset Password\nWas the password reset? (yes/no)\n\n"
                "## Vendor\nWhat was the vendor?\n\n"
                "## Blocked URL\nEnter the blocked URL:\n\n"
                "## Notes\nAny additional notes?\n\n"
                "## Technical Summary\nWrite a technical summary:\n\n"
            )
        else:
            template_file.write(
                "## Case Type\n{{case_type}}\n\n"
                "## Host Type\nWhat type of host alerted?\n\n"
                "## User Alerted\nWho/what user alerted?\n\n"
                "## Job Description of User Alerted\nWhat is the job description of the person that alerted?\n\n"
                "## Files Alerted\nEnter the files that alerted (separated by commas):\n\n"
                "## Notes\nAny additional notes?\n\n"
                "## Technical Summary\nWrite a technical summary:\n\n"
            )

def gather_case_details(case_type):
    if case_type == "Phishing":
        return gather_phishing_details()
    elif case_type == "Network":
        return gather_network_details()
    elif case_type == "Host":
        return gather_host_details()
    elif case_type == "Cloud":
        return gather_cloud_details()
    else:
        return gather_other_details()

def gather_phishing_details():
    email_from = input("Who was the email from? ")
    email_to = input("Who got the email? ")
    email_subject = input("What was the subject of the email? ")
    alerted_link = input("What was the alerted link? ")
    num_emails_sent = input("Enter the number of emails sent: ")
    emails_blocked = input("How many emails were blocked? ")
    emails_sent = input("How many emails were sent? ")
    emails_removed = input("How many emails were removed? ")
    num_clicks = input("Enter the number of clicks: ")
    job_desc = input("What is the job description of the person that alerted? ")
    reset_password = input("Was the password reset? (yes/no): ")
    vendor = input("What was the vendor? ")
    blocked_url = input("Enter the blocked URL: ")
    
    notes = input("Any additional notes? ")
    technical_summary = input("Write a technical summary: ")

    summary = (
        f"Phishing\n\n"
        f"Email From: {email_from}\n\n"
        f"Email To: {email_to}\n\n"
        f"Subject: {email_subject}\n\n"
        f"Alerted Link: {alerted_link}\n\n"
        f"Number of Emails Sent: {num_emails_sent}\n\n"
        f"Emails Blocked: {emails_blocked}\n\n"
        f"Emails Sent: {emails_sent}\n\n"
        f"Emails Removed: {emails_removed}\n\n"
        f"Number of Clicks: {num_clicks}\n\n"
        f"Job Description of User Alerted: {job_desc}\n\n"
        f"Reset Password: {reset_password}\n\n"
        f"Vendor: {vendor}\n\n"
        f"Blocked URL: {blocked_url}\n\n"
        f"Notes: {notes}\n\n"
        f"Technical Summary: {technical_summary}"
    )

    return summary

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

def gather_host_details():
    detection_type = input("Enter the type of detection: ")
    rule = input("What was the rule of detection? ")
    description = input("Write a description: ")
    root_cause = input("What was the root cause of the alert? ")
    return f"Detection Type: {detection_type}\n\n- Rule of Detection: {rule}\n\n- Description: {description}\n\nRoot Cause: {root_cause}"

def gather_cloud_details():
    root_cause = input("What was the root cause of the alert? ")
    rule = input("What was the rule of detection? ")
    summary = input("Write a technical summary: ")
    return summary

def gather_other_details():
    root_cause = input("What was the root cause of the alert? ")
    rule = input("What was the rule of detection? ")
    summary = input("Write a technical summary: ")
    return summary

def save_to_file(file_path, case_type, summary, actions):
    with open(file_path, 'a') as file:
        file.write("# Case Summary\n\n")
        file.write(f"## Case Type: {case_type}\n\n")
        file.write(f"### Actions Taken: {actions}\n\n")
        file.write(f"### Technical Summary:\n\n{summary}\n\n")
    print(f"Case summary saved to {file_path}")

if __name__ == "__main__":
    main()
