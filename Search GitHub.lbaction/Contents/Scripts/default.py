#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import webbrowser

items = []

arguments = ' '.join(sys.argv[1:])

url = 'https://github.com/search?q=' + arguments.replace(' ', '+')
webbrowser.open(url)

print json.dumps(items)
