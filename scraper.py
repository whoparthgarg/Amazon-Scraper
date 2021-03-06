import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.in/-/hi/MYD82HN-A-New-Apple-MacBook/dp/B08N5WRWNW?ref_=ast_sto_dp&th=1'

headers={"User-Agent": 'GET-YOUR-DEVICE-USER-AGENT'}

def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    s=price[1:9]
    s=s.replace(',','')
    converted_price=float(s)

    print(converted_price)
    print(title.strip())

    if(converted_price<1400000):
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('parthgarg2013@gmail.com','GENERATE-YOUR-GMAIL-ACCOUNT-KEY')

    subject='Price fell down'
    body='Check the amazon link https://www.amazon.in/-/hi/MYD82HN-A-New-Apple-MacBook/dp/B08N5WRWNW?ref_=ast_sto_dp&th=1'

    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'parthgarg2013@gmail.com',
        'parthgarg2013@gmail.com',
        msg
    )
    
    print('Hey email has been sent!')

    server.quit()


while(True):
    check_price()
    time.sleep(60)
