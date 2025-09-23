import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# محدوده ایران [min lon, max lon, min lat, max lat]
extent = [44, 64, 24, 40]

cities = [
    {"name": "Tehran", "lat": 35.6892, "lon": 51.3890, "pop": 8846782},
    {"name": "Mashhad", "lat": 36.2605, "lon": 59.6168, "pop": 3001184},
    {"name": "Isfahan", "lat": 32.6539, "lon": 51.6660, "pop": 1961260},
    {"name": "Shiraz", "lat": 29.5918, "lon": 52.5836, "pop": 1565572},
    {"name": "Tabriz", "lat": 38.0667, "lon": 46.2993, "pop": 1558693},
    {"name": "Qom", "lat": 34.6416, "lon": 50.8746, "pop": 1201158},
    {"name": "Ahvaz", "lat": 31.3203, "lon": 48.6692, "pop": 1184788},
    {"name": "Kermanshah", "lat": 34.3142, "lon": 47.0650, "pop": 946651},
    {"name": "Urmia", "lat": 37.5527, "lon": 45.0761, "pop": 736224}
]

# شکل و محور
plt.figure(figsize=(8, 8))
m = Basemap(projection='merc',
            llcrnrlon=extent[0], urcrnrlon=extent[1],
            llcrnrlat=extent[2], urcrnrlat=extent[3],
            resolution='i')

# ویژگی‌ها
m.drawcountries(linewidth=1, color="black")   # مرز کشورها
m.drawcoastlines(linewidth=0.8)              # خطوط ساحلی
m.fillcontinents(color="lightgray", lake_color="lightblue")  # خشکی‌ها
m.drawmapboundary(fill_color="lightblue")   # پس‌زمینه (اقیانوس‌ها)
m.drawrivers(color="blue")                  # رودخانه‌ها

# شهرها
for city in cities:
    x, y = m(city["lon"], city["lat"])
    m.scatter(x, y, marker='o', s=city["pop"]/10000,
              color="brown", alpha=0.5, zorder=5)
    plt.text(x+20000, y, city["name"], fontsize=8, color="black")

plt.title("Major Cities in Iran (Population Size)")
plt.show()

