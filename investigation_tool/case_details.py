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
        choice = input("Enter the corresponding number (or type 'quit' to exit): ")
        if choice.lower() == 'quit':
            exit()
        if choice in case_types:
            return case_types[choice]

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
        choice = input("Enter the corresponding number (or type 'quit' to exit): ")
        if choice.lower() == 'quit':
            exit()
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
