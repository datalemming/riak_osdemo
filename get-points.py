'''
To iterate through the shapefile and 
extract all polygon points and write them to
a file with the idx

SMDE 5/11/15

17/11/15
Changed the output syntax to make it easier to process.
'''
import shapefile
#import pickle

f=open('all-points2.csv','wb')
#points=[]

sf=shapefile.Reader('./water/water_polygons')
shapes=sf.shapes()
max_idx=len(shapes)-1
idx=0
fileline=[]

while idx< max_idx:
	print idx
	poly=shapes[idx].points
	#fileline.append([idx,poly])
	f.write(str(idx)+","+ str(poly)+"\n")
	idx=idx+1
	#fileline=[]

#shapes=[]

f.close()
