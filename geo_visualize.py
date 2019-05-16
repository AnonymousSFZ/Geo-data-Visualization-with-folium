import folium
import pandas as pd

USE_JUPYTER_NB   = True
VERBOSE          = False
SUPPRESS_WARNING = True

# Suppress Future Warning
if SUPPRESS_WARNING:
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

# Import Dataset and Map
country_geo = 'world-countries.json'
data = pd.read_csv('Indicators.csv')

# Dataset Overview
if VERBOSE:
    countries = data['CountryName'].unique().tolist()
    indicators = data['IndicatorName'].unique().tolist()
    print('Head of dataset:', data.head(), sep='\n', end='\n\n')
    print('Number of Countries: ', len(countries), sep='\n', end='\n\n')
    print('Indicator Name:', len(indicators), sep='\n', end='\n\n')

# Data Selection
hist_indicator =  'Life expectancy at birth'
hist_year = 2013
mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year])
stage = data[mask1 & mask2]
data_to_plot = stage[['CountryCode','Value']]
if VERBOSE:
    print('Data to plot:', data_to_plot.head(), sep='\n',end='\n\n')

# Map Plot
hist_indicator = stage.iloc[0]['IndicatorName']
map = folium.Map(location=[100, 0], zoom_start=1.5)
# Bing Map with country_geo(.json)
map.choropleth(geo_data=country_geo, data=data_to_plot,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator)
# Convert Folium plot to HTML
map.save('plot_data.html') 
print('SUCCESS: Check for plot_data.html')

# Use IFrame to display HTML
if USE_JUPYTER_NB:
    from IPython.display import IFrame
    display(IFrame('plot_data.html', width=700, height=450))
