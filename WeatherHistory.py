__author__ = 'ab'

import simplejson
import urllib
import urllib2
import xml.sax
from WeatherImportHandler import WeatherImportHandler

address = urllib.urlencode({"q": "51427, Bergisch Gladbach, Germany"})
url = "http://nominatim.openstreetmap.org/search.php?%s&format=json&addressdetails=0" % address
req = urllib2.Request(url)
opener = urllib2.build_opener()
input = opener.open(req)

data = simplejson.load(input)
print data[0]["lat"] + " " + data[0]["lon"]


url = "http://api.yr.no/weatherapi/locationforecast/1.9/?lat=%s;lon=%s" % (data[0]["lat"], data[0]["lon"])
req = urllib2.Request(url)
input = opener.open(req)
xmldata = input.read()

handler = WeatherImportHandler()
xml.sax.parseString(xmldata, handler)
print handler.temperature