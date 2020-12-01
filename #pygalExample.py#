# import pygal 
import pygal 
  
# import Style class from pygal.style 
from pygal.style import Style 
import random
  
import csv

from pygal.maps.world import COUNTRIES
print(COUNTRIES)
#pick a random country
countryCode=random.choice(list(COUNTRIES.keys()))
country=COUNTRIES[countryCode]
print(country)
print(countryCode)

everyOtherCountry=list(COUNTRIES.keys())
everyOtherCountry.remove(countryCode)
print(everyOtherCountry)
# create a world map, 
# Style class is used for using 
# the custom colours in the map, 
from pygal.style import Style
#custom_style = Style(
#  colors=('#FF00000', '#000000'))
custom_style = Style(
    show_legend=False,
    colors=('#000000', '#BBBBBB'))

worldmap =  pygal.maps.world.World(show_legend=False, show_title=False, style=custom_style)
#worldmap =  pygal.maps.world.World(fill=True)

  
print([countryCode])
  
# hex code of colours are used 
# for every .add() called 
worldmap.add(country,  
             [countryCode],
             )
  
worldmap.add('everyone else',  
             everyOtherCountry,
             )
  
# save into the file 
worldmap.render_in_browser()
#worldmap.render_to_file('%s.svg' % country) 
  
print("Success") 
