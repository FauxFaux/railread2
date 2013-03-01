#!/usr/bin/env python

import sys
from xml.sax import parse, handler

class Handler(handler.ContentHandler):

	def __init__(self):
		self._name = ''
		self._latitude = ''
		self._longitude = ''
		self._tiplocref = ''
		self._stationname = ''

	def startElement(self, name, attrs):
		self._name = name

	def characters(self, content):
		if self._name == 'Longitude':
			self._longitude += content
		elif self._name == 'Latitude':
			self._latitude += content
		elif self._name == 'TiplocRef':
			self._tiplocref += content
		elif self._name == 'StationName':
			self._stationname += content
	
	def endElement(self, name):
		if name == 'StopPoint':
			if self._tiplocref != '':
				print(self._tiplocref, self._latitude, self._longitude, self._stationname)
			self._longitude = self._latitude = self._tiplocref = self._stationname = ''

parse(sys.stdin, Handler())

