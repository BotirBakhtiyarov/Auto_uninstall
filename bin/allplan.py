import subprocess
import shutil
import os

def uninstall_autocad():
    # PowerShell script to uninstall AutoCAD
    powershell_script = '''
    $application = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "*allplan*" }

    if ($application -ne $null) {
        $application.Uninstall()
    } else {
        Write-Host "AllPlan is not installed."
    }
    '''

    # Execute PowerShell script
    result = subprocess.run(['powershell', '-Command', powershell_script], capture_output=True, text=True)

    # Print PowerShell output
    print("=== PowerShell Script Output ===")
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

    # After uninstallation, delete specific directories if they exist
if __name__ == "__main__":
    print("Starting AllPlan uninstallation...")
    uninstall_autocad()
    print("AllPlan uninstallation process completed.")
