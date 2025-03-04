import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # Run your main script here
    import subprocess

    def is_wifi_on():
        result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
        return "Enabled" in result.stdout and "WiFi" in result.stdout

    def turn_on_wifi():
        subprocess.run(["netsh", "interface", "set", "interface", "WiFi", "admin=enabled"])

    if __name__ == "__main__":
        turn_on_wifi()
else:
    # Re-run the script with administrative privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



