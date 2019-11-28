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
    
    # delete all stations in this pack
    sql = 'DELETE from cfg_radio WHERE type ="'+packDB+'"'
    cur = conn.cursor()
    cur.execute(sql)
    
   
    return cur.lastrowid


    
    
 
def main():
    database        = r"/var/local/www/db/moode-sqlite3.db"
    
    with open('config.json') as json_file:
        data = json.load(json_file)
        for p in data['radiopack']:
            packBASE        = p['type'].lower()
            packCOUNTRY     = p['country'].lower()
            packSTATE       = p['state'].lower()
            packID          = p['cityid'].lower()

    
    packDB          = "u-" + packID
    packFILE        = packBASE + "-" + packCOUNTRY + "-" + packSTATE + "-" + packID + ".m3u"
    
    
    print("\n\n" + packID.upper() + " will shortly be removed from the _Network radio folder ..." )
    time.sleep(2)
    
    
    print("\n[Uninstall - "+packID.upper()+" : Playlists]")
    os.system("sudo rm /var/lib/mpd/playlists/scanner-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".m3u")
    os.system("sudo rm /var/lib/mpd/playlists/stations-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".m3u")
    os.system("sudo rm /var/lib/mpd/music/RADIO/_Stations/"+packCOUNTRY+"/"+packSTATE+"/"+packID+"/stations-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".m3u")
    os.system("sudo rm /var/lib/mpd/music/RADIO/_Stations/"+packCOUNTRY+"/"+packSTATE+"/"+packID+"/playlists/*.pls")
    os.system("sudo rm -rf /var/lib/mpd/music/RADIO/_Stations/"+packCOUNTRY+"/"+packSTATE+"/"+packID+"/playlists/")
    os.system("sudo rm -rf /var/lib/mpd/music/RADIO/_Stations/"+packCOUNTRY+"/"+packSTATE+"/"+packID)
    
    print("[Uninstall - "+packID.upper()+" : Logos]")
    os.system("sudo rm /var/www/images/radio-logos/thumbs/stations-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".jpg")
    os.system("sudo rm /var/www/images/radio-logos/thumbs/scanner-"+packCOUNTRY+"-"+packSTATE+"-"+packID+".jpg")
    
    
    
    # CLEAR ANY EXISTING STATIONS IN THIS PACK FROM THE DATABASE
    print("[Uninstall - "+packID.upper()+" : Database Entries]")
    defconn = create_connection(database)
    with defconn:
        station_id = delete_stations(defconn, packDB)
    
    time.sleep(1)
    print("\n\n[Uninstall - "+packID.upper()+" : DONE]\n\n\n")
    
    os.system("mpc update")
 
 
if __name__ == '__main__':
    main()
