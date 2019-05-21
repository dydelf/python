"""
Visual representation of coordinated and areas using Folium library.
"""

import pandas
import folium


data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    elif elevation >= 3000:
        return "red"

map = folium.Map(location=[38, -99], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
        popup=str(int(el)), fill_color=color_producer(el), color = "grey",
        fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r",
    encoding="utf-8-sig").read(), style_function=lambda x: {'fillColor':
    'green' if x['properties']['POP2005'] < 15000000 else 'orange' if 15000000
    <= x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("volcanoes.html")
