from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from info import *
import smtplib

# mail_list = ["5983495@qq.com"]
mail_list = ["513234541@qq.com"]
mail_host = "smtp.qq.com"
mail_user = "329103586"
mail_pass = "gqfumcntovhfbjgc"
mail_postfix = "qq.com"
# 

def send_mail(to_list, sub, content):
    me = "LoveLetter" + str((d2-d1).days - 68) + "<"+mail_user+"@"+mail_postfix+">"
    #msg = MIMEText(content.encode('utf-8'), 'plain', 'utf-8')
    msg = MIMEMultipart('related')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    part1 = MIMEText("<html><body><p> " + content1 + " </p><img src='cid:Love1' alt='Love1'></body></html>", 'html', 'utf-8')
    msg.attach(part1)

    part2 = MIMEImage(open('./love/Love (' + str((d2-d1).days - 68) + ').jpg', 'rb').read())
    part2.add_header('Content-ID', 'Love1')
    msg.attach(part2)

    # part = MIMEText(content.encode('utf-8'), 'plain', 'utf-8')
    # msg.attach(part)

    try:
        s = smtplib.SMTP_SSL(mail_host, 465)
        s.set_debuglevel(1)
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print e
        return False
if __name__ == '__main__':
    if send_mail(mail_list, 'LoveLetter', content1):
        print "done"
    else:
        print "wrong"
