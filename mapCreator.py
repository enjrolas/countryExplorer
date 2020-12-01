import pygal   
from pygal.style import Style 
from decouple import config
from pygal.maps.world import COUNTRIES

def createMap(countryCode, debug=False):
    print(countryCode)
    country=COUNTRIES[countryCode]

    everyOtherCountry=list(COUNTRIES.keys())
    everyOtherCountry.remove(countryCode)
    custom_style = Style(
        show_legend=False,
        colors=('#000000', '#BBBBBB'))

    worldmap =  pygal.maps.world.World(show_legend=False, show_title=False, style=custom_style)
    worldmap.add(country,  
             [countryCode],
                 )
    
    worldmap.add('everyone else',  
                 everyOtherCountry,
                 )
    if debug:
        worldmap.render_in_browser()
    else:
        worldmap.render_to_file('%s/%s/map.svg' % (config('countryDirectory'), country))
  

