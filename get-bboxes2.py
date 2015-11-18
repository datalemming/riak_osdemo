'''
To iterate through the shapefile and 
extract all bounding boxes and write them to
a file with the index

SMDE 6/11/15
'''
import shapefile
#import pickle

f=open('all-bboxes','wb')


sf=shapefile.Reader('./water/water_polygons')
shapes=sf.shapes()
max_idx=len(shapes)-1
idx=0
writeline=[]

while idx< max_idx:
	print idx
	box=shapes[idx].bbox
	f.write(str(idx)+","+str(box)+"\n")
	idx=idx+1
	
f.close()
shapes=[]
bboxes=[]
