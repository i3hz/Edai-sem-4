import requests

ESP_IP = "http://192.168.0.167"  
def activate_buzzer():
    response = requests.get(f"{ESP_IP}/buzzer")
    print(response.text)
for _ in range(5):
    activate_buzzer()
