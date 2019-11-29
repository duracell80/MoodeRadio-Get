import json, os


# Add structure of radio pack here form example the following will create RADIO/_Networks/us/somafm
with open("config.json") as json_file:
    config = json.load(json_file)
    for p in config['radiopack']:   
        packBASE        = p['type'].lower()
        packSCANNER     = p['auxlist'].lower()
        packINSTALLED   = p['installed']
        packSPLITLIST   = p['split'].lower()
        packD1          = p['pack-d1'].lower()
        packD2          = p['pack-d2'].lower()
        packD3          = p['pack-d3'].lower()
   

        
# Directories
pathFILE    = packD1+"-"+packD2+"-"+packD3
pathBASE    = packD1+"/"+packD2+"/"+packD3
pathSCRIPTS = packINSTALLED+"/MoodeRadio-Get/scripts/make"

    
exec(open(pathSCRIPTS+"-stations/build/uninstall.py").read())
os.system("mpc update")