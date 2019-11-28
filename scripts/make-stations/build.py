import json, os


# Add structure of radio pack here form example the following will create RADIO/_Networks/us/somafm
with open("config.json") as json_file:
    config = json.load(json_file)
    for p in config['radiopack']:   
        packAUTHOR      = p['author'].lower()
        packVERSION     = p['version'].lower()
        packINSTALLED   = p['installed']
        packBASE        = p['type'].lower()
        packSCANNER     = p['auxlist'].lower()
        packCOUNTRY     = p['pack-d1'].lower()
        packSTATE       = p['pack-d2'].lower()
        packID          = p['pack-d3'].lower()
        packCITY        = p['city']
        packDESC        = p['pack-description'].strip().replace('\n', '').replace('\r', '')
        packTIMEZONE    = p['timezone']

        
# Directories
pathFILE    = packCOUNTRY+"-"+packSTATE+"-"+packID
pathBASE    = packCOUNTRY+"/"+packSTATE+"/"+packID
pathBUILD   = "./build/"+pathBASE
pathASSETS  = "./assets/"        

# migrate json
os.system("sudo mkdir -p "+pathBUILD+"/logos")
os.system("sudo cp -f ./config.json "+pathBUILD+"/config.json")

# stations
os.system("sudo cp "+pathASSETS+"generic-stations-playlist.m3u "+pathBUILD+"/"+packBASE+"-"+pathFILE+".m3u")
os.system("sudo cp "+pathASSETS+"generic-logo.jpg "+pathBUILD+"/logos/"+packBASE+"-"+pathFILE+".jpg")
os.system("sudo cp "+pathASSETS+"import.py "+pathBUILD)


# scanner
if packSCANNER == "true":
    os.system("sudo cp "+pathASSETS+"generic-scanner-playlist.m3u "+pathBUILD+"/scanner-"+pathFILE+".m3u")
    os.system("sudo cp "+pathASSETS+"generic-scanner-logo.jpg "+pathBUILD+"/logos/scanner-"+pathFILE+".jpg")











# move the pack files to the SDCARD for user editing of playlist files / sharing the pack with other users
os.system("mkdir -p /mnt/SDCARD/_Stations/"+packCOUNTRY+"/"+packSTATE+"/"+packID)
os.system("sudo cp -rf "+pathBUILD+"/* /mnt/SDCARD/_Stations/"+packCOUNTRY+"/"+packSTATE+"/"+packID)


print("\n\nRadio pack created! \n\nThe pack has been copied to the /mnt/SDCARD/_Stations/"+packCOUNTRY+"/"+packSTATE+"/"+packID+" directory for easier editing. Contained in the pack is a stations playlist to edit, add the needed station urls there. There is also a generic logo for the stations playlist. When done run the install script within the pack to bring the playlists into Moode or choose to zip your pack for sharing with other users. \n")