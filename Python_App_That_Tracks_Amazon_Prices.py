# App to track website price and alert the user with an email
# Reference: https://www.youtube.com/watch?v=Bg9r_yLk7VY

# Required Libraries
import requests as req
from bs4 import BeautifulSoup as bs
import smtplib

#Provide the Url here
URL = 'https://www.amazon.com.au/Ingenuity-InLighten-Cradling-Rocker-Unicorn/dp/B07NPLRQRG/ref=sr_1_fkmr0_2?keywords=Ingenuity+SimpleComfort+Cradling+Swing+Everston&qid=1568091870&s=gateway&sr=8-2-fkmr0'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# Function to check the price of URL and if condition satisfies calls the send email method
def check_price():
    # Download the webpage content and initialise the BeautifulSoup html parser
    page = req.get(URL, headers=headers)
    soup = bs(page.content, 'html.parser')

    # Get the price from downloaded website content
    #price = soup.find('div',{'class':"price-only"}).get_text()
    #price = soup.find('div',{'class':"current-price"})
    price = soup.find('span',attrs={'id':'priceblock_ourprice'}).get_text()
    print(price)
    converted_price = float(price[1:7])

    if(converted_price < 259.0):
        send_mail()

# Function to send email alert using gmail app passowords
def send_mail():
    print("entered into send mail function")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('vid.dhamo@gmail.com','jjsezxkjnncevguo')

    subject = 'Price Fell Down'
    body = 'Check the amazon link https://www.amazon.com.au/Ingenuity-InLighten-Cradling-Rocker-Unicorn/dp/B07NPLRQRG/ref=sr_1_fkmr0_2?keywords=Ingenuity+SimpleComfort+Cradling+Swing+Everston&qid=1568091870&s=gateway&sr=8-2-fkmr0'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('vid.damo@gmail.com','d.vidhyasagar@gmail.com',msg)
    print("Email has been sent")

    server.quit()


check_price()


