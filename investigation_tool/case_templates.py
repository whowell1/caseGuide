import os

def read_template_file(case_type, phishing=False):
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    if phishing:
        template_path = os.path.join(templates_path, 'case_template_phishing.md')
        if not os.path.exists(template_path):
            create_template_file(template_path, phishing=True)
    else:
        template_path = os.path.join(templates_path, 'case_template.md')
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
