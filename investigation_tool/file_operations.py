import os

def create_case_directory(case_number):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Investigations')
    case_path = os.path.join(desktop_path, f"Case_{case_number}")
    os.makedirs(case_path, exist_ok=True)
    return case_path

def create_investigation_file(case_directory, case_number):
    return os.path.join(case_directory, f"{case_number}.md")

def save_to_file(file_path, case_type, summary, actions):
    with open(file_path, 'a') as file:
        file.write("# Case Summary\n\n")
        file.write(f"## Case Type: {case_type}\n\n")
        file.write(f"### Actions Taken: {actions}\n\n")
        file.write(f"### Technical Summary:\n\n{summary}\n\n")
    print(f"Case summary saved to {file_path}")
