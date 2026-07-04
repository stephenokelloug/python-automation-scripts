import os
import requests
from dotenv import load_dotenv

load_dotenv()

class EgoSmsGateway:
    def __init__(self):
        self.base_url = os.getenv("EGOSMS_URL")
        self.username = os.getenv("EGOSMS_USERNAME")
        self.password = os.getenv("EGOSMS_PASSWORD")
        self.sender = os.getenv("EGOSMS_SENDERID")

    def send_sms(self, number: str, message: str, priority: int = 0) -> dict:
        for attempt in range(3):  # retry up to 3 times
            try:
                response = requests.get(self.base_url, params={
                    "number": number,
                    "message": message,
                    "username": self.username,
                    "password": self.password,
                    "sender": self.sender,
                    "priority": priority
                }, timeout=10)

                return {
                    "status": "success" if response.ok else "error",
                    "body": response.text,
                    "httpCode": response.status_code
                }
            except requests.exceptions.ConnectionError as e:
                print(f"[SMS] Connection error: {e}, retrying...")
                time.sleep(2)  # wait before retry
        return {"status": "error", "body": "Connection failed after retries", "httpCode": 0}

