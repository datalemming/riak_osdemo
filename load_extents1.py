'''
To load the truncated geohashes into a riak bucket called 5kextents
The raw data is csv format in a file called temp.txt,
format is 
strTruncatedGeohash, colon separated list of relevant polygons as a string

SMDE
18/11/15
'''


import csv
import riak
#import pickle


myc=riak.RiakClient(pb_port=8087, protocol='pbc')
print myc
myb=myc.bucket('5kextents', bucket_type="osd")
print myb

#iterate through csv file and add each to the bucket
with open("temp.txt",'rb') as csvfile:
	fr=csv.reader(csvfile)
	for row in fr:
		mykey=row[0]
		myval=row[1]
		print "Processing" + mykey + "  "+myval
		action1=myb.new(mykey,data=myval)
		action1.store()
		print "Stored"

