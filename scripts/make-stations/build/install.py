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
    
    print("hello") 
 

    database        = r"/var/local/www/db/moode-sqlite3.db"
    
    packDB          = "u-" + packD3 + "-" + packBASE
    packFILE        = packBASE + "-" + packD1 + "-" + packD2 + "-" + packD3
    pathBUILD       = "/mnt/SDCARD/_Stations/"+packD1+"/"+packD2+"/"+packD3
    
    # CLEAR ANY EXISTING STATIONS IN THIS PACK FROM THE DATABASE
    defconn = create_connection(database)
    with defconn:
        station_id = delete_stations(defconn, packDB)
        
        
        
    # UPDATE THE DATABASE
    print("Adding to Station Database from: \n" + packFILE.upper() + "\n\n")

    with open(pathBUILD + "/" + packFILE + ".m3u") as f:
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
                
                
            print("[ " + str(station_id)+ " ] : " + stationName)
        
        
    # DO FILE SYSTEM STUFF
    os.system("sudo mkdir -p /var/lib/mpd/music/RADIO/_Stations/"+packD1+"/"+packD2+"/"+packD3+"/singles/")
    os.system("sudo cp ./"+packFILE+".m3u /var/lib/mpd/playlists/")
    os.system("sudo cp ./*.m3u /var/lib/mpd/music/RADIO/_Stations/"+packD1+"/"+packD2+"/"+packD3)
    os.system("sudo cp ./singles/pls/*.pls /var/lib/mpd/music/RADIO/_Stations/"+packD1+"/"+packD2+"/"+packD3+"/singles")
    
    os.system("sudo cp ./logos/"+packFILE+".jpg /var/www/images/radio-logos/thumbs")
    
    if packSCANNER == "true":
        os.system("sudo cp ./scanner-"+packD1+"-"+packD2+"-"+packD3+".m3u /var/lib/mpd/music/RADIO/_Stations/"+packD1+"/"+packD2+"/"+packD3+"")
        os.system("sudo cp ./logos/scanner-"+packD1+"-"+packD2+"-"+packD3+".jpg /var/www/images/radio-logos/thumbs")
        
    
 
if __name__ == '__main__':
    main()
