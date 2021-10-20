# -*- coding: utf-8 -*-
"""Копия блокнота "ChatBot - Day 3.ipynb"

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lfKqEmqClswr2Rn_bhNPX_Z5JeOdQpfx
"""

# pip install python - telegram - bot - -upgrade

import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import logging
# from telegram import Update, ForceReply
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# BOT_CONFIG = {
#     'intents': {
#         'hello': {
#             'examples': ['Привет!', 'Здарова', 'Хей-хей!!'],
#             'responses': ['Хай', 'Добрый вечер!', 'Здравствуйте!']
#         },
#         'bye': {
#             'examples': ['Пока', 'Увидимся!', 'Покеда'],
#             'responses': ['До свидания', 'Прощайте', 'Сайонара!']
#         }
#     }
# }

with open('D:\\BOT_CONFIG.json', encoding='utf-8') as f:
    BOT_CONFIG = json.load(f)

# with open('D:\\BOT_CONFIG.json', 'r') as f: # encoding='utf-8'
#     BOT_CONFIG = json.load(f)

# with open('D:\\BOT_CONFIG1.json', 'w') as f:
#     json.dump(BOT_CONFIG, f, ensure_ascii=False, indent=3)

"""# День 1"""

def clean(text):
    text = text.lower()
    cleaned_text = ''
    for ch in text:
        if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
            cleaned_text = cleaned_text + ch
    return cleaned_text

def get_intent(text):
    for intent in BOT_CONFIG['intents'].keys():
        for example in BOT_CONFIG['intents'][intent]['examples']:
            w1 = clean(example)
            w2 = clean(text)
            if nltk.edit_distance(w1, w2) / max(len(w1), len(w2)) < 0.4:
                return intent
    return 'интент не найден'

"""# День 2"""

X = []
y = []

for intent in BOT_CONFIG['intents'].keys():
    try:
        for example in BOT_CONFIG['intents'][intent]['examples']:
            X.append(example)
            y.append(intent)
    except:
        pass

print(len(X), len(y), len(set(y)))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print(len(X_train), len(X_test))

vectorizer = CountVectorizer(preprocessor=clean, analyzer='char', ngram_range=(2, 3))
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

print(len(vectorizer.get_feature_names_out()))

log_reg = LogisticRegression(C=0.2)
log_reg.fit(X_train_vect, y_train)
print(log_reg.score(X_train_vect, y_train))

print(log_reg.score(X_test_vect, y_test))

def get_intent_by_model(text):
    return log_reg.predict(vectorizer.transform([text]))[0]

def bot(question):
    intent = get_intent_by_model(question)
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])

question = ''
while True:
    question = input()
    if question != 'стоп':
        answer = bot(question)
        print(answer)
    else:
        break

# """# День 3"""
#
# # Enable logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
#
# logger = logging.getLogger(__name__)
#
#
# # Define a few command handlers. These usually take the two arguments update and
# # context.
# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     update.message.reply_markdown_v2(
#         fr'Hi {user.mention_markdown_v2()}\!',
#         reply_markup=ForceReply(selective=True),
#     )
#
#
# def help_command(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')
#
#
# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     question = update.message.text
#     try:
#         answer = bot(question)
#     except:
#         answer = 'Извините, что-то сломалось =('
#
#     update.message.reply_text(answer)
#
#
# def main() -> None:
#     """Start the bot."""
#     # Create the Updater and pass it your bot's token.
#     updater = Updater("1971454798:AAHLLbwzKp8hXfHLNo_KHg23c7420dsbstc")
#
#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher
#
#     # on different commands - answer in Telegram
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("help", help_command))
#
#     # on non command i.e message - echo the message on Telegram
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
#
#     # Start the Bot
#     updater.start_polling()
#
#     # Run the bot until you press Ctrl-C or the process receives SIGINT,
#     # SIGTERM or SIGABRT. This should be used most of the time, since
#     # start_polling() is non-blocking and will stop the bot gracefully.
#     updater.idle()
#
# main()