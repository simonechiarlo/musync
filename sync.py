import sys
import requests
from dotenv import load_dotenv
import os 
load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
YOUTUBE_DLP_COMMAND = os.getenv("YOUTUBE_DLP_COMMAND")

def send_status(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    res = requests.get(url).json()
    if res.get("ok"):
        print("Message Sent")
    else:
        print("Message Failed")
        
def sync():
    os.system(YOUTUBE_DLP_COMMAND)
    
if __name__ == "__main__":
    send_status("Sync ⏳")
    sync()
    send_status("Sync ✅")