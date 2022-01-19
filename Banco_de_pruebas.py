#!/usr/bin/env python
##################################################################
## Script test area for try functions into Davinci Resolve      ##
## Autor: Martin Elias Iglesias  martin@vfx-sup.com             ##
##################################################################
print(resolve.GetHelp())
# import DaVinciResolveScript as dvr_script
# resolve = dvr_script.scriptapp("Resolve")

# import sys, os, importlib
resolve = bmd.scriptapp("Resolve")
pathLib = 'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll'

projectManager = resolve.GetProjectManager()
project = resolve.GetProjectManager().GetCurrentProject()

timeline = project.GetCurrentTimeline()
# print("{} == Track number {} was renamed to {}".format(timeline.GetTrackName("video", int(track_number)), track_number,t))
# timeline.SetTrackName("video", int(track_number), t)
# timeline.SetTrackColor("video", 1, "Blue")
print(timeline.GetTrackColor("video", 1))
