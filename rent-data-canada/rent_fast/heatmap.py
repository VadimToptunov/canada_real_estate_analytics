import folium
from datetime import date
from folium.plugins import  HeatMap
import branca.colormap as cm
import json
import os

basic_path = "rent-data-canada/rent_fast/"
basic_data_path = f"{basic_path}circlemap_datasets/"

def get_heatmap():

    colors_list = ['azure', 'cyan', 'blue', 'lime', 'green', 'yellow', 'orange', 'red']
    colormap = cm.LinearColormap(colors=colors_list, vmin=500, vmax=3000)
    map_object = folium.Map(location=[43.6532, -79.3832], tiles = 'Stamen Toner', zoom_start=8)
    list_files = os.listdir(basic_data_path)
    for file in list_files:
        visualize_data(file, map_object, colormap)
                
        map_object.save(f"{basic_path}generated_heatmaps/circlemap_{date.today()}.html")

def visualize_data(file, map_object, colormap):
    data = list(read_data(file))
    for i in data:
        lat = i[0]
        long = i[1]
        price = i[2]
        folium.Circle(
            location=[lat, long],
            popup = (f"""<b>Price: ${price}</b>"""),
            radius=30,
            fill=True,
            color=colormap(price),
            fill_opacity=0.2
            ).add_to(map_object)

def read_data(file):
    with open(f"{basic_data_path}{file}", "r") as file:
        data = json.loads(file.read())
    return data


if __name__ == '__main__':
    get_heatmap()
