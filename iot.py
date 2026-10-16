from machine import Pin
from time import sleep
import network
import urequests
import time

LAT = "16.4322"
LON = "103.5064"

# Endpoint ของ Open-Meteo API
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true"


def connect_wifi(ssid, password):
    # Set ESP32 to Station mode (client)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to {ssid}...")
        wlan.connect(ssid, password)
        
        # Wait until the connection is established
        while not wlan.isconnected():
            time.sleep(0.5)
            print(".", end="")
            
    print("\nWi-Fi Connected!")
    # Print the IP address, subnet mask, gateway, and DNS
    print("Network config:", wlan.ifconfig())


def get_kalasin_temp():
    print("Fetching weather data from Open-Meteo...")
    temp = None
    try:
        # 1. ยิง HTTP GET Request ไปที่ API
        response = urequests.get(API_URL)
        
        # 2. ตรวจสอบสถานะการเชื่อมต่อ (200 = OK)
        if response.status_code == 200:
            # 3. แปลงข้อความตอบกลับเป็น JSON Dictionary
            data = response.json()
            
            # 4. เจาะเข้าถึง Key ที่เก็บค่าอุณหภูมิ
            temp = data["current_weather"]["temperature"]
  
        else:
            print(f"HTTP Error: {response.status_code}")
            
        # 5. ปิดการเชื่อมต่อเพื่อคืนพื้นที่ RAM ให้ ESP32 (สำคัญมาก)
        response.close()
        return temp
        
    except Exception as e:
        print("Error fetching API:", e)


wifi_name = "Sarayutgo"
password = 'qweytruio'
connect_wifi(wifi_name, password)

c = 0
while True:
    sleep(3)
    c = get_kalasin_temp()
    print(f"Celsius: {c}")


        
    
    



    