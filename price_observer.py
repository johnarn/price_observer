import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import re
import time
import sys


def check_price():
    new_item_url = url.readline()

    while new_item_url:

        desirable_price = new_item_url.split(" ")[1]
        item_url = new_item_url.split(" ")[0]
        new_item_url = url.readline()

        page = requests.get(item_url, headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find('h1', {'class': 'page-title'})
        if title:
            title = soup.find('h1', {'class': 'page-title'}).get_text().strip()
            price = soup.find('span', {'class': 'price js-price'})
            if price:
                price = soup.find('span', {'class': 'price js-price'}).get_text().strip()
                converted_price_list = re.findall('\d+', price)
                converted_price = float(float(converted_price_list[0]) + float(converted_price_list[1]) * 0.01)
                print(title + ' at price: ' + str(converted_price))
                if converted_price < float(desirable_price):
                    send_email(title, converted_price, item_url)

        time.sleep(60 * 2)
    print("close")


def send_email(title, converted_price, item_url):
    subject = title
    message = title + " at price: " + str(converted_price) + '\n' + item_url

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()


credentials = sys.argv[1]
urls = sys.argv[2]

creds = open(credentials, "r")
email = creds.readline()
password = creds.readline()
send_to_email = creds.readline()
headers = creds.readline()
creds.close()
url = open(urls, "r")

while True:
    check_price()
    time.sleep(60 * 60 * 24)
