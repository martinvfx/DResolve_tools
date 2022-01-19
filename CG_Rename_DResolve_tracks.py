#!/usr/bin/env python
##########################################################
## Script to automatice renaming tracks in timeline     ##
## Autor: Martin Elias Iglesias  martin@vfx-sup.com     ##
##########################################################

# import DaVinciResolveScript as dvr_script
# resolve = dvr_script.scriptapp("Resolve")

import sys, os, importlib
resolve = bmd.scriptapp("Resolve")
pathLib = 'C:\\Program Files\\Blackmagic Design\\DaVinci Resolve\\fusionscript.dll'

projectManager = resolve.GetProjectManager()
project = resolve.GetProjectManager().GetCurrentProject()

tracks_names = ["Digicut", "IN", "mov", "mov_version", "Fullres", "Retimed_Fullres", "Mograph", "_temp"]

timeline = project.GetCurrentTimeline()

total_tracks = timeline.GetTrackCount("video")
print('This timeline has {} tracks.'.format(total_tracks))

while total_tracks < len(tracks_names):
    timeline.AddTrack("video")
    total_tracks = timeline.GetTrackCount("video")


track_number = 1
for t in tracks_names:
    # if t is not "Digicut":
    #     print(None)
    if t is not str(timeline.GetTrackName("video", int(track_number))):
        print("{} == Track number {} was renamed to {}".format(timeline.GetTrackName("video", int(track_number)), track_number, t))
        timeline.SetTrackName("video", int(track_number), t)
        track_number +=1
    else:
        print('Nothing was changed')



