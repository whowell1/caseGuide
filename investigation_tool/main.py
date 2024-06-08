from file_operations import create_case_directory, create_investigation_file, save_to_file
from case_templates import read_template_file
from case_details import gather_case_details, select_case_type
import os

def main():
    while True:
        case_number = input("Enter the case number (or type 'quit' to exit): ")
        if case_number.lower() == 'quit':
            break

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

if __name__ == "__main__":
    main()
