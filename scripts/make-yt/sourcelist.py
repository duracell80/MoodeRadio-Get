#!/usr/bin/env python2
import json, os

f_json = []
for line in open('sourcelist.json', 'r'):
    f_json.append(json.loads(line))
    

# Number of Tracks
f_tracks = len(f_json)

if f_tracks < 1:
    os.system("sudo echo '#EXTINF:-1, YouTube: Content Not Returned, Playing Birdsong' >> /var/www/yt-play/yt-list.m3u")
    os.system("sudo echo 'http://edge-audio-03-gos2.sharp-stream.com/rspb.mp3' >> /var/www/yt-play/yt-list.m3u")

for f in range(0, f_tracks, 1):    
    
    # Title and Duration of Track
    f_title = "#EXTINF:"+str(f_json[f]['duration'])+", YouTube: " + f_json[f]['fulltitle']
    
    # URL of Audio Stream 250
    f_url   = f_json[f]['formats'][1]['url'] + "\n"
    
    if f_tracks > 1:
        os.system("sudo echo '"+f_title.encode('utf-8')+"' >> /var/www/yt-play/yt-list.m3u")
        os.system("sudo echo '"+f_url+"' >> /var/www/yt-play/yt-list.m3u")
    
    
  
os.system("sudo cp -f /var/www/yt-play/yt-list.m3u /var/lib/mpd/playlists/YouTube_Play.m3u")