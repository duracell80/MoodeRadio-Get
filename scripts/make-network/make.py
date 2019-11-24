import json, os


# Add structure of radio pack here form example the following will create RADIO/_Networks/us/somafm
# packAUTHOR      = "@githubUser"
# packVERSION     = "1.0.0"
# packBASE        = "networks"
# packCOUNTRY     = "us"
# packCITY        = "San Francisco"
# packID          = "somafm"
# packDESC        = """ Optional description"""




packAUTHOR      = "@username"
packVERSION     = "1.0.0"
packBASE        = "networks"
packCOUNTRY     = "us"
packCITY        = "Planet Radio"
packID          = "generic"
packDESC        = """This is a generic radiopack.  You could edit the radiopack here before copying it to the packs/network directory or you could go ahead and use 'sudo python make-install.py' from ./generic to copy it as is. Make sure you edit config.json file, rename the pack from being named 'generic' and add your stations to the .m3u playlist file. From there run 'sudo python install.py' to create the playlists and folders in Moode. But make sure you change the name of the pack to from generic! This is just a template."""


































data = {}
data['radiopack'] = []
data['radiopack'].append({
    'version': packVERSION.lower(),
    'author': packAUTHOR.lower(),
    'networkid': packID.lower(),
    'country': packCOUNTRY.lower(),
    'city': packCITY,
    'type': packBASE.lower(),
    'networkid': packID.lower(),
    'description': packDESC.strip().replace('\n', '').replace('\r', '')
})

os.system("sudo mkdir -p "+packID.lower())

with open(packID.lower()+'/config.json', 'w') as outfile:
    json.dump(data, outfile)
    
# Generate The Pack
os.system("sudo mkdir -p "+packID.lower())
os.system("sudo mkdir -p "+packID.lower()+"/playlists/m3u")
os.system("sudo mkdir -p "+packID.lower()+"/playlists/pls")
os.system("sudo mkdir -p "+packID.lower()+"/logos")

#os.system("sudo touch "+packID.lower()+"/"+packBASE+"-"+packCOUNTRY+"-"+packID+".m3u")
os.system("sudo cp ./generic-master-playlist.m3u ./"+packID+"/"+packBASE+"-"+packCOUNTRY+"-"+packID+".m3u")


os.system("sudo cp ./install.py ./"+packID+"/install.py")
os.system("sudo cp ./make-install.py ./"+packID+"/make-install.py")
os.system("sudo cp ./uninstall.py ./"+packID+"/uninstall.py")
os.system("sudo cp ./playlists.py ./"+packID+"/playlists.py")

os.system("sudo cp ./generic-logo.jpg ./"+packID+"/logos/"+packBASE+"-"+packCOUNTRY+"-"+packID+".jpg")


print("\n\n"+ packDESC.strip().replace('\n', '').replace('\r', '') + "\n\n" + "Change into the created pack with 'cd generic' to see what was just created!\n\n")
