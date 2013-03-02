#!/usr/bin/env python

import PIL.Image, PIL.ImageDraw
import sys
import collections

Station = collections.namedtuple('Station', ['code', 'lat', 'lon', 'name'])

def read_stations():
	ret = {}
	f = open('stations.lst')
	for line in f:
		vas = line.rstrip().split(' ', 3)
		ret[vas[0]] = Station(vas[0], float(vas[1]), float(vas[2]), vas[3])
	return ret

stations = read_stations()

size = (1000, 2000)
black = (0, 0, 0)
white = (255, 255, 255)

# oh yes I did
gps_zero_zero = (58.5901662093, -5.8390713972)
gps_one_one = (50.1216682052, 1.7497278474)
gps_size = (gps_one_one[0]-gps_zero_zero[0], gps_one_one[1]-gps_zero_zero[1])

im = PIL.Image.new('RGB', size, white)
draw = PIL.ImageDraw.Draw(im)

#draw.polygon([(0,0),(500,500)], outline=black)


last = None
run = []

maxlat = maxlon = -99
minlat = minlon = 99

f = open('readed.lst')
for line in f:
	if line == '\n' or line.startswith('schedule'):
		if len(run) > 2:
			draw.polygon(run, outline=black)
		run = []
		continue
	try:
		stat = stations[line.split(':')[0]]
		if stat.lon < minlon:
			minlon = stat.lon
		if stat.lon > maxlon:
			maxlon = stat.lon
		if stat.lat < minlat:
			minlat = stat.lat
		if stat.lat > maxlat:
			maxlat = stat.lat
		run.append(
			(
				(stat.lon - gps_zero_zero[1])/gps_size[1] * size[0],
				(stat.lat - gps_zero_zero[0])/gps_size[0] * size[1]
			)
		)
	except KeyError:
		pass

im.save('lol.png', 'PNG')
print (minlat, minlon, maxlat, maxlon)

