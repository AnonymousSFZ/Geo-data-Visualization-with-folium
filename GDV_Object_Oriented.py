import folium, sqlite3
import pandas as pd

USE_JUPYTER_NB   = True
SUPPRESS_WARNING = True

# Suppress Future Warning
if SUPPRESS_WARNING:
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

class DataSource:
    __cursor = None
    
    def __init__(self, database_name):
        conn = sqlite3.connect(database_name)
        self.cursor = conn.cursor()
        print(database_name, ' opened successfully')
    
    def select(self, table_name, select_column):
        # Data Selection
        sql = DataSource.sql_constructor(table_name, select_column)
        cursor = self.cursor.execute(sql)
        return DataSource.cursor2dataframe(cursor)
       
    @staticmethod
    def sql_constructor(table_name, select_column):
        sql = 'select * from ' + table_name + ' where '\
           + select_column[0] + ' = \'' + select_column[1] + '\' '
        for i in range(1, len(select_column)//2):
            sql += 'and ' + select_column[2*i] + ' = \'' + select_column[2*i+1] + '\''
        return sql
    
    @staticmethod
    def cursor2dataframe(cursor):
        # cursor to dictionary
        dict = {}
        colnames = cursor.description
        colnames = [i[0] for i in colnames]
        for colname in colnames:
                    dict[colname] = []
        for row in cursor:
            for value, colname in zip(row, colnames):
                    dict[colname].append(value)
        # dictionary to dataframe
        return pd.DataFrame(dict)
    
class GeoData:
    __data = None
    __map_data = None
    
    def __init__(self, data_source = None, map_source = None):
        self.__data = data_source
        self.__map_data = map_source

    def plot(self, plot_column, legend_name, key_on, output = 'plot_data.html'):
        map = folium.Map(location=[100, 0], zoom_start=1.5)
        # Bing Map with country_geo(.json)
        map.choropleth(geo_data = self.__map_data, data = self.__data[plot_column],
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
        
data_source = DataSource('database.sqlite')
data_source = data_source.select('Indicators', \
                    ['IndicatorName', 'Life expectancy at birth, total (years)', 'Year', '2013'])
geo_data = GeoData(data_source, 'world-countries.json')
geo_data.plot(['CountryCode','Value'], 'Life expectancy at birth','feature.id')
