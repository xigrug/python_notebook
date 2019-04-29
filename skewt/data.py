from datetime import datetime
from metpy.units import units
from siphon.simplewebservice.wyoming import WyomingUpperAir
date = datetime(2017, 9, 10, 6)
station = 'MFL'
df = WyomingUpperAir.request_data(date, station)
print(df.columns)
pressure = df['pressure'].values * units(df.units['pressure'])
temperature = df['temperature'].values * units(df.units['temperature'])
dewpoint = df['dewpoint'].values * units(df.units['dewpoint'])
u_wind = df['u_wind'].values * units(df.units['u_wind'])
v_wind = df['v_wind'].values * units(df.units['v_wind'])
print(pressure)
print(pressure[0])
print(temperature[0])
print(dewpoint[0])

