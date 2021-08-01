import requests
from bs4 import BeautifulSoup 
from apscheduler.schedulers.blocking import BlockingScheduler
from pync import Notifier
from datetime import datetime
import emoji

def grab_data():
    url = "https://coinmarketcap.com/currencies/bitcoin/"
    r = requests.get(url = url)
    soup = BeautifulSoup(r.text)
    price = soup.find('div',{"class":"priceValue___11gHJ"})
    perchange = soup.find('span',{"class":"feeyND"})
    pos = perchange.find('span',{"class":"icon-Caret-up"})
    neg = perchange.find('span',{"class":"icon-Caret-down"})
    if(pos):
      change = '+'+perchange.text
    elif(neg):
       change = '-'+perchange.text

    #printing
    print("BITCOIN")
    print("Price :",price.text) 
    print("Change :",change)

    #toast
    msg = f'price : {price.text}, change % : {change}'
    Notifier.notify(msg,title="Bitcoin \U0001F4B9")


scheduler = BlockingScheduler()
scheduler.add_job(grab_data,'interval', seconds=60)
scheduler.start()