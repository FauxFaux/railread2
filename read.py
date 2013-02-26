#!/usr/bin/env python
import datetime
import fileinput
import json
import traceback

now = datetime.date.today().isoformat()

try:
	for line in fileinput.input():
		doc = json.loads(line)
		try:
			sched = doc['JsonScheduleV1']
		except KeyError:
			# it's not a schedule line, normal
			continue

		if sched['CIF_stp_indicator'] != 'P':
			# P is for pants, also permanant
			continue

		if sched['schedule_start_date'] > now or sched['schedule_end_date'] < now:
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

