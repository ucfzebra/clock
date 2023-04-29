import requests
import os
import sys
import optparse
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import json

#Variable declaration section
ScrollSleep   = 0.025
HatHeight = 32
HatWidth  = 64
headers= {'Content-Type':'application/x-www-form-urlencoded'}
api_key = 'fc4e00520836cb1de3b13e1140031fd1'
# payload = dict(lat=25.54, lon=-81.84, units="imperial", appid="fc4e00520836cb1de3b13e1140031fd1")
payload={ 'lat':25.54, 'lon':-81.884, 'units':'imperial', 'appid':'{api_key}'}
r = requests.post('https://api.openweathermap.org/data/2.5/weather?appid=fc4e00520836cb1de3b13e1140031fd1&lat=25.54&lon=-81.84&units=imperial')
# = requests.post('https://api.openweathermap.org/data/2.5/weather', data=dict({'lat':25.54, \
        #    'lon':-81.884, 'units':'imperial', 'appid':b"fc4e00520836cb1de3b13e1140031fd1"}))

print(r.text)
weather = json.loads(r.text)
weather_desc = (weather['weather'][0]['description'])
humidity =  (weather['main']['humidity'])
temp =  (weather['main']['temp'])
print ('%3.1f℉'% temp)