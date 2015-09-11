#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json

items = []
actions = ['Global Variables', 'IBOutlets', 'Functions', 'IBActions']

# Note: The first argument is the script path!
for i in range(0,actions.__len__()):
	item = {}
	item['title'] = actions[i]
	items.append(item)


print json.dumps(items)
