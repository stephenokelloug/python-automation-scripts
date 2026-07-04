from core.excel_loader import ExcelLoader
from mikrotik.core.hotspot_user_manager import UserManager

if __name__ == "__main__":
    loader = ExcelLoader("students_latest.xlsx")
    users = loader.load_users()
    manager = UserManager()

    for user in users:
        manager.sync_user(user)
