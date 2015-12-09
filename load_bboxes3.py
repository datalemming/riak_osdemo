'''
To load the mid points of a bounding box into a riak bucket called bboxes,
to calculate a geohash for the mid point of the bounding box
to store that geohash in a bucket called geohashes
to write out the index and geohash to a file on disk for further processing

SMDE
17/11/15

Changed to include object content_type and supressed the output of file
as this is done elsewhere
SMDE
25/11/15

'''


import csv
import geohash
import riak
import pickle

#outfile=open("boxes-and-hashes-2.csv",'wb')

myc=riak.RiakClient(pb_port=8087, protocol='pbc')
print myc
myboxbucket=myc.bucket_type('osd').bucket('new-bboxes')
print myboxbucket
myhashbucket=myc.bucket_type('osd').bucket('new-geohashes')
print myhashbucket

with open('all-bboxes2.csv', 'rb') as csvfile:
	bboxreader=csv.reader(csvfile)
	for row in bboxreader:
		index=str(row[0])
		maxlong=float(row[1])
		maxlat=float(row[2])
		minlong=float(row[3])
		minlat=float(row[4])
		midlat=float(row[5])
		midlong=float(row[6])
		print midlat,midlong
		gh=geohash.encode(midlat,midlong)
		print index, gh
		print index, row[1:5]
		obj1=riak.riak_object.RiakObject(myc,myhashbucket,index)
		obj1.content_type='text/plain'
		obj1.data=gh
		obj1.store()
		bcoords=row[1:5]
		obj2=riak.riak_object.RiakObject(myc,myboxbucket,index)
		obj2.content_type='text/plain'
		obj2.data=pickle.dumps(bcoords)
		obj2.store()
		#outfile.write(index+","+gh)
		
#outfile.close()
		

