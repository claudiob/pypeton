#!/usr/bin/env python
import bongo

class Index(bongo.PageHandler): pass

if __name__ == '__main__':
	bongo.main('%(PROJECT_NAME)s',[
		('', Index),
	], secret = '%(SECRET)s')
