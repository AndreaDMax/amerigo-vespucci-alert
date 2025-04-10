import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urlparse, urlencode, urlunparse, parse_qs

# === CONFIG ===
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'  # insert your Telegram bot token
CHAT_ID = 'YOUR_CHAT_ID'  # insert your chat ID
TAPPA = 'taranto'
GIORNO_INIZIO = '16'
GIORNO_FINE = '22'
MESE_ARRIVO = 'aprile'  # Month as string, as required in the URL
ANNO_ARRIVO = '2025'

# Ensure input is lowercase
TAPPA = TAPPA.lower()
MESE_ARRIVO = MESE_ARRIVO.lower()

URLS = [
    'https://tourvespucci.it/sali-a-bordo/',
    f'https://tourvespucci.it/eventi/visita-a-bordo-{TAPPA}/',
    f'https://tourvespucci.it/{TAPPA}-{GIORNO_INIZIO}-{GIORNO_FINE}-{MESE_ARRIVO}-{ANNO_ARRIVO}/'
]

START = True
ua = UserAgent()
previous_contents = {}  # Stores the page content to monitor changes


def build_url_with_timestamp(url):
    """Adds a timestamp to the URL to avoid caching"""
    parts = list(urlparse(url))
    query = parse_qs(parts[4])
    query['t'] = [str(int(time.time()))]  # Add current timestamp
    parts[4] = urlencode(query, doseq=True)
    return urlunparse(parts)


def get_headers():
    """Generates realistic headers"""
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0'
    }
    return headers


def notify_telegram(message):
    """Sends a Telegram message"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print(f"[!] Errore invio Telegram: {e}")


def get_page_content(url):
    """Downloads and cleans the page content using BeautifulSoup"""
    headers = get_headers()
    fresh_url = build_url_with_timestamp(url)
    try:
        response = requests.get(fresh_url, headers=headers, timeout=15)
        if response.status_code in [403, 429, 503]:
            raise Exception(f"Blocco IP o errore HTTP {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove scripts, styles, and other non-useful sections
        for tag in soup(["script", "style", "noscript", "header", "footer"]):
            tag.decompose()

        # Get only the visible content, such as the article body
        content_section = soup.find('div', class_='site-content')  # Use the correct selector for your page

        if content_section:
            clean_text = content_section.get_text()
            return clean_text.strip()
        else:
            return ""

    except requests.exceptions.RequestException as e:
        raise Exception(f"Errore rete: {e}")


# === MONITORAGGIO ===
if START:
    notify_telegram("⚠️ Bot avviato!\n")
    START = False
while True:
    for url in URLS:
        try:
            content = get_page_content(url)

            if url not in previous_contents:
                previous_contents[url] = content
                print(f"[~] Primo controllo → {url}")
            elif content != previous_contents[url]:
                print(f"[✔] Modifica rilevata su: {url}")
                notify_telegram(f"⚠️ La pagina è cambiata!\n🔗 {url}")
                previous_contents[url] = content
            else:
                print(f"[=] Nessuna variazione su: {url}")

        except Exception as e:
            print(f"[⚠] Errore su {url}:\n    {e}")
            notify_telegram(f"❗ Errore su:\n{url}\n{e}")

    delay = random.randint(30, 220)  # Vary the delay to avoid patterns
    print(f"\n⏳ Attesa {delay} secondi prima del prossimo controllo...\n")
    time.sleep(delay)
