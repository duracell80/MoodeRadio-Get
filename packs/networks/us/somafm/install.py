import os, time, json

import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn


def delete_stations(conn, packDB):
    
    # delete all stations in this pack to prevent duplicates
    
   
    sql = 'DELETE from cfg_radio WHERE type ="'+packDB+'"'
    cur = conn.cursor()
    cur.execute(sql)
    
   
    return cur.lastrowid




def create_station(conn, station):
    
    sql = ''' INSERT INTO cfg_radio(station,name,type,logo)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, station)
    
    # copy the station logo to /var/www/images/radio-logos
    # os.system("sudo cp ./logos/moode-generic.jpg /var/www/images/radio-logos/'"+station[1]+".jpg'")
    
    return cur.lastrowid


    
    
 
def main():
    database        = r"/var/local/www/db/moode-sqlite3.db"
    
    with open('config.json') as json_file:
        data = json.load(json_file)
        for p in data['radiopack']:
            packBASE        = p['type']
            packCOUNTRY     = p['country']
            packID          = p['networkid']
            packVERSION     = p['version']
            packAUTHOR      = p['author']
    
    packDB          = "u-" + packID
    packFILE        = packBASE + "-" + packCOUNTRY + "-" + packID + ".m3u"

    
    
    print("\n\n" + packID.upper() + " will shortly be installed to the _Network radio folder ..." )
    time.sleep(2)
    
    # CREATE THE SEPERATE SINGLE PLAYLISTS FROM THE MASTER M3U
    os.system("sudo python ./playlists.py") 
    
    # CLEAR ANY EXISTING STATIONS IN THIS PACK FROM THE DATABASE
    defconn = create_connection(database)
    with defconn:
        station_id = delete_stations(defconn, packDB)
    
    
    # UPDATE THE DATABASE
    print("Adding to Station Database from: \n" + packFILE.upper() + "\n\n")

    with open(packFILE) as f:
        lines = f.readlines()

    for line in lines:

        if "EXTINF:-1" in line:

            lineJump        = int(lines.index(line)+1)

            ssplit          = line.split(",")
            stationName     = ssplit[1].strip();
            stationURL      = lines[lineJump].strip();


            # CREATE THE DB ENTRY
            conn = create_connection(database)
            with conn:
            
                station      = (stationURL, stationName, packDB, 'local')
                station_id   = create_station(conn, station)

                
                
            stationEcho         = "[ " + str(station_id)+ " ] : " + stationName

            print(stationEcho)
            time.sleep(0.10)

    
    
    
    
    
    
    time.sleep(2)
    os.system("sudo mkdir -p /var/lib/mpd/music/RADIO/_Networks/"+packCOUNTRY+"/"+packID+"/playlists/") 
    time.sleep(2)
    
    os.system("sudo cp ./"+packBASE+"-"+packCOUNTRY+"-"+packID+".m3u /var/lib/mpd/playlists/")
    os.system("sudo cp ./"+packBASE+"-"+packCOUNTRY+"-"+packID+".m3u /var/lib/mpd/music/RADIO/_Networks/"+packCOUNTRY+"/"+packID+"")
    os.system("sudo cp ./logos/"+packBASE+"-"+packCOUNTRY+"-"+packID+".jpg /var/www/images/radio-logos/thumbs")
    os.system("sudo cp ./playlists/pls/*.pls /var/lib/mpd/music/RADIO/_Networks/"+packCOUNTRY+"/"+packID+"/playlists")
    
    print("\n\n[Installed: "+packID.upper()+"] Location: RADIO/_Networks/"+packBASE+"/"+packCOUNTRY+"/"+packID+"\n\nEnjoy The Music!\n\n\n")
    
    os.system("mpc update")
        
 
        
 
 
if __name__ == '__main__':
    main()
