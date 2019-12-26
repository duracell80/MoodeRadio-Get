#!/usr/bin/env python2
import urllib, random, requests, json, os

def is_ascii(text):
    if isinstance(text, unicode):
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode('ascii')
        except UnicodeDecodeError:
            return False
    return True

cmd_path        = "/var/www/radio"

pi_path         = "/var/lib/mpd/music/RADIO/_Stations"
web_path        = cmd_path + "/sources/rb"
cfg_file        = cmd_path + "/sources/config.json"
api_path        = ["https://de1.api.radio-browser.info",
                   "https://de2.api.radio-browser.info",
                   "https://fr1.api.radio-browser.info",
                   "https://nl1.api.radio-browser.info"]


f_server        = random.choice(api_path)
f_response      = urllib.urlopen("{0}/json/tags".format(f_server)).read()
f_json          = json.loads(f_response)






# CACHE TAG FILE FOR LOCAL UI RENDER
c_filename = web_path + "/tags.json"
if not os.path.exists(c_filename):
    os.system("sudo touch " + c_filename)
    os.system("sudo chmod 777 " + c_filename)
    with open(c_filename, "w") as c_file:
        c_file.write(f_response)
    
else:    
    with open(c_filename, "w") as c_file:
        c_file.write(f_response)
    


os.system("sudo mkdir -p "  + pi_path + "/networks")
os.system("sudo mkdir -p "  + pi_path + "/tags")


with open(cfg_file) as json_file:
    config = json.load(json_file)
    for p in config['radiobrowser']:   
        p_range     = p['range']
        p_tags      = p['tags'].lower().replace("&", "and").replace(" ", "-").replace("'", "-")
        p_stations  = p['stations'].lower()


r_range     = p_range.split("-")        
r_tags      = p_tags.split(",")
r_stations  = p_stations.split(",")
f_path      = pi_path   + "/tags/*.m3u"
s_path      = pi_path   + "/networks/*.m3u"


# REMOVE STATIONS AND TAGS TO REGEN
os.system("sudo rm -rf "    + f_path)
os.system("sudo rm -rf "    + s_path)

# DO TAGS
for f, f_item in enumerate(f_json): 
    
    f_tag   = f_item['name']
    f_cnt   = f_item['stationcount']
    f_range = range(int(r_range[0]),int(r_range[1]))
    
    
    if f_tag in r_tags:
            
        if f_cnt in f_range and is_ascii(f_tag):
            print("Tag: {0} ({1})".format(f_tag, str(f_cnt))) 


            f_folder    = f_tag.lower().replace("&", "and").replace(" ", "-").replace("'", "-")
            f_path      = pi_path   + "/tags/"+ f_folder
            p_path      = f_path    + "/source_community.m3u"


            os.system("sudo mkdir -p "  + f_path)
            os.system("sudo chmod 777 " + f_path)
            os.system("sudo rm -rf "    + p_path)

            p_url   = "{0}/m3u/stations/bytag/{1}".format(f_server, f_tag)  
            p_file  = requests.get(p_url)



            os.system("sudo touch " + p_path)
            os.system("sudo chmod 777 " + p_path)
            open(p_path, 'wb').write(p_file.content)
        
            os.system("sudo sed -i 's/EXTINF:1/EXTINF:-1/g' " + p_path)

        
        
        
        
        
        
        
# DO STATION NAME LOOKUP
for n_item in r_stations:
    n_url   = "{0}/json/stations/byname/{1}".format(f_server, n_item)
    n_json  = json.loads(urllib.urlopen(n_url).read())
    n_url   = "{0}/m3u/stations/byname/{1}".format(f_server, n_item)

    
    
    if "url" in str(n_json):
        n_file      = requests.get(n_url)     
        f_path      = pi_path   + "/networks/"
        p_path      = f_path    + n_item.lower().replace("&", "and").replace(" ", "-").replace("'", "-") +".m3u"

        print("Station: {0}".format(n_item)) 

        os.system("sudo touch " + p_path)
        os.system("sudo chmod 777 " + p_path)
        open(p_path, 'wb').write(n_file.content)

        os.system("sudo sed -i 's/EXTINF:1/EXTINF:-1/g' " + p_path)
        
        
        
        
        
        
        
        
        
        
#os.system("mpc update")