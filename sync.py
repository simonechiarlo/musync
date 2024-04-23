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
        
def send_file(file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    files = {
        "chat_id": (None, CHAT_ID),
        "document": open(file_path, "rb")
    }
    res = requests.post(url, files=files).json()
    if res.get("ok"):
        print("File Sent")
    else:
        print("File Failed")
        
def sync():
    os.system(YOUTUBE_DLP_COMMAND + "| tee -a /app/log.txt")
    
if __name__ == "__main__":
    send_status("Sync ⏳")
    sync()
    send_status("Sync ✅")
    send_file("/app/log.txt")