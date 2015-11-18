import shapefile
#import pickle

#f=open("all-polys.pickle","wb")
#polys=[]
sf=shapefile.Reader("./water/water_polygons")
idx=0
max_idx=len(list(sf.iterShapes()))
print max_idx













'''sr=sf.shapeRecord(3)
print sr
print sr.shape
print sr.record
print sr.shape.shapeType
print sr.shape.bbox
print sr.shape.points
'''
