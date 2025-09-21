import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

extent = [44, 64, 24, 40]  # [min lon, max lon, min lat, max lat]
cities=[
    {"name": "Tehran", "lat": 35.6892, "lon": 51.3890, "pop": 8846782},
    {"name": "Mashhad", "lat": 36.2605, "lon": 59.6168, "pop": 3001184},
    {"name": "Isfahan", "lat": 32.6539, "lon": 51.6660, "pop": 1961260},
    # {"name": "Karaj", "lat": 35.8355, "lon": 50.9916, "pop": 1592492},
    {"name": "Shiraz", "lat": 29.5918, "lon": 52.5836, "pop": 1565572},
    {"name": "Tabriz", "lat": 38.0667, "lon": 46.2993, "pop": 1558693},
    {"name": "Qom", "lat": 34.6416, "lon": 50.8746, "pop": 1201158},
    {"name": "Ahvaz", "lat": 31.3203, "lon": 48.6692, "pop": 1184788},
    {"name": "Kermanshah", "lat": 34.3142, "lon": 47.0650, "pop": 946651},
    {"name": "Urmia", "lat": 37.5527, "lon": 45.0761, "pop": 736224}
]
#  شکل و محور
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(8, 8))

#  محدوده
ax.set_extent(extent, crs=ccrs.PlateCarree())

# ویژگی‌های جغرافیایی
ax.add_feature(cfeature.BORDERS, linewidth=1, edgecolor="black")   # مرز کشورها
ax.add_feature(cfeature.COASTLINE, linewidth=0.8)                  # خطوط ساحلی
ax.add_feature(cfeature.LAND, facecolor="lightgray")               # خشکی‌ها
ax.add_feature(cfeature.OCEAN, facecolor="lightblue")              # اقیانوس‌ها
ax.add_feature(cfeature.LAKES, facecolor="lightblue")              # دریاچه‌ها
ax.add_feature(cfeature.RIVERS, edgecolor="blue")                  # رودخانه‌ها

for city in cities:
    ax.scatter(city["lon"], city["lat"], marker='o', s=city["pop"]/10000,color="brown", alpha=0.5, label=city["name"])
    ax.text(city["lon"] + 0.3, city["lat"],
            city["name"],
            color="black",
            fontsize=8, transform=ccrs.PlateCarree())

plt.show()
