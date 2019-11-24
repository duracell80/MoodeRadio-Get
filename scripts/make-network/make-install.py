import os, json

with open('config.json') as json_file:
    data = json.load(json_file)
    for p in data['radiopack']:
        packBASE        = p['type'].lower()
        packCOUNTRY     = p['country'].lower()
        packID          = p['networkid'].lower()


os.system("mkdir -p ../../../packs/"+packBASE+"/"+packCOUNTRY+"/"+packID)
os.system("sudo cp -r ./* ../../../packs/"+packBASE+"/"+packCOUNTRY+"/"+packID)
os.system("sudo rm -r ../../../packs/"+packBASE+"/"+packCOUNTRY+"/"+packID+"/make-install.py")



print("\n\nRadiopack copied to the packs/networks directory.\nEdit the master M3U playlist, then run install.py or playlists.py from there!")

print("\nHINT: From here change to the packs directory 'cd ../../../packs/networks/' \n\n")