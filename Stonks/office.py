import telebot
import csv
import pandas as pd
import csv
from tqdm.auto import tqdm
from collections import Counter
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

with open('office_corpus.csv', 'r', encoding='utf-8',  newline='', errors='ignore') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
data = pd.DataFrame(rows)

interaction_df = pd.read_csv('final-2.csv', sep='\t')


def character_get(character):
    dic_values = {}
    for i in range(len(interaction_df)):
        if str(interaction_df['source'][i]).strip() == character or str(interaction_df['target'][i]).strip() == character:
            if str(interaction_df['target'][i]).strip()!=character:
                dic_values[str(interaction_df['target'][i])] = interaction_df['value'][i]
            else:
                dic_values[str(interaction_df['source'][i])] = interaction_df['value'][i]
    return dic_values


def cleaning(clean, fw, stop):
    for k in fw:
        if k not in stop:
            clean.append(k)
    return Counter(clean).most_common(10)


michael = []
dwight = []
kevin = []
andy = []
jim = []
pam = []
erin = []
ryan = []
oscar = []
angela = []

for i in tqdm(range(len(data))):
    if data.loc[i]['﻿SPEAKER'] == 'Michael':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               michael.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Jim':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               jim.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Dwight':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               dwight.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Pam':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               pam.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Andy':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               andy.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Kevin':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               kevin.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Angela':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               angela.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Oscar':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               oscar.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Erin':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               erin.append(j)
    if data.loc[i]['﻿SPEAKER'] == 'Ryan':
        utter = data.loc[i]['UTTERANCE']
        utter = utter.replace('.', '')
        utter = utter.replace(',', '')
        utter = utter.replace('!', '')
        utter = utter.replace('?', '')
        for j in utter.split():
               ryan.append(j)


token = '1235319864:AAErBd1NgrDwu5QTPoe_9yMEmsjoOjQ9oBY'
bot = telebot.TeleBot(token)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.add('Персонажи', '/stats')



@bot.message_handler(commands=['stats'])
def stats_link(message):
    linkB = telebot.types.InlineKeyboardMarkup()
    link = telebot.types.InlineKeyboardButton(text='Сайт со статистикой', url='vk.com/feed')
    linkB.add(link)
    back = telebot.types.ReplyKeyboardMarkup(True)
    back.add('Персонажи')
    bot.send_message(message.chat.id, 'Перейди на сайт со статистикой', reply_markup=linkB)
    bot.send_message(message.chat.id, 'Вернуться к персонажам', reply_markup=back)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доброе утро, еще один прекрасный день в офисе :)', reply_markup=keyboard1)


keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.add('Michael', 'Dwight', 'Jim', 'Pam', 'Andy', 'Kevin', 'Angela', 'Oscar', 'Erin', 'Ryan')


Michael_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Michael_keyboard.add('/MichaelFW', '/MichaelFP', '/MichaelInt',  'Персонажи')

Dwight_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Dwight_keyboard.add('/DwightFW', '/DwightFP', '/DwightInt', 'Персонажи')

Jim_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Jim_keyboard.add('/JimFW', '/JimFP', '/JimInt', 'Персонажи')

Pam_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Pam_keyboard.add('/PamFW', '/PamFP', '/PamInt', 'Персонажи')

Andy_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Andy_keyboard.add('/AndyFW', '/AndyFP', '/AndyInt', 'Персонажи')

Kevin_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Kevin_keyboard.add('/KevinFW', '/KevinFP', '/KevinInt', 'Персонажи')

Angela_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Angela_keyboard.add('/AngelaFW', '/AngelaFP', '/AngelaInt', 'Персонажи')

Oscar_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Oscar_keyboard.add('/OscarFW', '/OscarFP', 'OscarInt', 'Персонажи')

Erin_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Erin_keyboard.add('/ErinFW', '/ErinFP', '/ErinInt', 'Персонажи')

Ryan_keyboard = telebot.types.ReplyKeyboardMarkup(True)
Ryan_keyboard.add('/RyanFW', '/RyanFP', '/RyanInt', 'Персонажи')


@bot.message_handler(commands=['MichaelFW', 'MichaelFP', 'MichaelInt'])
def send_text(message):
    if message.text == '/MichaelFW':
        clean = []
        c = cleaning(clean, michael, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/MichaelFP':
        bot.send_message(message.chat.id, len(michael))
    elif message.text == '/MichaelInt':
        for o in character_get('Michael').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['DwightFW', 'DwightFP', 'DwightInt'])
def send_text(message):
    if message.text == '/DwightFW':
        clean = []
        c = cleaning(clean, dwight, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/DwightFP':
        bot.send_message(message.chat.id, len(dwight))
    elif message.text == '/DwightInt':
        for o in character_get('Dwight').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['JimFW', 'JimFP', 'JimInt'])
def send_text(message):
    if message.text == '/JimFW':
        clean = []
        c = cleaning(clean, jim, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/JimFP':
        bot.send_message(message.chat.id, len(jim))
    elif message.text == '/JimInt':
        for o in character_get('Jim').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['PamFW', 'PamFP', 'PamInt'])
def send_text(message):
    if message.text == '/PamFW':
        clean = []
        c = cleaning(clean, pam, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/PamFP':
        bot.send_message(message.chat.id, len(pam))
    elif message.text == '/PamInt':
        for o in character_get('Pam').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['AndyFW', 'AndyFP', 'AndyInt'])
def send_text(message):
    if message.text == '/AndyFW':
        clean = []
        c = cleaning(clean, andy, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/AndyFP':
        bot.send_message(message.chat.id, len(andy))
    elif message.text == '/AndyInt':
        for o in character_get('Andy').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['KevinFW', 'KevinFP', 'KevinInt'])
def send_text(message):
    if message.text == '/KevinFW':
        clean = []
        c = cleaning(clean, kevin, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/KevinFP':
        bot.send_message(message.chat.id, len(kevin))
    elif message.text == '/KevinInt':
        for o in character_get('Kevin').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['AngelaFW', 'AngelaFP', 'AngelaInt'])
def send_text(message):
    if message.text == '/AngelaFW':
        clean = []
        c = cleaning(clean, angela, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/AngelaFP':
        bot.send_message(message.chat.id, len(angela))
    elif message.text == '/AngelaInt':
        for o in character_get('Angela').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['OscarFW', 'OscarFP', 'OscarInt'])
def send_text(message):
    if message.text == '/OscarFW':
        clean = []
        c = cleaning(clean, oscar, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/OscarFP':
        bot.send_message(message.chat.id, len(oscar))
    elif message.text == '/OscarInt':
        for o in character_get('Oscar').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['ErinFW', 'ErinFP', 'ErinInt'])
def send_text(message):
    if message.text == '/ErinFW':
        clean = []
        c = cleaning(clean, erin, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/ErinFP':
        bot.send_message(message.chat.id, len(erin))
    elif message.text == '/ErinInt':
        for o in character_get('Erin').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(commands=['RyanFW', 'RyanFP', 'RyanInt'])
def send_text(message):
    if message.text == '/RyanFW':
        clean = []
        c = cleaning(clean, ryan, stop)
        for l in c:
            bot.send_message(message.chat.id, l)
    elif message.text == '/RyanFP':
        bot.send_message(message.chat.id, len(ryan))
    elif message.text == '/RyanInt':
        for o in character_get('Ryan').items():
            for n in o:
                bot.send_message(message.chat.id, n)


@bot.message_handler(content_types=['text'])
def send_text(message):
    hi_there = 'Hello, I`m '
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Добрый день, коллега')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До завтра')
    elif message.text.lower() == 'персонажи':
        bot.send_message(message.chat.id, 'Вот наш коллектив, выбирай кто интересен', reply_markup=keyboard2)
    elif message.text == 'Michael':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Michael_keyboard)
    elif message.text == 'Dwight':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Dwight_keyboard)
    elif message.text == 'Jim':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Jim_keyboard)
    elif message.text == 'Pam':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Pam_keyboard)
    elif message.text == 'Andy':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Andy_keyboard)
    elif message.text == 'Kevin':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Kevin_keyboard)
    elif message.text == 'Angela':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Angela_keyboard)
    elif message.text == 'Oscar':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Oscar_keyboard)
    elif message.text == 'Erin':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Erin_keyboard)
    elif message.text == 'Ryan':
        hi_there += message.text
        bot.send_message(message.chat.id, hi_there, reply_markup=Ryan_keyboard)


@bot.message_handler(commands=['MichaelFPh'])
def send_text(message):
    bot.send_message(message.chat.id, 'Beer is my life')


bot.polling()

