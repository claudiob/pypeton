#!/usr/bin/env python
import bongo

class Index(bongo.PageHandler): pass

urls = [
	('', Index),
]

config = {
	'secret' : '%(SECRET)s', 
}

from socket import gethostname # Hostname based local settings 
hostname = gethostname().split('.')[0]

try:
	import sys
	path = os.path.join(os.path.dirname(__file__), 'hosts')
	sys.path.insert(0, path)
	config.update((k,v) for k,v in  
		__import__(hostname).__dict__.iteritems() if k[:2] != '__')
	sys.path.remove(path)
except: 
	print >> sys.stderr, '%(yellow)sLocal settings file: [%(blue)shosts/%%s.py%(yellow)s] not found, skipped.%(normal)s' %% hostname

def main(): bongo.main('%(PROJECT_NAME)s', urls, **config)
if __name__ == '__main__': main()
