from pyexpat.errors import messages
from types import MemberDescriptorType
from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import json
import random
import os
import pyjokes
from quoters import Quote
from pyrogram import filters
from randimage import get_random_image, show_array
import aiohttp
from json import dumps

group = ""
global_welcome_message = "WELCOME TO THE GROUP "
left_message = ""


bot = Client(
    "safe_place_bot",
    api_id = ,
    api_hash = ",
    bot_token = "",
)

#Global Vars 
GROUP = 
chat_id = 


jokes = pyjokes.get_joke # You can use this when you have to use the same thing over and over again sometimes, Like For Example, pyjokes.get_joke(language="hi", category="neutral"), pyjokes.get_joke(language="en", category="neutral"), Then Instead of writting 'pyjokes.get_joke' you use your pre-defined function 'jokes' in place of that.


#Start 
@bot.on_message(filters.command('start'))
def command_send_spam (client,message):
    bot.send_message(message.chat.id, "***I AM A BOT*** I AM NOT VERY SMART YET -- ***WELCOME***..")


#Get Random Rick And Morty Pic 
@bot.on_message(filters.command('randomrickandmorty'))
def pickrandom(bot,message):
    directory = "/pics/"
    random_image = random.choice(os.listdir(directory))
    bot.send_photo(message.chat.id, photo=open(directory + random_image,'rb'))


#Joke
@bot.on_message(filters.command(["joke"]))
async def crackjoke(_, message):
    joke = jokes(language="en", category="all")
    await message.reply_text(joke)


#Random Quote
@bot.on_message(filters.command(["quote"]))
async def quoter(_, message):
    quote = Quote.print()
    await message.reply_text(quote)
 


#@bot.on_message(filters.command('members'))
#def get_usernames(bot,message):
    #for member in bot.get_chat_members(chat_id):
        #message.reply_text(member)
        #print(type(member))
        #print (member)

#Get Chat members
@bot.on_message(filters.command('members'))
def get_usernames(bot,message):
    for member in bot.get_chat_members(chat_id):
        message.reply(member)
        print (member)



#Count Members 
@bot.on_message(filters.command('membercount'))
def get_chat_members_count(bot,message):
    count = bot.get_chat_members_count(chat_id)
    message.reply(f' There are {count} members in this chat')
    print(message)

    

# Command Help
@bot.on_message(filters.command('help') & filters.private)
def command_help (client,message):
    message.reply_text("This is the help section wagwan")


##Command ECHOBOT
#@bot.on_message(filters.text & filters.private)
#def echobot(client,message):
        #message.reply_text(f'what you saying poose?........... {message.text}')

#Welcome New Members 
@bot.on_message(filters.chat(group) & filters.new_chat_members)
def welcome_new_members(client,message):
    message.reply_text(global_welcome_message)


#Message chat member on exit 
@bot.on_message(filters.chat(group) & filters.left_chat_member)
def goodbye(client,message):
    message.reply_text(left_message)    


##
#welcome 
#@bot.on_message(filters.chat(group) & filters.new_chat_members)
#def welcome(client,message):
   # message.reply_text(WELCOME_MESSAGE)


#Send a single photo
@bot.on_message(filters.command('photo'))
def send_photo(client,message):
    bot.send_photo(message.chat.id,"https://images.squarespace-cdn.com/content/v1/5b788d28697a98e17a6d4c7a/b83f0eab-7dd6-4e9b-83a1-13139ac2a03b/rickroll+cropped.png")


#Send File Via audio ID
@bot.on_message(filters.audio & filters.private)
def audio(bot,message):
   message.reply(message.audio.file_id)

#Send Audio 
@bot.on_message(filters.command('audio'))
def audio_command(bot,message):
    bot.send_audio(message.chat.id,"CQACAgIAAxkBAAIMHmN87tu6f4c1dD7PsGqlT5Lum2vfAAITIQACo9LoS9VzOGmhp3wrHgQ")

#Bot Restricted words 
@bot.on_message(filters.text)
def delete_text(bot,message):
    word_list = ['bro', 'wtf']
    if message.text in word_list:
        message.delete(message.id)
        message.reply_text("THAT IS A RESTRICTED WORD !!!  ")


#

START_MESSAGE = "Heya, I am a simple test bot"
START_MESSAGE_BUTTONS = [
    [InlineKeyboardButton('CHANNEL', url='https://telegram.dog/wildthatcodesbot')],
    [InlineKeyboardButton('devloper', url='https://telegram.dog/wildthatcodesbot')]
]
@bot.on_message(filters.command("start"))
def start_command(client, message):
    text= START_MESSAGE
    reply_markup = InlineKeyboardMarkup (START_MESSAGE_BUTTONS)
    message.reply(
    text=text,
    reply_markup=reply_markup
    )


#@bot.on_message(filters.command('members'))
#def chat_members(client,message):
    #for message in bot.get_chat_history('safe_place_bot'):
        #message.reply_text(message)
        



print ("I am alive")
print (chat_id)
bot.run()
