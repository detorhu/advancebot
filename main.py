import telebot
from flask import Flask, request
from threading import Thread

# --- Telegram Bot Setup ---
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# --- Flask Setup ---
app = Flask(__name__)

# --- Store messages globally ---
messages = []

# --- Function to send message to Telegram Bot ---
def send_message_to_bot(message):
    bot.send_message(chat_id='YOUR_CHAT_ID', text=message)

# --- Handle website form submission ---
@app.route('/send_message', methods=['POST'])
def handle_message():
    # Get message from website form
    user_message = request.form.get('message')
    
    # Send message to Telegram Bot
    send_message_to_bot(user_message)
    
    return "Message sent to bot!"

# --- Flask Keep Alive ---
def run_flask():
    app.run(host='0.0.0.0', port=5000)

# --- Start Flask in a thread to keep it running ---
def start_flask():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()

# --- Start Flask server for receiving messages ---
start_flask()

# --- Telegram Bot's /start Command ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Your messages from the website will show here!")

# --- Polling to keep bot running ---
bot.polling()
