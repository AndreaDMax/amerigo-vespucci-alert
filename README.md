# 🛳️ Tour Vespucci Alert

📘 **Need this in English?** [Click here for the English version](README_EN.md)

Un bot Python che **monitora le modifiche alle pagine del sito [tourvespucci.it](https://tourvespucci.it)** e invia notifiche **Telegram** ogni volta che qualcosa cambia!  
Perfetto per non perdersi l'apertura delle prenotazioni delle tappe del Vespucci 🚢

---

## ⚙️ Funzionalità

- 🔄 Controllo continuo delle pagine specifiche di una tappa
- 🧠 Intelligente: ignora header, footer, script e stili
- 🔔 Notifiche Telegram in tempo reale
- 👤 Header realistici con user agent casuali per evitare blocchi
- 🕒 Delay casuale per comportarsi come un vero utente

---

## 📦 Requisiti

- Python 3.7+
- Una bot Telegram attivo
- Il tuo Chat ID

---

## 🛠️ Installazione

1. **Clona il repository**
   ```bash
   git clone https://github.com/AndreaDMax/amerigo-vespucci-alert.git
   cd amerigo-vespucci-alert
   ```

2. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura il bot**

   Apri il file `.py` e modifica queste variabili all'inizio:
   ```python
   TELEGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'
   CHAT_ID = 'YOUR_CHAT_ID'
   ```

4. **Imposta la tappa da monitorare**
   ```python
   TAPPA = 'taranto'            # es. venezia
   GIORNO_INIZIO = '16'
   GIORNO_FINE = '22'
   MESE_ARRIVO = 'aprile'       # scritto in lettere
   ANNO_ARRIVO = '2025'
   ```

---

## ▶️ Avvio

Avvia lo script con:
```bash
python alert.py
```

Riceverai subito una notifica su Telegram:
```
⚠️ Bot avviato!
```

---

## 📤 Notifiche Telegram

Riceverai messaggi come:
```
⚠️ La pagina è cambiata!
🔗 https://tourvespucci.it/taranto-16-22-aprile-2025/
```

E in caso di errore:
```
❗ Errore su:
https://tourvespucci.it/sali-a-bordo/
Errore rete: ...
```

---

## 🤖 Come ottenere il TOKEN e CHAT_ID

1. Crea un bot tramite [@BotFather](https://t.me/BotFather)
2. Ottieni il token (es. `123456:ABC-DEF...`)
3. Scrivi al tuo bot e visita [https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates](https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates) per recuperare il `chat_id`

---

## 🧪 Consigli

- Evita controlli troppo frequenti: rischi un blocco IP
- Puoi salvare un log locale per avere uno storico (opzionale)

---

## 📄 Licenza

MIT © [AndreaDMax]
