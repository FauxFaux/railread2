#!/usr/bin/env python
import fileinput
import json
import traceback

try:
	for line in fileinput.input():
		doc = json.loads(line)
		try:
			sched = doc['JsonScheduleV1']
		except KeyError:
			continue

		seg = sched['schedule_segment']
		try:
			locs = seg['schedule_location']
		except KeyError:
			continue

		print ''
		print "schedule:", sched['schedule_days_runs']
		for loc in locs:
			pss = loc.get('pass')
			if not pss:
#				print "pass: %s" % (pss,)
#			else:
				print "{0}: {1} -> {2}".format(loc['tiploc_code'],
					loc.get('arrival'), loc.get('departure'))
except KeyError:
	print ''
	print 'BANG'
	traceback.print_exc()
	print fileinput.lineno()

