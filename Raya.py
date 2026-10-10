# ═══════════════════════════════════════════════════════════
# TOKENS & KEYS - REFACTORED FOR RIYA X CPM1 BOT
# ═══════════════════════════════════════════════════════════
BOT_TOKEN = "8796954967:AAFUyVS7X-2iLf_vwFrQYM0trsc2RxImBJE"
bot = telebot.TeleBot(BOT_TOKEN)

OWNER_ID = 8296992233  # Assigned Telegram User ID

ADMIN_IDS = [8296992233]  # Assigned Telegram User ID List
ALLOWED_KEYS = ["Riya8055"]  # Primary authorization key set to Riya8055

CHANNEL_ID = "@your_channel_username"
CHANNEL_LINK = "https://t.me/your_channel_username"

# ═══════════════════════════════════════════════════════════
# FLASK WEB SERVER METADATA REFACTORED
# ═══════════════════════════════════════════════════════════
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "bot": "Riya X CPM1 bot",
        "version": "1.0.0",
        "uptime": "running"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

def get_text(chat_id, key, **kwargs):
    texts = {
        "welcome": (
            "☠️ **RIYA X CPM1 BOT** ☠️\n"
            "🔥 **ADVANCED AUTOMATION TOOL** 🔥\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            "🔐 Welcome!\n"
            "📌 Choose activation method:\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            "🔑 Normal Key\n"
            "⏰ Time Key\n"
            "🎁 Free Trial (10 min)\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            "👤 Admin: Riya X CPM1 Support"
        ),
        "cpm1_section": (
            "☠️☠️☠️ **RIYA X CPM1 BOT - CPM1 MENU** ☠️☠️☠️\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            "📱 **Activation Menu**"
        ),
        "cpm2_section": (
            "☠️☠️☠️ **RIYA X CPM1 BOT - CPM2 MENU** ☠️☠️☠️\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            "🎮 **Activation Menu**"
        ),
        "back": "🔙 Back",
        "not_logged": "❌ **Not logged in!** Use /start",
        "not_logged_short": "❌ **Not logged in!**",
        "login_cpm_success": "✅ **Logged in to CPM1!**",
        "login_cpm_fail": "❌ **Login failed!**",
        "login_cpm2_success": "✅ **Logged in to CPM2!**",
        "login_cpm2_fail": "❌ **Login failed!**",
        "key_success": "✅ **Activated with Riya8055 Key!**",
        "wrong_key": "❌ Invalid key!",
        "key_title": "🔑 **Enter activation key:**",
        "enter_pass": "☠️ **Enter password:**",
        "email_prompt": "☠️ **Selected {section}**\n━━━━━━━━━━━━━━━━━━━━━\n📧 **Enter email:**",
        "king_email_prompt": "👑 **Enter CPM1 email:**",
        "king_pass_prompt": "☠️ **Enter CPM1 password:**",
        "king_rank_success": "✅ {msg}",
        "king_rank_fail": "❌ {msg}",
        "money_added": "✅ **Added {amount}!**",
        "money_fail": "❌ **Failed!**",
        "id_changed": "✅ **ID changed to `{new_id}`**",
        "id_fail": "❌ **Failed!**",
        "email_changed": "✅ **Email changed to `{new_email}`**",
        "email_fail": "❌ **Failed!**",
        "pass_changed": "✅ **Password changed!**",
        "pass_fail": "❌ **Failed!**",
        "clone_success": "✅ **Clone done!**\n🚗 {success}/{total} cars",
        "clone_fail": "❌ **Clone failed!**\n💀 {error}",
        "unlock_cars_done": "✅ **Cars unlocked!**",
        "unlock_cars_fail": "❌ **Failed to unlock cars!**",
        "unlock_cars_auto_done": "✅ **Injected {success}/270 cars!**",
        "logout": "🚪 **Logged out**",
        "free_trial_first": "🎁 **Free trial activated!** ✅ 10 minutes",
        "trial_activating": "🎁 Activating...",
        "start_normal_key": "🔑 Normal Key",
        "start_time_key": "⏰ Time Key",
        "start_free_trial": "🎁 Free Trial (10 min)",
        "main_cpm1": "📱 CPM1",
        "main_cpm2": "🎮 CPM2",
        "admin_panel": "👑 **Riya X CPM1 Bot - Admin Panel**",
        "not_admin": "❌ **Admins only!**",
        "refresh_account": "🔄 Refresh Info",
        "unlock_cars_auto_confirm": (
            "🤖 **Auto Injection (1-270)**\n"
            "⚡ Ready to inject 270 cars.\n"
            "📌 Confirm?"
        ),
        "unlock_cars_auto_yes": "✅ Confirm",
        "unlock_cars_auto_cancel": "❌ Cancel",
        "unlock_cars_manual_prompt": "🖐️ **Manual Injection**\n📌 Enter Car ID:",
        "unlock_cars_prompt": (
            "🚗 **Unlock CPM1 Cars**\n"
            "━━━━━━━━━━━━━━━━━━━━━\n"
            "📧 Email: `{email}`\n\n"
            "📌 Choose injection type:"
        ),
        "time_key_title": "⏰ **Enter Time Key:**"
    }
    
    text = texts.get(key, f"Missing text: {key}")
    if kwargs:
        try:
            text = text.format(**kwargs)
        except Exception:
            pass
    return text


    # ═══════════════════════════════════════════════════════════
# BOT STARTUP AND WEBHOOK PURGING ENGINE
# ════════════════════════════════[span_1](start_span)[span_1](end_span)═══════════════════════════
print("="*60, flush=True)
print("☠️☠️☠️ RIYA X CPM1 BOT - INITIALIZATION ☠️☠️☠️", flush=True)
print("="*60, flush=True)

# Purge pre-existing webhooks to allow long polling
for attempt in range(3):
    try:
    [span_2](start_span)[span_2](end_span)    bot.delete_webhook(drop_pending_updates=True)
        print("🧹 Webhook cleared successfully", flush=True)
        break
    except Exception as e:
        print(f"⚠️ Webhook clear attempt {attempt+1} failed: {e}", flush=True)
        time.sleep(2)

def run_bot():
    while True:
        try:
            print("🔄 Starting Telegram polling loop...", flush=True)
            bot.polling(
                none_stop=True,
                timeout=20,
                long_polling_timeout=20,
                skip_pending=True
            )
        except Exception as e:
            print(f"❌ Polling loop error encountered: {e}", flush=True)
            time.sleep(5)

if __name__ == "__main__":
    run_bot()

import [span_29](start_span)[span_29](end_span)[span_39](start_span)[span_39](end_span)os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8796954967:AAFUyVS7X-2iLf_vwFrQYM0trsc2RxImBJE")
OWNER_ID = int(os.environ.get("OWNER_ID", "8296992233"))
ADMIN_IDS = [int(x) for x in os.environ.get("ADMIN_IDS", "8296992233").split(",")]
ALLOWED_KEYS = os.environ.get("ALLOWED_KEYS", "Riya8055").split(",")



