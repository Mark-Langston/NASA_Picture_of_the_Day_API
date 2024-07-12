import urllib.request
import json
import webbrowser

## Define APID
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=DEMO_KEY' ## replace DEMO_KEY with your nasa api key

## Call the webservice
apodurlobj = urllib.request.urlopen(apodurl + mykey)

## read the file-like object
apodread = apodurlobj.read()

## decode json to python data structure
decodeapod = json.loads(apodread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeapod)

## use browser to open the https url
input('\nPress Enter to open NASA Picture of the Day in Browser')
webbrowser.open(decodeapod['url'])
