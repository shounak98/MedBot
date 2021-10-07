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


#api_key = os.getenv('api_key')
bot = telebot.TeleBot('2028323189:AAEMpqqC1xMHUXCHjg4H57OxHTsiXtJql1c')             #MEDBOT Apikey

@bot.message_handler(commands=["Meds"])
def meds(update):

    bot.reply_to('Hello')

#bot.polling(1)

def medic(update: Update, context: CallbackContext) -> None:
    mornDataset = pd.read_csv("morningMed.csv")
    nightDataset = pd.read_csv("nightMed.csv")
    if((time > (7)) and (time < (12))):
        update.message.reply_text('Morning')
        

    elif(( time > (12)) and (time < (16)) ):
        
        a_row=mornDataset.sample()
        index=str(int(a_row.values[0]))
        name=str(a_row['Name of Medicine'].values[0])
        b4_B=str(a_row['Before Breakfast'].values[0])
        aft_B=str(a_row['After Breakfast'].values[0])
        for Index in mornDataset.iterrows():
            update.message.reply_text('Afternoon')
            update.message.reply_text('Hello'+ index + '\t\t'+ name + '\t\t'+ b4_B + '\t\t' + aft_B + '\t\t' , parse_mode='HTML')


    elif(( time > (18)) and (time < (22))):
        update.message.reply_text('Night')

updater = Updater('api_key')
updater.dispatcher.add_handler(CommandHandler('medic', medic))   
updater.start_polling()
updater.idle()



