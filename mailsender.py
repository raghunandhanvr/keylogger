# --> smtp lib, ssl

import smtplib, ssl

def sendmail(message):
    s_server = "smtp.gmail.com"
    port = 587
    send_mail = "seceminiproject@gmail.com"
    mail_password = "sriram@raghu"
    recv_mail = "r4ghunandhan@gmail.com"

    con = ssl.create_default_context()

    try:
        server = smtplib.SMTP(s_server, port)
        server.ehlo()
        server.starttls(context= con)
        server.ehlo()
        server.login(send_mail, mail_password)
        server.sendmail(sendmail, recv_mail, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()