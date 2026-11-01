import re

# TASK 3: TASK AUTOMATION WITH PYTHON SCRIPTS (Email Extractor)
def run_email_extractor():
    print("\n--- EMAIL ADDRESS EXTRACTOR ---")
    
    # Get input file name from user
    input_filename = input("Enter input text file name (default 'input.txt'): ").strip()
    if not input_filename:
        input_filename = "input.txt"
        
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"'{input_filename}' not found. Creating a sample file for demonstration.")
        text = "Hello support team, reach us at contact@python.org or admin@domain.co.in. For feedback use feedback@test.com."
        with open(input_filename, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Sample '{input_filename}' created successfully.")

    # Regular expression pattern to find email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    emails = re.findall(email_pattern, text)
    unique_emails = sorted(set(emails))
    
    if not unique_emails:
        print("No email addresses found in the file.")
        return
        
    lines = ["EXTRACTED EMAIL ADDRESSES REPORT", "-" * 32]
    
    print("\nExtracted Emails:")
    for email in unique_emails:
        print(email)
        lines.append(email)
        
    print(f"TOTAL EMAILS FOUND: {len(unique_emails)}")
    lines.append(f"TOTAL EMAILS FOUND: {len(unique_emails)}")
    lines.append("Note: Extracted using regular expressions (re) and file handling.")
    
    if input("Save report to emails_report.txt? (y/n): ").strip().lower() == "y":
        with open("emails_report.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(lines))
        print("Report saved successfully.")

if __name__ == "__main__":
    run_email_extractor()
