'''
To calculate geohash of the top left and bottom right 
coords of the bounding boxes of the water polygons.

Format of line is
id
bottom long, lat
top long, lat

Some of the bboxes have a latitude of 90 degrees and geohash cannot cope with this.
Will need to adjust to 89.9r9

SME 11/11/2015

'''

import geohash
import csv

with open("all-bboxes", 'rb') as csvfile:
	br=csv.reader(csvfile)
	for row in br:
		#print row
		id=int(row[0])
		bottom_long=float(row[1])
		bottom_lat=float(row[2])
		if bottom_lat == 90:
			bottom_lat=bottom_lat-.000000001
		top_long=float(row[3])
		top_lat=float(row[4])
		if top_lat==90:
			top_lat=top_lat-.000000001
		try:
			print str(geohash.encode(bottom_lat,bottom_long, precision=4))+","+str(id)
			print str(geohash.encode(top_lat,top_long, precision=4))+","+str(id)
		except:
			print "*** Issue with "+str(id)
			print bottom_lat, bottom_long
			print top_lat, top_long
			print "***"


csvfile.close()			
	
