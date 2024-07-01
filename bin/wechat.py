import subprocess
import os

def uninstall_wechat():
    uninstall_exe_path = r'C:\Program Files\Tencent\WeChat\Uninstall.exe'

    # Check if the uninstall executable exists
    if not os.path.exists(uninstall_exe_path):
        print(f"Error: Uninstall executable not found at {uninstall_exe_path}")
        return

    # Use subprocess to run the uninstall executable
    try:
        subprocess.run([uninstall_exe_path, '/S'], check=True)
        print("WeChat uninstallation process completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to uninstall WeChat. {e}")

if __name__ == "__main__":
    print("Starting WeChat uninstallation...")
    uninstall_wechat()
