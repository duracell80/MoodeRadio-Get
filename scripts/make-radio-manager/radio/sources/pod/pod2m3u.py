import sys, os, urllib, requests, podcastparser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')


# Get feed of podcast else set default
try:
    print("Podcast Feed: " + sys.argv[1])
    feedurl = sys.argv[1]
except IndexError as e:
    # Skynews Daily Podcast by Default
    feedurl = "https://www.spreaker.com/show/3287246/episodes/feed"
    
# Get name of podcast else set default
try:
    print("Podcast Playlist Name: podcast_" + sys.argv[2])
    pod_name = sys.argv[2]
except IndexError as e:
    pod_name = "default"    


# Get name of podcast else set default
try:
    print("Podcast Episodes: " + sys.argv[3])
    pod_items = sys.argv[3]
except IndexError as e:
    pod_items = 5


    

    
    
    
data            = podcastparser.parse(feedurl, urllib.urlopen(feedurl), int(pod_items))
pod_title       = data["title"]
pod_timeformat  = "%m/%d/%Y"
pod_m3u         = "#EXTM3U\n"




# Let's do this, metaverse from podcastparser.py ...
# total_time,
# description
# payment_url
# link
# guid
# cover_url
# enclosures:
#    url
#    mime_type,
#    file_size
#    file_size
# description_html
# title
# published
# episode_art_url



if "http" in data["cover_url"]:
    pod_art = data["cover_url"]
    print("Podcast Cover Art: " + pod_art)

    

for s in data["episodes"]:
    
        
    pod_date    = datetime.fromtimestamp(s["published"])
    pod_m3u     = pod_m3u + "#EXTINF:"+ str(s["total_time"])+ "," + pod_title + " - " + pod_date.strftime(pod_timeformat) + " - " + s["title"] + "\n"
    
    for e in s["enclosures"]:
        pod_m3u = pod_m3u + e["url"] + "\n\n"

# SET File        
os.system("sudo touch podcast_"+pod_name+".m3u")
os.system("sudo chmod 777 podcast_"+pod_name+".m3u")
with open("podcast_"+pod_name+".m3u", "w") as f_m3u:
    f_m3u.write(pod_m3u)
    
# GET Cover Art
r = requests.get(pod_art)
os.system("sudo touch /var/www/images/radio-logos/podcast_"+pod_name+".jpg")
os.system("sudo chmod 777 /var/www/images/radio-logos/podcast_"+pod_name+".jpg")
with open("/var/www/images/radio-logos/podcast_"+pod_name+".jpg", "wb") as f:
    f.write(r.content)    

os.system("sudo cp -f /var/www/images/radio-logos/podcast_"+pod_name+".jpg /var/www/images/radio-logos/thumbs/")    
os.system("sudo mkdir -p /var/lib/mpd/music/RADIO/_Podcasts")

# MOVE File
os.system("sudo cp -f *.m3u /var/lib/mpd/playlists/")
os.system("sudo cp -f *.m3u /var/lib/mpd/music/RADIO/_Podcasts/")
os.system("mpc update")
os.system("mpc clear; mpc load podcast_"+pod_name+"; mpc play")