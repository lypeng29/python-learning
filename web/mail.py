# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From:')
# password = input('Password:')
# to_addr = input('To:')
from_addr = '893371810@qq.com'
password = 'LYPENG8969*'
to_addr = 'liyongpeng3472@dingtalk.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
msg['From'] = _format_addr('python学习 <%s>' % from_addr)
msg['To'] = _format_addr('you <%s>' % to_addr)
msg['Subject'] = Header('主题', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

