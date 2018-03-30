#!/usr/bin/env python

import urllib

for n in ["%.2d" % i for i in range(133)]:
	urllib.urlretrieve('http://www.mapytatr.net/PRODUKTY/MAPY_TAT/WYSOKIE/SLICES/tpn_{}.jpg'.format(n), '{}.jpg'.format(n))
