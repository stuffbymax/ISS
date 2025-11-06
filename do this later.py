import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('DgVeneto AstroPi Sensor data 2023 - data.csv')

# Assume df has 'latitude', 'longitude', 'date_time'
df['date_time'] = pd.to_datetime(df['date_time'])

# Shift latitude, longitude, and time to get next points
df['lat2'] = df['latitude'].shift(-1)
df['lon2'] = df['longitude'].shift(-1)
df['time2'] = df['date_time'].shift(-1)

# Haversine formula
R = 6371000  # meters

phi1 = np.radians(df['latitude'])
phi2 = np.radians(df['lat2'])
delta_phi = np.radians(df['lat2'] - df['latitude'])
delta_lambda = np.radians(df['lon2'] - df['longitude'])

a = np.sin(delta_phi/2)**2 + np.cos(phi1)*np.cos(phi2)*np.sin(delta_lambda/2)**2
c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
df['distance_m'] = R * c  # meters


# Time difference in seconds
df['delta_t'] = (df['time2'] - df['date_time']).dt.total_seconds()

# Speed in m/s
df['speed_m_s'] = df['distance_m'] / df['delta_t']


# dont show what is not lat lon and date_time



# Set datetime as index for plotting
df.set_index('date_time', inplace=True)

print(df)

df.plot()
plt.show()




