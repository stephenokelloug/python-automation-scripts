import os
from dotenv import load_dotenv
from core.ego_sms_gateway import EgoSmsGateway

# Load environment variables from .env
load_dotenv()

if __name__ == "__main__":
    # Create gateway instance
    sms = EgoSmsGateway()

    # Ask for test input
    number = input("Enter recipient number (e.g. 2567xxxxxxx): ")
    message = input("Enter test message: ")

    # Send SMS
    result = sms.send_sms(number, message)

    print("=== SMS Test Result ===")
    print(f"Status   : {result['status']}")
    print(f"HTTP Code: {result['httpCode']}")
    print(f"Response : {result['body']}")
