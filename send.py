import smtplib

from config import Configuration

class send_message():
        def email(subject, msg):

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(Configuration.EMAIL_ADDRESS, Configuration.PASSWORD)
                message = 'Subject: {}\n\n{}'.format(subject, msg)
                server.sendmail(Configuration.EMAIL_ADDRESS, Configuration.EMAIL_ADDRESS, message)
                server.quit()
                print("Success: Email sent!")




