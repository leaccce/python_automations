import os
import subprocess

def is_wifi_on():
    result = subprocess.run(["netsh", "interface", "show", "interface"], capture_output=True, text=True)
    return "Enabled" in result.stdout and "WiFi" in result.stdout
        
def turn_on_wifi():
    subprocess.run(["netsh", "interface", "set", "interface", "WiFi", "admin=enabled"])

def connect_wifi(network_name):
    command = f'netsh wlan connect name="{network_name}" ssid="{network_name}"'
    os.system(command)

if __name__ == "__main__":
    if is_wifi_on()==False:
        print("Wifi is Disabled\nRun the program as admin to enable the wifi.")
        turn_on_wifi()
    else:
        print("Wi-Fi is enabled.")
    print(f"Connecting to H-VIT")
    connect_wifi("H-VIT")   
