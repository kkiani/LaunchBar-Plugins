#!/usr/local/bin/python3
#
# LaunchBar Action Script
#
import sys
import json
import os

def subTitleFixer(path):
    file = open(path, 'r', encoding='windows-1256')
    text = file.read()
    file.close()
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
        
def PushNotification():
    script = """osascript -e 'tell application "LaunchBar"\n	display in notification center "he subtitle file replaced with the fixed one" with title "Subtitle Fixer"\n	hide\nend tell'"""
    os.system(script)

    
items = []

arguments = ' '.join(sys.argv[1:])
subTitleFixer(arguments)
PushNotification()
