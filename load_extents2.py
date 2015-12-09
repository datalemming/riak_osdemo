'''
To load the truncated geohashes into a riak bucket called 5kextents
The raw data is csv format in a file called temp.txt,
format is 
strTruncatedGeohash, colon separated list of relevant polygons as a string

SMDE
18/11/15

Changed to 4 characters in geohash
23/11/15 SMDE

Changed to include content_type as test/plain as default python one is json and this
was causing issues.
25/11/15 SMDE
'''


import csv
import riak
#import pickle


myc=riak.RiakClient(pb_port=8087, protocol='pbc')
print myc
bucket=myc.bucket_type('osd').bucket('new-4c-extents')
print bucket

#iterate through csv file and add each to the bucket
with open("gh-4char.csv",'rb') as csvfile:
	fr=csv.reader(csvfile)
	for row in fr:
		mykey=row[0]
		myval=row[1]
		print "Processing" + mykey + "  "+myval
		obj=riak.riak_object.RiakObject(myc,bucket,mykey)
		obj.content_type='text/plain'
		obj.data=myval
		obj.store()

