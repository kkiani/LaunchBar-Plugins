#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import subprocess

items = []

def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

# Note: The first argument is the script path!
for i in range(1, len(sys.argv)):
    argument = sys.argv[i]
    item = {}
    item['title'] = getClipboardData()
    items.append(item)

print json.dumps(items)
