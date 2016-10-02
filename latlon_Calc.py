from math import radians, cos, sin, asin, sqrt, degrees, atan2
import sys

def haversine(lon1, lat1, lon2, lat2):
	"""Calculates distance between 2 coordinates using haversine formula"""
	directionDict = {'North':[0,90],'East':[90,180],'South':[180,270],'West':[270,360]}
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	# haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	r = 6371 # Radius of earth in kilometers. Use 3956 for miles

	"""Calculate bearing (angle) between 2 coordinates"""
	bearing = atan2(sin(lon2-lon1)*cos(lat2), cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(lon2-lon1))
	bearing = degrees(bearing)
	bearing = (bearing + 360) % 360

	direction = ""
	for k,v in directionDict.iteritems():
		if bearing >= v[0] and bearing < v[1]:
			direction = k

	return c * r, bearing, direction

if __name__ == "__main__":
	print sys.argv[1:]
	lon1 = float(sys.argv[1:][0])
	lat1 = float(sys.argv[1:][1])
	lon2 = float(sys.argv[1:][2])
	lat2 = float(sys.argv[1:][3])

	print haversine(lon1, lat1, lon2, lat2)
