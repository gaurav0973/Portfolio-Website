"""
Sending emails in python
"""

import smtplib
import ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "codejourneypanda@gmail.com"
    password = "vkpj zjwz vuxq yswb"


    receiver = "codejourneypanda@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context =  my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



# host = "smtp.gmail.com"
#     port = 465

#     username = "codejourneypanda@gmail.com"
#     password = "vkpj zjwz vuxq yswb"


#     receiver = "codejourneypanda@gmail.com"
#     my_context = ssl.create_default_context()

#     message = """\
#     Subject : Hi!
#     How are you?
#     bye!
#     """

#     with smtplib.SMTP_SSL(host, port, context =  my_context) as server:
#         server.login(username, password)
#         server.sendmail(username, receiver, message)
