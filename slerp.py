from pysal.cg import sphere

jfk = (-73.778925,40.639751)
sfo = (-122.374889,37.618972)
mph = 300

miles = sphere.arcdist(jfk, sfo, sphere.RADIUS_EARTH_MILES)
hours = miles / mph

print "Reach SFO from JFK in {0} hours at {1} mph".format(hours, mph)
print "Hourly weather forecast coordinates:"

# WeatherSource only returns hourly forecasts on the hour
reports = int(round(hours))

for i in range(reports):
    print sphere.geointerpolate(jfk, sfo, i/float(reports))

