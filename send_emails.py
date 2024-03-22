import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
from datetime import datetime

# Read the CSV file containing the email IDs and company names
hr_list = pd.read_csv('hr_email_and_name_list.csv')

# Set up email server and login credentials
smtp_server = 'smtp-mail.outlook.com'
smtp_port = 587  # Use 587 for TLS
smtp_username = 'example@outlook.com'
smtp_password = '12345678'

# Compose your email
sender_email = 'example@outlook.com'

# Path to your resume file
resume_file_path = 'Resume.pdf'

# Iterate over each HR email and send the email with resume attachment
for index, row in hr_list.iterrows():
    hr_email = row['email']
    company_name = row['company_name']
    subject = f'Application for Software Developer Position at {company_name}'
    message_body = f'''
    Dear Hiring Manager,

    I hope this email finds you well. My name is Prem Ganwani, and I am writing to express my genuine interest in the Software Developer position at {company_name}.

    {company_name}'s reputation for excellence and innovation in the tech industry has caught my attention. I am particularly impressed by {company_name}'s commitment to pushing technological boundaries and delivering top-notch solutions. Throughout my internships and professional experiences, I have led projects such as developing an HR Management System (HRMS) using OutSystems and architecting backend APIs for platforms like BookMyShow. These experiences have honed my skills in software development, preparing me to excel in a dynamic work environment like yours.

    Thank you for considering my application. I am eager to discuss how my background and aspirations align with the Software Developer position at {company_name}. Please let me know a convenient time for an interview.

    Warm regards,

    Prem Ganwani  
    prem.codez@gmail.com  
    +917427087287
    '''

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = hr_email
    msg['Subject'] = subject

    # Attach message body
    msg.attach(MIMEText(message_body, 'plain'))

    # Attach resume file
    with open(resume_file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {resume_file_path.split("/")[-1]}')
        msg.attach(part)

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            # Login to your account
            server.login(smtp_username, smtp_password)
            # Send email
            server.sendmail(sender_email, hr_email, msg.as_string())
        
        # Print success message after successful email delivery
        print(f"{datetime.now()}: Iteration {index + 1}: Email successfully sent to: {hr_email}")
    
    except Exception as e:
        # Print error message if email delivery fails
        print(f"{datetime.now()}: Failed to send email to {hr_email}: {str(e)}")
        continue
    
    # Add delay of 3 minutes after each successful email
    delay = 180  
    print(f"Waiting for {delay} seconds before sending the next email...")
    time.sleep(delay)

print("All emails sent successfully.")