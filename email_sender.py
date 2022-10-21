import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send(sender, password, recipient, post, content):
    msg = MIMEMultipart()
    user = sender
    pass_word = password
    to = recipient
    msg['From'] = user
    msg['To'] = to
    subject = f'Application for the post of {post}'
    msg['Subject'] = subject
    body = content
    msg.attach(MIMEText(body, 'plain'))

    filename = 'JK_Resume.pdf'
    attachment = open('JK_Resume.pdf', "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    text = msg.as_string()

    try:
        smtp_server = smtplib.SMTP('smtp.office365.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(user, pass_word)
        smtp_server.sendmail(user, to, text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)
