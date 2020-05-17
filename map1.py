import folium
map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

#normally cooridantes will be in textfile
for coordinates in [[38, -99],[39, -97]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Henlo am marker", icon=folium.Icon(color='blue')))

map.add_child(fg)

map.save("Map1.html")
