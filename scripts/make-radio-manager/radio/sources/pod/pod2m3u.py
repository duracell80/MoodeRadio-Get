import sys, os, urllib, requests, json, podcastparser
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')






# GET feed of podcast else set default
try:
    feedurl = sys.argv[1]
except IndexError as e:
    # Skynews Daily Podcast by Default
    feedurl = "https://www.spreaker.com/show/3287246/episodes/feed"
else:
    r = requests.get(feedurl)
    feedstatus = str(r.status_code)

# CHECK ALL IS OK WITHOUT 404
if "404" in feedstatus:
    print("Feed not found")
    sys.exit()
else:    
    
    
    
    
    
    
    # GET name of podcast else set default
    try:
        pod_name = sys.argv[2]
    except IndexError as e:
        pod_name = "default"    


    # GET name of podcast else set default
    try:
        pod_items = sys.argv[3]
    except IndexError as e:
        pod_items = 5






    # GET the dictonary object from Podcastparser    
    try:
        data = podcastparser.parse(feedurl, urllib.urlopen(feedurl), int(pod_items))
    except podcastparser.FeedParseError:
        print("Podcast Parser Error: Please file a bug report at github.com/gpodder/podcastparser")
        sys.exit()
    
    
    
    
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


    # CHECK for cover art
    if "http" in data["cover_url"]:
        pod_art = data["cover_url"]


    # PARSE each episode
    for s in data["episodes"]:
        pod_date    = datetime.fromtimestamp(s["published"])
        pod_m3u     = pod_m3u + "#EXTINF:"+ str(s["total_time"])+ "," + pod_title + " - " + pod_date.strftime(pod_timeformat) + " - " + s["title"] + "\n"

        for e in s["enclosures"]:
            pod_m3u = pod_m3u + e["url"] + "\n\n"







    # WRITE last item to call back to API to check for more episodes
    pod_m3u = pod_m3u + "#EXTINF:-1,"+ pod_title + " - Check For Latest "+pod_items+" Episodes\n"
    pod_m3u = pod_m3u + "http://localhost:80/radio/sources/pod/?type=podcast&src="+feedurl+"&name="+pod_name+"&items="+pod_items+"&interlude=1"

    # SET file
    os.system("sudo mkdir -p /var/lib/mpd/music/RADIO/_Podcasts")
    os.system("sudo touch podcast_"+pod_name+".m3u")
    os.system("sudo chmod 777 podcast_"+pod_name+".m3u")
    with open("podcast_"+pod_name+".m3u", "w") as f_m3u:
        f_m3u.write(pod_m3u)

    os.system("sudo touch podcast_"+pod_name+".json")
    os.system("sudo chmod 777 podcast_"+pod_name+".json")    
    with open("podcast_"+pod_name+".json", "w") as f_json:
        f_json.write(str(json.dumps(data, indent=4)))

    # GET cover art
    r = requests.get(pod_art)
    os.system("sudo touch /var/www/images/radio-logos/podcast_"+pod_name+".jpg")
    os.system("sudo chmod 777 /var/www/images/radio-logos/podcast_"+pod_name+".jpg")
    with open("/var/www/images/radio-logos/podcast_"+pod_name+".jpg", "wb") as f:
        f.write(r.content)       


    # COPY files
    os.system("sudo cp -f /var/www/images/radio-logos/podcast_"+pod_name+".jpg /var/www/images/radio-logos/thumbs/") 
    os.system("sudo cp -f *.m3u /var/lib/mpd/playlists/")
    os.system("sudo cp -f *.m3u /var/lib/mpd/music/RADIO/_Podcasts/")

    # UPDATE MPD, clear, load and play
    # os.system("mpc update")
    # os.system("mpc stop; mpc clear; mpc load podcast_"+pod_name+"; mpc play")