'''
To check the sensitivity of geohash
smde 12/11/15
'''

from __future__ import division
import geohash

latitude=0
longitude=0
for latitude in range(0,89):
	for longitude in range(0,179):
		print latitude/10,longitude/10,geohash.encode(latitude/10,longitude/10,precision=5)


		
