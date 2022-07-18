import phonenumbers
from test import number
from phonenumbers  import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium 

key = 'Your API Key'

ch_num = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_num, 'ja')
print(location)

service = phonenumbers.parse(number)
print(carrier.name_for_number(service, 'jp'))

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
# print(lat,lng)

search = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(search)
search.save('./map/location.html')