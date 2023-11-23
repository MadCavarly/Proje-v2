import network
from time import sleep_ms
import ubinascii

def connect_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print("Connecting to Wi-Fi", end="")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            print(".", end="")
            sleep_ms(100)
        print(" Connected")

    else:
        print("Already connected")

    print(f"Network config: {sta_if.ifconfig()}")
    mac_addr = sta_if.config("mac")
    mac_ascii = ubinascii.hexlify(mac_addr, ":").decode()
    print(f"MAC: {mac_addr} --> {mac_ascii}")

def disconnect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.active():
        sta_if.active(False)
    if not sta_if.isconnected():
        print("Disconnected")
