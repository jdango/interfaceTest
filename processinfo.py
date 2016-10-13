#encoding:utf-8
import sys
import os

import atexit
import time
import psutil


time.sleep(3)


line_num = 1

def getCPUstate():
	phymem = psutil.pypmem_usage()
	buffers = getattr(psutil, 'phymem_buffers', lambda:0)()
	cached = getattr(psutil, 'cached_phymem', lambda:0)()
	used = phymem.total - (phymem.free + buffers + cached)
	line = "Memory:%5s%% %6s/%s" % (
		phymem.percent,
		str(int(used / 1024 /1024)) + "M",
		str(int(phymem.total / 1024 /1024)) + "M")
	return line

def bytes2human(n):
	symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
	prefix ={}
	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10
	for s in reversed(symbols):
		if n >= prefix[s]:
			value = float(n) / prefix[s]
			return '%.2f %s' % (value, s)
	return '%.2f B' % (n)


def poll(interval):
	tot_before = psutil.network_io_counters()
	pnic_before = psutil.network_io_counters(pernic = True)
	time.sleep(interval)
	tot_after = psutil.network_io_counters()
	