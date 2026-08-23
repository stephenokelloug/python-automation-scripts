import time
from mikrotik.core.mikrotik_client import MikroTikClient

# List of gateways to try in order
GATEWAYS = ["10.21.119.209", "192.168.70.89"]

# Host to test connectivity against
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
        print(f"[INFO] Switching to gateway {gw}...")
        mt.run_cmd(f"/ip route set [find dst-address=0.0.0.0/0] gateway={gw}")
        time.sleep(10)  # wait for route to apply

        # Step 3: Test connectivity again
        success, output = mt.check_connectivity(TEST_HOST)
        if success:
            print(f"[SUCCESS] Switched to gateway {gw}")
            return

    # Step 4: If none worked
    print("[ERROR] No gateways worked. Will retry later.")

if __name__ == "__main__":
    main()
