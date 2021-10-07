#import os
import datetime
import telebot
import pandas as pd
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, callbackcontext, updater

currentTime = datetime.datetime.now()
currentDay = datetime.datetime.today()
time = currentTime.hour
day = currentDay.weekday()

def medic(update: Update, context: CallbackContext) -> None:
    mornDataset = pd.read_csv("morningMed.csv")
    nightDataset = pd.read_csv("nightMed.csv")
    df = nightDataset.to_string(columns= ['Index','Name of Medicine','Before Breakfast','After Breakfast','Before Lunch','After Lunch','Before Dinner','After Dinner'])
    if((time > (12)) and (time < (17))):
        update.message.reply_text('Afternoon')
        update.message.reply_text(df)


updater = Updater('api_key')
updater.dispatcher.add_handler(CommandHandler('medic', medic))   
updater.start_polling()
updater.idle()
