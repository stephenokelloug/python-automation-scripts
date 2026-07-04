import os
import pandas as pd

class ExcelLoader:
    def __init__(self, file_name: str):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.file_path = os.path.join(project_root, "data", file_name)

    def load_users(self):
        ext = os.path.splitext(self.file_path)[1].lower()
        if ext == ".csv":
            df = pd.read_csv(self.file_path)
        else:
            df = pd.read_excel(self.file_path, engine="openpyxl")
        return df.to_dict(orient="records")

    def save_new_version(self, users: list[dict], suffix: str = "_updated"):
        df = pd.DataFrame(users)
        base, ext = os.path.splitext(self.file_path)
        new_file = f"{base}{suffix}{ext}"
        if ext == ".csv":
            df.to_csv(new_file, index=False)
        else:
            df.to_excel(new_file, index=False, engine="openpyxl")
        return new_file
