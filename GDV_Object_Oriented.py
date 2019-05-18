import folium
import pandas as pd


# To do:
# 重写DataSource类，完成与数据库的连接


USE_JUPYTER_NB   = True
SUPPRESS_WARNING = True

# Suppress Future Warning
if SUPPRESS_WARNING:
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

class GeoData:
    data = None
    map_data = None
    
    def __init__(self, data_source = None, map_source = None):
        self.data = data_source
        self.map_data = map_source

    def plot(self, plot_column, legend_name, key_on, output = 'plot_data.html'):
        map = folium.Map(location=[100, 0], zoom_start=1.5)
        # Bing Map with country_geo(.json)
        map.choropleth(geo_data = self.map_data, data = self.data[plot_column],
                     columns = plot_column, key_on = key_on,
                     fill_color = 'YlGnBu', fill_opacity = 0.7, line_opacity = 0.2,
                     legend_name = legend_name)
        # Convert Folium plot to HTML
        map.save(output) 
        print('SUCCESS: Check for plot_data.html')

        # Use IFrame to display HTML
        if USE_JUPYTER_NB:
            from IPython.display import IFrame
            display(IFrame('plot_data.html', width=700, height=450))
            
class DataSource:
    data = None
    stage = None
    select_column = None
    
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
    
    def select(self, select_column):
        # Data Selection
        stage = self.data.copy()
        assert(stage is not self.data)
        for i in range(len(select_column)//2):
            column_value =  select_column[2*i+1]
            column_head = select_column[2*i]
            mask = self.data[column_head].str.contains(column_value)
            stage = stage[mask]
            return stage
        
data_source = DataSource('Indicators.csv')
data_source = data_source.select(['IndicatorName', 'Life expectancy at birth', 'Year', 2013])
geo_data = GeoData(data_source, 'world-countries.json')
geo_data.plot(['CountryCode','Value'], 'Life expectancy at birth','feature.id')
