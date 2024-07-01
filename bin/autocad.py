import subprocess
import shutil
import os

def uninstall_autocad():
    # PowerShell script to uninstall AutoCAD
    powershell_script = '''
    $application = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like "*AutoCAD*" }

    if ($application -ne $null) {
        $application.Uninstall()
    } else {
        Write-Host "AutoCAD is not installed."
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
    delete_directories()

def delete_directories():
    # List of directories to delete after uninstallation
    directories_to_delete = [
        r'C:\Program Files\Autodesk\AutoCAD 2024',
        r'C:\Program Files\Autodesk\AutoCAD Activity Insights'
    ]

    for directory in directories_to_delete:
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
                print(f"Deleted: {directory}")
            except Exception as e:
                print(f"Error deleting {directory}: {e}")

if __name__ == "__main__":
    print("Starting AutoCAD uninstallation...")
    uninstall_autocad()
    print("AutoCAD uninstallation process completed.")
