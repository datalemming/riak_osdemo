'''
To load the polygon points into a riak bucket called polygons
There was an issue with the csv format, so go back to the root shapefile
to do the work.

SMDE
17/11/15

Changed content_type to 'text/plain' due to default being json
smde 25/11/15
'''


#import csv

import shapefile
import riak
import pickle


myc=riak.RiakClient(pb_port=8087, protocol='pbc')
print myc
bucket=myc.bucket_type('osd').bucket('new-polygons')
print bucket

sf=shapefile.Reader('./water/water_polygons')
shapes=sf.shapes()
max_idx=len(shapes)-1
idx=0

while idx< max_idx:
	print idx
	poly=shapes[idx].points
	print poly	
	obj=riak.riak_object.RiakObject(myc,bucket,str(idx))
	obj.content_type='text/plain'
	obj.data=pickle.dumps(poly)
	obj.store()
	idx=idx+1
	print "Next record\n"

shapes=[]	

