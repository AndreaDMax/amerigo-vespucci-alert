# 🛳️ Tour Vespucci Alert

A Python bot that **monitors changes to pages on [tourvespucci.it](https://tourvespucci.it)** and sends **Telegram notifications** whenever something changes!  
Perfect for staying up to date on the reservations of Vespucci's itinerary 🚢

---

## ⚙️ Features

- 🔄 Continuous monitoring of location-specific pages
- 🧠 Smart content filtering: skips header, footer, scripts, styles
- 🔔 Real-time Telegram alerts
- 👤 Realistic headers with random user agents to avoid detection
- 🕒 Random delay between requests to mimic human behavior

---

## 📦 Requirements

- Python 3.7+
- An active Telegram bot
- Your Telegram Chat ID

---

## 🛠️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AndreaDMax/amerigo-vespucci-alert.git
   cd amerigo-vespucci-alert
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your bot**

   Open the `.py` file and update the following variables:
   ```python
   TELEGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'
   CHAT_ID = 'YOUR_CHAT_ID'
   ```

4. **Set the location you want to monitor**
   ```python
   TAPPA = 'taranto'            # e.g. venezia
   GIORNO_INIZIO = '16'
   GIORNO_FINE = '22'
   MESE_ARRIVO = 'aprile'       # in letters
   ANNO_ARRIVO = '2025'
   ```

---

## ▶️ Running the bot

Run the script with:
```bash
python watcher.py
```

You will immediately receive a Telegram message:
```
⚠️ Bot avviato!
```

---

## 📤 Telegram Notifications

You’ll receive alerts like:
```
⚠️ La pagina è cambiata!
🔗 https://tourvespucci.it/taranto-16-22-aprile-2025/
```

Or in case of errors:
```
❗ Errore su:
https://tourvespucci.it/sali-a-bordo/
Errore rete: ...
```

---

## 🤖 How to get your TOKEN and CHAT_ID

1. Create a bot via [@BotFather](https://t.me/BotFather)
2. Copy your bot token (e.g. `123456:ABC-DEF...`)
3. Start a chat with your bot and visit [https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates](https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates) to find your `chat_id`

---

## 🧪 Tips

- Avoid checking too often to prevent getting blocked
- Optionally, log changes locally for reference

---

## 📄 License

MIT © [AndreaDMax]
