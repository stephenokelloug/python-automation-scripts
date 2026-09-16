import os
import time
from dotenv import load_dotenv
from mikrotik.core.mikrotik_client import MikroTikClient

load_dotenv()

# Load gateways from .env
GATEWAYS = os.getenv("WAN_GATEWAYS", "").split(",")
TEST_HOST = "8.8.8.8"

def main():
    mt = MikroTikClient()

    # Step 1: Check current WAN connectivity
    success, output = mt.check_connectivity(TEST_HOST)
    if success:
        print("[INFO] Current WAN is healthy, no switch needed.")
        return

    print("[WARN] Current WAN failed, trying backups...")

    # Step 2: Loop through gateways
    for gw in GATEWAYS:
        gw = gw.strip()
        if not gw:
            continue
        print(f"[INFO] Switching to gateway {gw}...")
        mt.run_cmd(f"/ip route set [find dst-address=0.0.0.0/0] gateway={gw}")
        time.sleep(10)

        # Step 3: Test connectivity again
        success, output = mt.check_connectivity(TEST_HOST)
        if success:
            print(f"[SUCCESS] Switched to gateway {gw}")
            return

    print("[ERROR] No gateways worked. Will retry later.")

if __name__ == "__main__":
    main()
