import math

"""
:lat1 = value from latitude from MKAD 66km, Moscow. lat = 55.755826
:long1 = value from longtitude from MKAD 66km, Moscow. lng = 37.6173 
"""


def haversine(lat1, long1, lat2, long2):
    """
    Callculate the great circle distance beetwen two points
    on the earth(specific in decimal degrees)
    """
    # convert decimal degrees to radians
    lat1, long1, lat2, long2 = map(math.radians, [lat1, long1, lat2, long2])

    # haversine formula
    dlat = lat2 - lat1
    dlong = long2 - long1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    # Radius in Kilometers, for Miles use 3956
    r = 6371
    return c * r
