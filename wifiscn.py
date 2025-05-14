import subprocess
import re

def scan_wifi(interface="wlan0"):
    try:
        # Run the iwlist scan command
        result = subprocess.check_output(["sudo", "iwlist", interface, "scanning"], stderr=subprocess.STDOUT)
        result = result.decode('utf-8')

        # Parse output
        cells = result.split("Cell ")
        wifi_list = []

        for cell in cells[1:]:
            ssid = re.search(r'ESSID:"(.+?)"', cell)
            quality = re.search(r"Quality=(\d+)/(\d+)", cell)
            signal_level = re.search(r"Signal level=(-?\d+) dBm", cell)
            mac = re.search(r"Address: ([\da-fA-F:]+)", cell)

            wifi_info = {
                "SSID": ssid.group(1) if ssid else "Hidden",
                "Quality": f"{quality.group(1)}/{quality.group(2)}" if quality else "N/A",
                "Signal": f"{signal_level.group(1)} dBm" if signal_level else "N/A",
                "MAC": mac.group(1) if mac else "N/A"
            }

            wifi_list.append(wifi_info)

        return wifi_list

    except subprocess.CalledProcessError as e:
        print("Error scanning for WiFi networks:", e.output.decode())
        return []

# Example usage
if __name__ == "__main__":
    networks = scan_wifi("wlan0")  # Replace wlan0 with your WiFi interface name
    for i, net in enumerate(networks, start=1):
        print(f"{i}. SSID: {net['SSID']}, Signal: {net['Signal']}, Quality: {net['Quality']}, MAC: {net['MAC']}")
