import folium
from datetime import date
import branca.colormap as cm
import json
import os

from realtor_enums.RealtorEnums import RealtorEnums

basic_path = RealtorEnums.GENERATED_CIRCLEMAPS_PATH.value


def get_circlemap():
    colors_list = ['azure', 'cyan', 'blue', 'lime', 'green', 'yellow', 'orange', 'red']
    colormap = cm.LinearColormap(colors=colors_list, vmin=500, vmax=3000)
    map_object = folium.Map(location=[43.6532, -79.3832], tiles='Stamen Toner', zoom_start=8)
    list_files = os.listdir(RealtorEnums.CIRCLEMAP_DATASETS.value)
    for file in list_files:
        visualize_data(file, map_object, colormap)
                
        map_object.save(f"{basic_path}circlemap_{date.today()}.html")


def visualize_data(file, map_object, colormap):
    data = list(read_data(file))
    for i in data:
        lat = i[0]
        long = i[1]
        price = i[2]
        folium.Circle(
            location=[lat, long],
            popup =f"""<b>Price: ${price}</b>""",
            radius=30,
            fill=True,
            color=colormap(price),
            fill_opacity=0.2
            ).add_to(map_object)


def read_data(file):
    with open(f"{RealtorEnums.CIRCLEMAP_DATASETS.value}{file}", "r") as file:
        data = json.loads(file.read())
    return data


if __name__ == '__main__':
    get_circlemap()
