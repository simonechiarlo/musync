import sys
import requests
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_status():
    if(len(sys.argv) < 2):
        print("Usage: python status.py <message>")
        sys.exit()

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={sys.argv[1]}"
    res = requests.get(url).json()
    if res.get("ok"):
        print("Message Sent")
    else:
        print("Message Failed")
    
if __name__ == "__main__":
    send_status()