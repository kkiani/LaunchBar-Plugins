#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import goslate


arguments = ' '.join(sys.argv[1:])
# scriptOutput = []


items = []

# item = {}
# item['title'] = arguments + ' to persian'
# items.append(item)

# # Note: The first argument is the script's path
# for arg in sys.argv[1:]:
#     item = {}
#     item['title'] = 'Argument: ' + arg
#     items.append(item)

def translte():
	gs = goslate.Goslate()
	result = gs.translate(arguments, 'fa')
	item = {}
	item['title'] = result
	item['subtitle'] = 'translating ' + arguments
	item['icon'] = 'Marcus-Roberto-Google-Play-Google-Translate'
	items.append(item)
    
translte()


print json.dumps(items)
