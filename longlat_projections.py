import pandas as pd
import geopandas
from matplotlib import pyplot as plt
from Prep_zone import prep_zone_area

df = pd.DataFrame({'VLF code': ['PTK', 'JJY', 'JJI', 'NWC'], 'Latitude': [53.090, 37.372557, 32.092247, -21.816325], 'Longitude': [158.550, 140.849007, 130.829095, 114.16546]})

geodf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
print(geodf)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

# We restrict to South America.
ax = world.plot(color='white', edgecolor='black')
# We can now plot our ``GeoDataFrame``.
geodf.plot(ax=ax, color='red')
plt.show()