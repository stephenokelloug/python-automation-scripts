import os
import paramiko
from dotenv import load_dotenv

load_dotenv()

class MikroTikClient:
    def __init__(self):
        self.host = os.getenv("MIKROTIK_HOST")
        self.user = os.getenv("MIKROTIK_USER")
        self.password = os.getenv("MIKROTIK_PASS")

    def run_cmd(self, cmd: str):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #ssh.connect(self.host, username=self.user, password=self.password)
            ssh.connect(
                self.host,
                port=22,
                username=self.user,
                password=self.password,
                look_for_keys=False,
                allow_agent=False,
                timeout=10
            )

            stdin, stdout, stderr = ssh.exec_command(cmd)
            output = stdout.read().decode().strip() or stderr.read().decode().strip()
            ssh.close()
            return True, output
        except Exception as e:
            return False, str(e)

    def create_user(self, username: str, password: str, profile: str, comment: str):
        cmd = f'/ip hotspot user add name={username} password={password} profile="{profile}" comment="{comment}" disabled=no'
        return self.run_cmd(cmd)

    def update_password(self, username: str, password: str):
        cmd = f'/ip hotspot user set [find name={username}] password={password}'
        return self.run_cmd(cmd)
