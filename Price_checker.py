# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:18:41 2019

@author: 91855
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.amazon.in/Digitek-DTR-550-LW-Tripod/dp/B074CWD7MS/ref=sr_1_2_sspa?keywords=camera&qid=1566312575&s=gateway&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQUYyVDVYWlI2STE2JmVuY3J5cHRlZElkPUEwNTA2NTc1VUtMWkRUVVZIUkE4JmVuY3J5cHRlZEFkSWQ9QTA3MDYwMDczT1NVWURGWFREQTJTJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="


header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
page = requests.get(url, headers=header)
    
soup = BeautifulSoup(page.content, 'html.parser')
    
title = soup.find(id="productTitle").get_text().strip()
    
def checker():
    
    price = soup.find(id="priceblock_ourprice").get_text()
    
    converted_price = float(price[1:].replace(',',''))
    
    if converted_price < 1700:
        send_email()

def send_email():
    user = 'naveen.rawatgt@gmail.com'
    pass_code = 'fbpxrhazysctqymx'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.ehlo()
    
    server.starttls()
    
    server.ehlo()
    
    server.login(user, pass_code)
    
    subject = f"Prices fall down for {title}"
    
    body = f"Please checkout the link : {url}"
    
    msg = f"Subject : {subject} \n\n {body}"
    
    server.sendmail(user,
                    'naveen.rawatgt@gmail.com',
                    msg
                    )
    
    print("Email send!")
    
    server.quit()
    
while True:
    checker()
    time.sleep(200)
 
    