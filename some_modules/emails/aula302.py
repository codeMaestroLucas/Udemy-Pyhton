# EMAILS
# The Gmail interface changes a lot, so it may change the code too.

# Ir atras disso

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


    
    file_path = Path(__file__).parent / 'aula302.txt'

    load_dotenv()
    
    sender = os.getenv('EMAIL_FROM', '')
    recipient = sender # Sending to myself

    # SMTP CONFIG
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = sender
    smtp_password = os.getenv("EMAIL_PASSWORD", '')


    # DATA
    data = dict(
        name= 'Lucas',
        value= 323.50,
        date= '2024-05-21',
        enteprise= 'LS Enterprise',
        number= '+88 (99) 4444-2222'
    )
    
    with open(file_path, 'r', encoding= 'utf8') as file:
        file_text = file.read()
        template = Template(file_text)
        email_text = template.substitute(data)
    
    # MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = 'Fatura - Lucas'

    # MIMEText
    part1 = MIMEText(email_text, 'plain', 'utf-8')
    msg.attach(part1)

    # Para anexar arquivos (opcional)
    # filename = 'nome_do_arquivo.extensao'
    # attachment = open('caminho/para/o/arquivo', 'rb')
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', f'attachment; filename={filename}')
    # msg.attach(part)


    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        print('Email sent successfully!')



if __name__ == '__main__':
    main()