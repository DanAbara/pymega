# This script was started but I decided to discontinue and modify the first one instead.

# import modules
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt") # load pandas data

lat = list(data["LAT"]) # Latitude list from df
lon = list(data["LON"]) # Longitude list from df
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

# function for rule based colouring of markers
def color_maker(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <3000:
        return 'orange'
    else:
        return 'red'

# set base map
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcano points") # create feature group fgv for volcanoes

# add markers to feature group as points of volcanoes
for lt, ln, el in zip(lat, lon, elev): # zip enables the rows on each column to be mathed to the corresponding row values / with each other
    iframe = folium.IFrame(html=html % str(el), width=150, height=100)
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln],
        popup=folium.Popup(iframe),          #folium.Popup(str(el), parse_html=True), -- use this if there are quotes (') in the string
        radius=6,
        fill=True,
        fill_color=color_maker(el),
        color="grey", # sets the border colours for all markers
        fill_opacity=0.7 # this sets transparency
    )
)

# Load geojson data using the encoding. see help(__builtins__.open) for info on enconding using 'open()' method.
# The data is of the world, it uses a polygon type to categorise the different regions
# POP2005 attribute gives us the population of the different regions
# lambda is a 1 line function. eg. l = lambda x = x**2. l(5) will return 25.

fgp = folium.FeatureGroup(name="Population") # create feature group fgp for population

fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(), 
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'})
)

# add the created feature groups to map
map.add_child(fgv) 
map.add_child(fgp)

map.add_child(folium.LayerControl()) # to display the different feature groups. Must come after adding the feature group to the map.

# save map
map.save("Map2.html")