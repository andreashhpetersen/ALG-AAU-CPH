import json
import urllib
import requests

url = 'https://parseapi.back4app.com/classes/Complete_List_Names?limit=10000'
headers = {
    'X-Parse-Application-Id': 'zsSkPsDYTc2hmphLjjs9hz2Q3EXmnSxUyXnouj1I', # This is the fake app's application id
    'X-Parse-Master-Key': '4LuCXgPPXXO2sU5cXm6WwpwzaKyZpo3Wpj4G4xXK' # This is the fake app's readonly master key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
with open('./names.txt', 'w') as f:
    for entry in data['results']:
        f.write(f"{entry['Name']} - {entry['Gender']}\n")
