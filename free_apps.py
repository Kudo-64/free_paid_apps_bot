import requests, datetime, time
from os import system
from telegram import ParseMode
from telegram.ext import *
from bs4 import BeautifulSoup

API_KEY = <put_your_API_key_here>

cata_list=['Action','Adventure','Arcade','Board','Card','Casino','Casual','Educational','Music','Puzzle','Racing','Role Playing','Simulation','Sports','Strategy','Trivia','Word']


ios_links = []
ios_prices = []
ios_classType = []
ios_last_checked = datetime.datetime(2009, 12, 2, 10, 24, 34, 198130)

android_links = []
android_prices = []
android_classType = []
android_last_checked = datetime.datetime(2009, 12, 2, 10, 24, 34, 198130)

def grab_android():
    global android_last_checked

    while len(ios_links) > 0 : ios_links.pop()
    while len(ios_prices) > 0 : ios_prices.pop()
    while len(ios_classType) > 0 : ios_classType.pop()

    headers={'User-Agent':'Mozilla/5.0'}
    url = "https://yofreesamples.com/entertainment-freebies/free-google-play-android-apps-today/"
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, features="lxml")

    aas = soup.find_all('a', class_="read-more-link button offer_button_single external_link_button")
    pps = soup.find_all('p',class_='p0 m0')

    for i in range(len(aas)):
        price = pps[i].text.split()[-1]
        link = aas[i].get('href')
        android_links.append(link)
        android_prices.append(price)

        response_filter = requests.get(link) # Getting the store page
        soup_filter = BeautifulSoup(response_filter.text, features="lxml")
        # ##
        dd_s = soup_filter.find_all('span',class_='VfPpkd-vQzf8d')
        catagory = dd_s[2].text.strip()
        if catagory in cata_list:
            android_classType.append("g")
        elif catagory == 'Personalization':
            android_classType.append("p")
        else:
            android_classType.append("a")
    android_last_checked = datetime.datetime.now()

def grab_ios():
    global ios_last_checked

    while len(ios_links) > 0 : ios_links.pop()
    while len(ios_prices) > 0 : ios_prices.pop()
    while len(ios_classType) > 0 : ios_classType.pop()

    headers={'User-Agent':'Mozilla/5.0'}
    url = 'https://yofreesamples.com/entertainment-freebies/free-apple-app-store-iphone-ipad-apps-today/'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, features="lxml")

    aas = soup.find_all('a', class_="read-more-link button offer_button_single external_link_button")
    pps = soup.find_all('p',class_='p0 m0')

    for i in range(len(aas)):
        price = pps[i].text.split()[-1]
        link = aas[i].get('href')
        ios_links.append(link)
        ios_prices.append(price)

        response_filter = requests.get(link)
        soup_filter = BeautifulSoup(response_filter.text, features="lxml")
        dd_s = soup_filter.find_all('dd',class_='information-list__item__definition')
        catagory = dd_s[2].text.strip()
        if ':' in catagory:
            catagory = catagory.split(':')[0]
            if catagory == 'Games':
                ios_classType.append("g")
            else:
                ios_classType.append("a")
        else:
            if catagory == 'Games':    
                ios_classType.append("g")
            else:
                ios_classType.append("a")

    ios_last_checked = datetime.datetime.now()

def send(update,context):
    x=0
    for i,kind in enumerate(ios_classType):
        if kind=="a":
            text = "🔷 <b>Previous Price:</b> "+ios_prices[i]+"\n"+f"🔗 <a href='{str(ios_links[i])}'><b>Check out !</b></a>"+'\n\n.'
            update.message.reply_text(text,disable_web_page_preview=False,parse_mode='HTML')
            x +=1
            if x == 25 or x == 50 or x == 75:
                time.sleep(2)

def send_games(update,context):
    x=0
    for i,kind in enumerate(ios_classType):
        if kind=="g":
            text = "🔷 <b>Previous Price:</b> "+ios_prices[i]+"\n"+f"🔗 <a href='{str(ios_links[i])}'><b>Check out !</b></a>"+'\n\n.'
            update.message.reply_text(text,disable_web_page_preview=False,parse_mode='HTML')
            x +=1
            if x == 25 or x == 50 or x == 75:
                time.sleep(2)

###### 
def send_apps_android(update,context):
    x=0
    for i,kind in enumerate(android_classType):
        if kind=="a":
            text = "🔷 <b>Previous Price:</b> "+android_prices[i]+"\n"+f"🔗 <a href='{str(android_links[i])}'><b>Check out !</b></a>"+'\n\n.'
            update.message.reply_text(text,disable_web_page_preview=False,parse_mode='HTML')
            x +=1
            if x == 25 or x == 50 or x == 75:
                time.sleep(2)

def send_games_android(update,context):
    x=0
    for i,kind in enumerate(android_classType):
        if kind=="g":
            text = "🔷 <b>Previous Price:</b> "+android_prices[i]+"\n"+f"🔗 <a href='{str(android_links[i])}'><b>Check out !</b></a>"+'\n\n.'
            update.message.reply_text(text,disable_web_page_preview=False,parse_mode='HTML')
            x +=1
            if x == 25 or x == 50 or x == 75:
                time.sleep(2)


def send_packs_android(update,context):
    x=0
    for i,kind in enumerate(android_classType):
        if kind=="p":
            text = "🔷 <b>Previous Price:</b> "+android_prices[i]+"\n"+f"🔗 <a href='{str(android_links[i])}'><b>Check out !</b></a>"+'\n\n.'
            update.message.reply_text(text,disable_web_page_preview=False,parse_mode='HTML')
            x +=1
            if x == 25 or x == 50 or x == 75:
                time.sleep(2)


def start_command(update,context):
    update.message.reply_text('🤖 Welcom to my Bot')
    update.message.reply_text('🚀 Check the commands available at the left bottom to get started !')
    
def doing_command_ios(update,context):

    user_name = update.message.chat.first_name
    update.message.reply_text('Hi '+user_name+' !')
    update.message.reply_text('Please wait a moment while scraping new apps ...')

    delta = datetime.datetime.now() - ios_last_checked
    if delta.total_seconds()/3600 > 12:
        grab_ios()
    send(update,context)

    now = datetime.datetime.now()
    qs = '🔶 Last Update Was :-'
    year = str(now.strftime("%Y / %B / %d"))
    tim = str(now.strftime("%a - %H:%M"))
    update.message.reply_text(f"<b>{qs}</b>"+'\n🗓 '+year+'\n🕰 '+tim,parse_mode=ParseMode.HTML)


def doing_command_games_ios(update,context):
    user_name = update.message.chat.first_name
    update.message.reply_text('Hi '+user_name+' !')
    update.message.reply_text('Please wait a moment while scraping new games ...')

    delta = datetime.datetime.now() - ios_last_checked   
    if delta.total_seconds()/3600 > 12:
        grab_ios()
    send_games(update,context)

    now = datetime.datetime.now()
    qs = '🔶 Last Update Was :-'
    year = str(now.strftime("%Y / %B / %d"))
    tim = str(now.strftime("%a - %H:%M"))
    update.message.reply_text(f"<b>{qs}</b>"+'\n🗓 '+year+'\n🕰 '+tim,parse_mode=ParseMode.HTML)

# ####################################

def doing_command_android(update,context):

    user_name = update.message.chat.first_name
    update.message.reply_text('Hi '+user_name+' !')
    update.message.reply_text('Please wait a moment while scraping new apps ...')

    delta = datetime.datetime.now() - android_last_checked
    if delta.total_seconds()/3600 > 12:
        grab_android()
    send_apps_android(update,context)

    now = datetime.datetime.now()
    qs = '🔶 Last Update Was :-'
    year = str(now.strftime("%Y / %B / %d"))
    tim = str(now.strftime("%a - %H:%M"))
    update.message.reply_text(f"<b>{qs}</b>"+'\n🗓 '+year+'\n🕰 '+tim,parse_mode=ParseMode.HTML)

def doing_games_android(update,context):
    user_name = update.message.chat.first_name
    update.message.reply_text('Hi '+user_name+' !')
    update.message.reply_text('Please wait a moment while scraping new games ...')

    delta = datetime.datetime.now() - android_last_checked
    if delta.total_seconds()/3600 > 12:
        grab_android()
    send_games_android(update,context)

    now = datetime.datetime.now()
    qs = '🔶 Last Update Was :-'
    year = str(now.strftime("%Y / %B / %d"))
    tim = str(now.strftime("%a - %H:%M"))
    update.message.reply_text(f"<b>{qs}</b>"+'\n🗓 '+year+'\n🕰 '+tim,parse_mode=ParseMode.HTML)

def doing_packs_android(update,context):
    user_name = update.message.chat.first_name
    update.message.reply_text('Hi '+user_name+' !')
    update.message.reply_text('Please wait a moment while scraping new games ...')

    delta = datetime.datetime.now() - android_last_checked
    if delta.total_seconds()/3600 > 12:
        grab_android()
    send_packs_android(update,context)

    now = datetime.datetime.now()
    qs = '🔶 Last Update Was :-'
    year = str(now.strftime("%Y / %B / %d"))
    tim = str(now.strftime("%a - %H:%M"))
    update.message.reply_text(f"<b>{qs}</b>"+'\n🗓 '+year+'\n🕰 '+tim,parse_mode=ParseMode.HTML)


def main():
    
    updater = Updater(API_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("ios_apps",doing_command_ios))
    dp.add_handler(CommandHandler("ios_games",doing_command_games_ios))
    dp.add_handler(CommandHandler("android_apps",doing_command_android))
    dp.add_handler(CommandHandler("android_games",doing_games_android))
    dp.add_handler(CommandHandler("android_packs",doing_packs_android))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
