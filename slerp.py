from pysal.cg import sphere

jfk = (-73.778925,40.639751)
sfo = (-122.374889,37.618972)
gso = (-79.937306,36.09775)
mia = (-80.290556,25.79325)
mph = 300

miles = sphere.arcdist(gso, mia, sphere.RADIUS_EARTH_MILES)
hours = miles / mph

print "Reach MIA from GSO in {0} hours at {1} mph".format(hours, mph)
print "Hourly weather forecast coordinates:"

# WeatherSource only returns hourly forecasts on the hour
reports = int(round(hours))

for i in range(reports):
    print sphere.geointerpolate(jfk, sfo, i/float(reports))

