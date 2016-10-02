import latlon_Calc

if __name__ == "__main__":
	f = open("gps_data.csv", "r")
	gpsData = f.readlines()
	f.close()
	gpsData = gpsData[-1]
	#print gpsData
	lon1 = float(sys.argv[1:][0])#85.330462
	lat1 = float(sys.argv[1:][1])#27.714224
	lon2 = float(gpsData[2])
	lat2 = float(gpsData[1])
	data = latlon_Calc.haversine(lon1, lat1, lon2, lat2)
	distance = str(int(data[0]))
	direction = str(data[2])
	f = open("foo.txt", "w")
	print "distance ", distance, "metres",  "direction", direction
	f.write("Distance "+distance+" metres direction "+direction)
	f.close()
