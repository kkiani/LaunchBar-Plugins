#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import webbrowser
from urllib import quote_plus

items = []

arguments = ' '.join(sys.argv[1:])

url = 'http://stackoverflow.com/search?q=' + quote_plus(arguments)
webbrowser.open(url)

print json.dumps(items)