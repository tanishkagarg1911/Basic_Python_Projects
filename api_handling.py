
import requests

url ="https://api.waqi.info/feed/@12430/?token=4bbc3e169a7c4f16076eafd981ade784da39ff93"

response=requests.get(url)
#print(response.status_code)   # sanity check
#print(response.text)

data=response.json()
#print(type(data))
#print(data)

aqi=data['data']['aqi']
print("AQI:", aqi)
city=data['data']['city']['name']
print("City:", city)

dominant_pollutant=data['data']['dominentpol']
print("Dominant Pollutant:", dominant_pollutant)

iaqi=data['data']['iaqi']

pm25 = iaqi["pm25"]["v"]
pm10 = iaqi["pm10"]["v"]
co = iaqi["co"]["v"]

print("PM2.5:", pm25)
print("PM10:", pm10)
print("CO:", co)

def aqi_status(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

status = aqi_status(aqi)
print("Air Quality Status:", status)
