#!/usr/bin/env python
#
# LaunchBar Action Script
#

from os import system

system("defaults write com.apple.finder CreateDesktop -bool false")
system("killall Finder")