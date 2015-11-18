'''
To load the polygon points into a riak bucket called polygons
There was an issue with the csv format, so go back to the root shapefile
to do the work.

SMDE
17/11/15
'''


#import csv

import shapefile
import riak
import pickle


myc=riak.RiakClient(pb_port=8087, protocol='pbc')
print myc
myb=myc.bucket('polygons', bucket_type="osd")
print myb

sf=shapefile.Reader('./water/water_polygons')
shapes=sf.shapes()
max_idx=len(shapes)-1
idx=10

print idx
poly=shapes[idx].points
print poly	
val1=pickle.dumps(poly)
key1=myb.new(str(idx),data=val1)
key1.store()
print key1	
idx=idx+1
key1=""
val1=""
print "Next record\n"

shapes=[]	

