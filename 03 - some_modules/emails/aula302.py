# EMAILS
# The Gmail interface changes a lot, so it may change the code too.

"""STEPS
1) Activate the IMAP configuration in the email;
2) https://www.cloudskillsboost.google/focuses/1071?locale=pt_BR&parent=catalog
"""

def main() -> None:
    """Function used to run the main code."""
    from dotenv import load_dotenv
    from pathlib import Path
    from string import Template
    import os
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    # Load environment variables
    load_dotenv()

    # Email details
    sender = os.getenv('EMAIL_FROM')
    recipient = sender  # Sending to myself

    # SMTP CONFIG
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = sender
    smtp_password = os.getenv("EMAIL_PASSWORD")

    # Data for the email body
    data = dict(
        name='Lucas',
        value=323.50,
        date='2024-05-21',
        enteprise='LS Enterprise',
        number='+88 (99) 4444-2222'
    )

    # Read the email template and substitute data
    file_path = Path(__file__).parent / 'aula302.txt'
    with open(file_path, 'r', encoding='utf8') as file:
        file_text = file.read()
        template = Template(file_text)
        email_text = template.substitute(data)

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'Fatura - Lucas'

    # Attach the email body
    part1 = MIMEText(email_text, 'plain', 'utf-8')
    msg.attach(part1)

    # Attach a file
    filename = r'.env-example'
    filepath = r'some_modules\\emails\\.env-example'
    with open(filepath, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
        msg.attach(part)

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        print(f'Email sent successfully to {data["name"]}!')

if __name__ == '__main__':
    main()