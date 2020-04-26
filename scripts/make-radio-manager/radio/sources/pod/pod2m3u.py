import sys, os, urllib, podcastparser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')


feedurl         = sys.argv[1]
data            = podcastparser.parse(feedurl, urllib.urlopen(feedurl), 25)
pod_title       = data["title"]
pod_timeformat  = "%m/%d/%Y"
pod_m3u         = "#EXTM3U\n"




# Let's do this, metaverse from podcastparser.py ...
# total_time,
# description
# payment_url
# link
# guid
# enclosures:
#    url
#    mime_type,
#    file_size
#    file_size
# description_html
# title
# published
# episode_art_url


for s in data["episodes"]:
    
    pod_date    = datetime.fromtimestamp(s["published"])
    pod_m3u     = pod_m3u + "#EXTINF:"+ str(s["total_time"])+ "," + pod_title + " - " + pod_date.strftime(pod_timeformat) + " - " + s["title"] + "\n"
    
    for e in s["enclosures"]:
        pod_m3u = pod_m3u + e["url"] + "\n\n"
        
os.system("sudo touch podcast_"+sys.argv[2]+".m3u")
os.system("sudo chmod 777 podcast_"+sys.argv[2]+".m3u")
with open("podcast_"+sys.argv[2]+".m3u", "w") as f_m3u:
    f_m3u.write(pod_m3u)
    
    
#os.system("sudo cp *.m3u /var/lib/mpd/playlists/")
#os.system("mpc clear; mpc load podcast_*; mpc play")