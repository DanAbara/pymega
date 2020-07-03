import folium # for creating webmaps
import pandas
import json

df = pandas.read_csv('Volcanoes.txt',sep=',')

map=folium.Map(
    location=[df["LAT"].mean(),df["LON"].mean()], # to center the map based on the lon/lat values. dont use avg for mean since this is a DataFrame df and not a simple tuple or list.
    zoom_start=5, 
    tiles='Mapbox Bright'
    ) # create map using Map method of folium

# add markers to map by iterating through the data

# function for rule based colouring
def markcolor(elev):
    minimum = int(min(df["ELEV"])) # minimum value of elevations
    increment = int((max(df["ELEV"])-min(df["ELEV"]))/3) # (max - min)/3 to compute value to increment by in order to have 3 categories

    if elev in range(minimum,minimum+increment):
        col='green'
    elif elev in range(increment,increment+increment):
        col='orange'
    else:
        col='red'
    return col

# create feature groupings for use with layer control panel on map later.
fg = folium.FeatureGroup(name='Volcano Locations')

# now create markers
for name,lat,lon,elev in zip(df["NAME"],df["LAT"],df["LON"],df["ELEV"]): # selecting lat and lon columns of the df
    fg.add_child(folium.Marker( # add the marker to feature group volcano loactions and then add these fg later to the map as seen on line #39
        location=[lat, lon],
        popup=name,
        icon=folium.Icon(color=markcolor(elev)))
    ) 

map.add_child(fg) # add volcano locations feature group to map.

# load geojson data using the encoding. see help(__builtins__.open) for info on enconding using 'open()' method.
with open('world.json', "r", encoding="utf-8-sig") as data_file:
    data = json.load(data_file)

#map.add_child(fg) # add feature group to map, so the geojson data and layer control will identify the different features.

map.add_child(folium.GeoJson(
    data=data, 
    name='world population',
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}
    )
)

map.add_child(folium.LayerControl())

map.save(outfile='testmap.html') # save the map using the save function in the Map type.