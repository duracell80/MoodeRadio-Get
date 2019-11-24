import os, time, json

def create_playlists(filename):
    
    print("Creating playlists from: \n" + filename.upper() + "\n\n")
    
    with open(filename) as f:
        lines = f.readlines()
    
    time.sleep(2)
    
    count = 0    
    for line in lines:
        
        if "EXTINF:-1" in line:
            count       = count +1
            lineJump    = int(lines.index(line)+1)
            
            if count < 10:
                zeropre = "00"
            else:
                zeropre = "0"
            
            ssplit          = line.split(",")
            stationName     = ssplit[1]
            stationFileM3U  = zeropre+str(count)+ "-" + ssplit[1].strip().replace(" ", "-").lower() + ".m3u"
            stationFilePLS  = zeropre+str(count)+ "-" + ssplit[1].strip().replace(" ", "-").lower() + ".pls"
            stationEcho     = "[ " + zeropre+str(count)+ " ] : " + stationName.strip()
            stationURL      = lines[lineJump]

            print(stationEcho)
            
            # CREATE THE M3U LISTS
            f = open("./playlists/m3u/" + stationFileM3U, "w")
            f.write("#EXTM3U\n\n"+line+stationURL)
            f.close()
            
            time.sleep(0.10)
            
            # CREATE THE PLS LISTS
            f = open("./playlists/pls/" + stationFilePLS, "w")
            f.write("[playlist]\nFile1="+stationURL+"\n"+"Title1="+stationName+"\nNumberOfEntries=1\nLength1=-1\nVersion=1")
            f.close()
            
            time.sleep(0.10)
            
            
    
    print("\n\n[Playlists: DONE]\n\n")
    
 
def main():
    
    with open('config.json') as json_file:
        data = json.load(json_file)
        for p in data['radiopack']:
            packBASE        = p['type'].lower()
            packCOUNTRY     = p['country'].lower()
            packSTATE       = p['state'].lower()
            packID          = p['cityid'].lower()

    
    packDB          = "u-" + packID
    packFILE        = packBASE + "-" + packCOUNTRY + "-" + packSTATE + "-" + packID + ".m3u"
    

    os.system("sudo mkdir -p ./playlists/m3u") 
    os.system("sudo mkdir -p ./playlists/pls") 
    
    create_playlists(packFILE)
        
 
        
 
 
if __name__ == '__main__':
    main()
