import datetime
import folium

from db.DBConnector import DBConnector

geo = "rent-data-canada/lfsa.geojson"


def get_map():
    m = folium.Map(location=[43.6532, -79.3832], zoom_start=10, tiles=None)
    folium.TileLayer('CartoDB positron', name="Light Map", control=False).add_to(m)
    db_conn = DBConnector("rent-data-canada/database/apptdata.db")
    ready_df = db_conn.get_data_frame()
    chloropleth = folium.Choropleth(
        geo_data=geo,
        name='Choropleth Map of Canada 1 Bedroom Apartments Rent Prices',
        data=ready_df,
        columns=['fsa', "average_price"],
        key_on='feature.properties.CFSAUID',
        bins=9,
        fill_color='OrRd',
        nan_fill_color="White",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Median Rent Price',
        highlight=True,
        line_color='black').add_to(m)

    folium.features.GeoJson(
        data=geo,
        name='Apartment Average Prices',
        smooth_factor=2,
        style_function=lambda x: {'color': 'black', 'fillColor': 'transparent', 'weight': 0.5},
        tooltip=folium.features.GeoJsonTooltip(
            fields=['CFSAUID', "PRNAME"],
            aliases=["FSA: ", "Province: "],
            sticky=False)
    ).add_to(chloropleth)
    m.save(f"Chloro-map-{datetime.date.today()}.html")
