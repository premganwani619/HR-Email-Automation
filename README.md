# HR Email Sender

This script sends job application emails to HR contacts listed in a CSV file.

## Prerequisites

- Python 3
- pandas
- smtplib
- email

## Usage

1. Place your resume file named `Resume.pdf` in the same directory as this script.
2. Update the `hr_email_and_name_list.csv` file with HR email addresses and company names.
3. Modify the SMTP server details, sender email, and sender email password in the script.
4. Run the script.

## Script Details

- The script reads HR email addresses and company names from a CSV file.
- It sends personalized emails to each HR contact with a resume attachment.
- After sending each email, it waits for 3 minutes before sending the next email.

## Author

Prem Ganwani - prem.codez@gmail.com


# Write content to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)

print("README.md generated successfully.")
