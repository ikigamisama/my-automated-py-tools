import requests
import smtplib
import datetime

from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = datetime.datetime.now()
content = ''


def extract_news(url):
    print('Extracting Hacker News Stories . . . .')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + '<a href="' + tag.a.get(
            'href') + '">' + tag.text + '</a>' + '\n' + '<br>') if tag.text != 'More' else '')

    return cnt


content += extract_news('https://news.ycombinator.com/')
content += '<br>------<br>'
content += '<br><br>End of Message'

print('Composing Email...')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'kotascross22@gmail.com'
TO = 'ikigamidevs.15@gmail.com'
PASS = 'nfuqrztfjtkvhqcj'

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print("Initializing Error")

server = smtplib.SMTP(SERVER, PORT)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Send . . .')

server.quit()


