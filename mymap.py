#importing required lib
import folium
import pandas

#reading cord. of volcano from csv files as dataframes
data=pandas.read_csv("Volcano.csv")
#ploting points on map 
map=folium.Map(location=[38.58,-99.09] , zoom_start=6)

#function to determine the color of marker
def color_finder(elevation):
    if el < 2000:
        return "green"
    elif 2000 <= elevation < 3000:
        return "orange"
    else :
        return "red"

#converting to list 
nam=list(data["NAME"])
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
#styling the banner
html = """<h4>Volcano information:</h4>
Height: %s m
"""
#feature group
fg= folium.FeatureGroup(name="my map")
#loop for plotting multiple points
for lt,ln,el, in zip(lat, lon,elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6,  popup=folium.Popup(iframe),fill_color=color_finder(el),color="gray",fill=True, fill_opacity=0.7))
map.add_child(fg)
#saving files as html 
map.save("newmap.html")
