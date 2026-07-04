from core.ego_sms_gateway import EgoSmsGateway
from mikrotik.core.mikrotik_client import MikroTikClient

class UserManager:
    def __init__(self):
        self.sms = EgoSmsGateway()
        self.mikrotik = MikroTikClient()

    def sync_user(self, user: dict):
        username = user["Username"]
        password = user["Password"]
        profile = user["Profile"]
        comment = user["Comments"]
        phone = user["Phone"]

        # Always create a new user
        success, output = self.mikrotik.create_user(username, password, profile, comment)
        action = "created"

        print(f"[MikroTik] {username}: {action} → {output}")

        # Send SMS notification
        message = (
            f"Anume WiFi - Hello {comment}, your account has been {action}. "
            f"Access Number: {username}, Password: {password}. "
            f"Please do not share your account. "
            f"If you cannot login, report to the IT Office for account activation."
        )
        # sms_result = self.sms.send_sms(phone, message)
        # print(f"[SMS] {username}: {sms_result['status']}")

    def change_password(self, user: dict):
        username = user["Username"]
        password = user["Password"]
        comment = user["Comments"]
        phone = user["Phone"]

        success, output = self.mikrotik.update_password(username, password)
        print(f"[MikroTik] {username}: password updated → {output}")

        message = (
            f"Hello {comment}, your hotspot password has been updated. "
            f"New Password: {password}. "
            f"If you cannot login, report to the IT Office for account activation."
        )
        sms_result = self.sms.send_sms(phone, message)
        print(f"[SMS] {username}: {sms_result['status']}")
