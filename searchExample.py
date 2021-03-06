from google_images_search import GoogleImagesSearch
from decouple import config
import os
from PIL import Image
# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch(config('API_KEY'), config('CX'))

# define search params:
_search_params = {
    'q': 'morocco',
    'num': 10,
#    'safe': 'off',
#    'fileType': 'jpg|gif|png',
    'imgType': 'photo',
#    'imgSize': 'HUGE',
#    'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow',
#    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
#    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'
}

# this will only search for images:
#print(gis.search(search_params=_search_params))

# this will search and download:
#gis.search(search_params=_search_params, path_to_dir='path/')

# this will search, download and resize:
#gis.search(search_params=_search_params, path_to_dir='path/', width=500, height=500)

# search first, then download and resize afterwards:
gis.search(search_params=_search_params)
for image in gis.results():
    for attr, value in image.__dict__.items():
        print ("%s, %s" % (attr, value))

    image.download('path/')
    image.resize(500, 500)
