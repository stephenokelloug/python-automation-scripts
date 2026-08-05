from core.ego_sms_gateway import EgoSmsGateway
from mikrotik.core.mikrotik_client import MikroTikClient
from core.password_generator import PasswordGenerator

def main():

    pwd = PasswordGenerator()

    # Ask for details
    comment = input("Enter student name/comment: ").strip()
    access_number = input("Enter access number (username): ").strip()
    password = input("Enter password (leave blank to uto generate'): ").strip() or pwd.generate(4)
    phone_number = input("Enter phone number: ").strip()
    profile = input("Enter hotspot profile (leave blank for 'default'): ").strip() or "Set20"

    # Create user on MikroTik
    mt = MikroTikClient()
    success, output = mt.create_user(access_number, password, profile, comment)
    action_status = "created" if success else "failed"

    print(f"[MikroTik] {action_status}: {output}")

    # Prepare SMS message
    #message = (
    #    f"Anume WiFi - Hello {comment}, your account has been {action_status}. "
    #    f"Access Number: {access_number}, Password: {password}. "
    #    f"Please do not share your account. If you cannot login, report to the IT Office for account activation."
    #)

    message = (
        f"Anume WiFi: Hello {comment}, your account {action_status}. "
        f"User: {access_number}, Pass: {password}. "
        f"Do not share. For issues, visit IT Office."
    )

    # Send SMS
    sms = EgoSmsGateway()
    sms_result = sms.send_sms(phone_number, message)
    print(f"[SMS] {sms_result}")

if __name__ == "__main__":
    main()
