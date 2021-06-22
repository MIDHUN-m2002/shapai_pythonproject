import requests
from datetime import datetime
from os import write

api_key='d0c7d0b8263bf2443a94c2c9fc2fc73a'
location =input('ENTER THE CITY NAME :')
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key#this link from the openweather api .we add location and api key variable to it
api_link = requests.get(complete_api_link)# allows to get a https request inthe get form
api_data = api_link.json()#data is comming inthe form json refer openweather website https://openweathermap.org/current


#create variables to store and display data,we only take informations that we need
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")


print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

print('"CHECK THE WEATHERNOW FILE FOR .txt FORMAT"')
temp=str(temp_city)
weatherdesc=str(weather_desc)
humidity=str(hmdt)
speed=str(wind_spd)
with open('weathernow.txt','w') as f:
    f.write('-------------------------------------------------------------')
    f.write('\n')
    f.write('Weather Stats for - {}  || {}'.format(location.upper(), date_time))
    f.write('\n')
    f.write('-------------------------------------------------------------')
    f.write('\n')
    f.write('Current temperature is:')
    f.write(temp) 
    f.write('\t')
    f.write('deg C')
    f.write('\n')
    f.write('Current weather desc  :')
    f.write(weatherdesc)
    f.write('\n')
    f.write('Current Humidity      :')
    f.write(humidity)
    f.write('\n')
    f.write('Current wind speed    :')
    f.write(speed)
    f.write('\n')

    

