# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint:
    def __init__(self, lat, lon, name):
        LatLon.__init__(self, lat, lon)
        self.name = name

    def __str__(self):
        #return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
        return f"{self.name} is located at {self.lat} latitude and {self.lon} longitude."

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache:
    def __init__(self, name, difficulty, size, lat, lon):
        Waypoint.__init__(self, lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return f"{self.name} is located at {self.lat} latitude and {self.lon} longitude. It is catorgorized as size {self.size} with a {self.difficulty} difficulty rating."

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(41.70505, -121.51521, "Catacombs")

print(waypoint.name, waypoint.lat, waypoint.lon)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache.name, geocache.difficulty, geocache.size, geocache.lat, geocache.lon)

# Print it--also make this print more nicely
print(geocache)
