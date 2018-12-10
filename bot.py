from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

from telegram.ext import (Updater, CommandHandler, 
MessageHandler, RegexHandler, Filters,ConversationHandler)
# extract needed modules from libraries 

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                    
                    
                    
logger = logging.getLogger(__name__)
# that is custom to enable logging,
# put every time when you start coding

NAME, PHOTO, LOCATION, BIO = range(4)
# that is what the bot will be asking


def start(bot,update):
    reply_keyboard = [['Anna'],['Not gonna say']]

    update.message.reply_text(
        'Hi, babe. My name is Jack. And I want to get aquainted with you. '
        'Send /cancel to get me off.\n\n'
        'Whatcha name?',
         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return NAME

def name(bot,update):
    user = update.message.from_user
    logger.info("Name of %s: %s", user.first_name, update.message.text)
    update.message.reply_text("Okay. Are you able to send me a pic of yourself, "
                              "so I can know what you look like, or send /skip if you don't want to.",
                              reply_markup=ReplyKeyboardRemove())
    return PHOTO

def photo(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s",user.first_name, 'user_photo. jpg')
    update.message.reply_text("Wow, you're so beautiful :) "
                              "Where do you live? Send me your locaton or send /skip"
                              "if you don't want to")
    return LOCATION

def skip_photo(bot,update):
    user = update.message.from_user
    logger.info('User %s did not send a photo', user.first_name)
    update.message.reply_text("That's a pity, but I bet you look gorgeous, babe. "
                               "Send me your location or send /skip")
    return LOCATION

def location(bot, update):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Location of %s: %f / %f", user.first_name, user_location.latitude,
                user_location.longitude)
    update.message.reply_text("I'm your neigbour! Send me a link of your VK page")

    return BIO

def skip_location(bot,update):
    user = update.message.from_user
    logger.info('User %s did not send a location', user.first_name)
    update.message.reply_text("You seem a bit paranoid! "
                              "At least, tell me something about yourself")
    return BIO
    

def bio(bot, update):
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text("Nice, I will text you later ;)")

    return ConversationHandler.END


def cancel(bot,update):
    user = update.message.from_user
    logger.info("User %s refused the conversation", user.first_name)
    update.message.reply_text("Oh, so... bye, then. I hope we could talk later on",
    reply_markup = ReplyKeyboardRemove())

    return ConversationHandler.END

def error(bot, update, error):
        logger.warning('Update "%s" caused error "%s"', update, error)

def main():
         
        updater = Updater('742208292:AAFFKAbqAhqMYqkST1kY3Onulz966zBI3nw')

        dp = updater.dispatcher

    # Add conversation handler with the states NAME, PHOTO, LOCATION and BIO
        conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            NAME: [RegexHandler('^(Anna|Not gonna say)$', name)],

            PHOTO: [MessageHandler(Filters.photo, photo),
                    CommandHandler('skip', skip_photo)],

            LOCATION: [MessageHandler(Filters.location, location),
                       CommandHandler('skip', skip_location)],

            BIO: [MessageHandler(Filters.text, bio)]
        },

        fallbacks=[CommandHandler('cancel', cancel)])
        
        dp.add_handler(conv_handler)

    # log all errors

        dp.add_error_handler(error)

    # Start the Bot
        updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()



if __name__ == '__main__':
    main()