from google_images_search import GoogleImagesSearch
from decouple import config
import os
from PIL import Image
from mapCreator import *
from pygal.maps.world import COUNTRIES
import random
import urllib

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch(config('API_KEY'), config('CX'))

countryCode=random.choice(list(COUNTRIES.keys()))
country=COUNTRIES[countryCode]
print(country)
print(countryCode)

try:
    os.mkdir(config('countryDirectory'))
except:
    pass

try:
    os.mkdir("%s/%s" % (config('countryDirectory'), country))
except:
    pass

createMap(countryCode)

terms=["nature", "traditional people", "food", "city", "wildlife", "unusual", "animal"]

for term in terms:
    # define search params:
    _search_params = {
        'q': '%s %s' % (country, term),
        'num': 10,
        #    'safe': 'off',
        #    'fileType': 'jpg|gif|png',
        'imgType': 'photo',
        'imgSize': 'HUGE',
        #    'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow',
        #    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
        #    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
        }
    print("searching for %s" % _search_params['q'])
    imageDirectory="%s/%s/" % (config('countryDirectory'), country)
    gis.search(search_params=_search_params)
    print(gis.results())
    print(list(gis.results()))
    image=random.choice(gis.results())
    print(image)
    for attr, value in image.__dict__.items():
        print ("%s, %s" % (attr, value))
        
    path = urllib.parse.urlparse(image._url).path
    file= path.split('/')[-1]
    ext = file.split('.')[1]    
    print("filename: %s" % file)
    print("extension: %s" % ext)
    print("downloading image to %s" % imageDirectory)
    image.download(imageDirectory)
    originalImage="%s%s" % (imageDirectory, file)
    finalName= "%s%s.%s" % (imageDirectory, term, ext)
    print("renaming %s to %s" % (originalImage, finalName))
    os.rename(originalImage, finalName)
