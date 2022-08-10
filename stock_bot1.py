#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 19:53:10 2022

@author: tsaipoliang
"""

import requests
from bs4 import BeautifulSoup
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import datetime,time

def yahoo_stock_crawler(stock):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                           AppleWebKit/537.36 (KHTML, like Gecko) \
                           Chrome/102.0.0.0 Safari/537.36'}
    url=f'https://finance.yahoo.com/quote/{stock}?p={stock}'
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text, 'lxml')
    price=soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    return float(price.text)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('SUJCU2yVlEe6s93XZm4ssrbHj1Zax1lz4m429ZYUNAzUxXUQxalGBUOyGNU383UhYa1IDsQpeauu9WJa7I')
# 必須放上自己的Channel Secret
handler = WebhookHandler('d68c5d0543cba2367f26f7922f6b74a6')

line_bot_api.push_message('U9a880705aba3434ff1b4c8bcad222f79', TextSendMessage(text='2330 get stock start'))

#for i in range(0,5):
#    price=yahoo_stock_crawler('2330.TW')+datetime.datetime.now()
#    line_bot_api.push_message('U9a880705aba3434ff1b4c8bcad222f79', TextSendMessage(text=price))
#    time.sleep(60)

#print(price)
#print(type(price))