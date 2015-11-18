'''
To iterate through the shapefile and 
extract all bounding boxes and write them to
a pickle with the index

SMDE 5/11/15
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
	writeline.append(idx,box)
	f.write(str(writeline+"\n"))
	idx=idx+1
	writeline=[]
	
f.close()
shapes=[]
bboxes=[]
