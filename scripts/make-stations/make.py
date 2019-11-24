import json, os


# Add structure of radio pack here form example the following will create RADIO/_Networks/us/somafm
# packAUTHOR      = "@githubUser"
# packVERSION     = "1.0.0"
# packBASE        = "stations"
# packCOUNTRY     = "us"
# packCITY        = "San Francisco"
# packID          = "somafm"
# packDESC        = """ Optional description"""




packAUTHOR      = "@username"
packVERSION     = "1.0.0"
packBASE        = "stations"
packCOUNTRY     = "us"
packSTATE       = "ca"
packID          = "sfo"
packCITY        = "Planet Radio"
packDESC        = """This is a generic radiopack.  You could edit the radiopack here before copying it to the packs/stations directory or you could go ahead and use 'sudo python make-install.py' from ./generic to copy it as is. Make sure you edit config.json file, rename the pack from being named 'generic' and add your stations to the .m3u playlist file. From there run 'sudo python install.py' to create the playlists and folders in Moode. But make sure you change the name of the pack to from generic! This is just a template."""


































data = {}
data['radiopack'] = []
data['radiopack'].append({
    'version': packVERSION.lower(),
    'author': packAUTHOR.lower(),
    'country': packCOUNTRY.lower(),
    'state': packSTATE.lower(),
    'cityid': packID.lower(),
    'city': packCITY,
    'type': packBASE.lower(),
    'description': packDESC.strip().replace('\n', '').replace('\r', '')
})

os.system("sudo mkdir -p "+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower())

with open(packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+'/config.json', 'w') as outfile:
    json.dump(data, outfile)
    
# Generate The Pack
os.system("sudo mkdir -p "+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower())
os.system("sudo mkdir -p "+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/playlists/m3u")
os.system("sudo mkdir -p "+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/playlists/pls")
os.system("sudo mkdir -p "+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/logos")

# stations
os.system("sudo cp ./generic-master-playlist.m3u ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/"+packBASE+"-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".m3u")

# scanners
os.system("sudo cp ./generic-scanner-playlist.m3u ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/scanner-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".m3u")


os.system("sudo cp ./install.py ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/install.py")
os.system("sudo cp ./make-install.py ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/make-install.py")
os.system("sudo cp ./uninstall.py ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/uninstall.py")
os.system("sudo cp ./playlists.py ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/playlists.py")

# station collection logo
os.system("sudo cp ./generic-logo.jpg ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/logos/"+packBASE+"-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".jpg")

# scanner collection logo
os.system("sudo cp ./generic-scanner-logo.jpg ./"+packCOUNTRY.lower()+"/"+packSTATE.lower()+"/"+packID.lower()+"/logos/scanner-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".jpg")


print("\n\n"+ packDESC.strip().replace('\n', '').replace('\r', '') + "\n\n" + "Change into the created pack with 'cd us/ca/sfo' to see what was just created!\n\n")
