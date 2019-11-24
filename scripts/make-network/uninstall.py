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
            packBASE        = p['type']
            packCOUNTRY     = p['country']
            packID          = p['networkid']
            packVERSION     = p['version']
            packAUTHOR      = p['author']
    
    packDB          = "u-" + packID
    packFILE        = packBASE + "-" + packCOUNTRY + "-" + packID + ".m3u"
    
    print("\n\n" + packID.upper() + " will shortly be removed from the _Network radio folder ..." )
    time.sleep(2)
    
    
    print("\n[Uninstall - "+packID.upper()+" : Playlists]")
    os.system("sudo rm /var/lib/mpd/playlists/"+packBASE+"-"+packCOUNTRY+"-"+packID+".m3u")
    os.system("sudo rm /var/lib/mpd/music/RADIO/_Networks/"+packCOUNTRY+"/"+packID+"/"+packBASE+"-"+packCOUNTRY+"-"+packID+".m3u")
    os.system("sudo rm /var/lib/mpd/music/RADIO/_Networks/"+packCOUNTRY+"/"+packID+"/playlists/*.pls")
    os.system("sudo rm -rf /var/lib/mpd/music/RADIO/_Networks/"+packCOUNTRY+"/"+packID+"/playlists/")
    os.system("sudo rm -rf /var/lib/mpd/music/RADIO/_Networks/"+packCOUNTRY+"/"+packID)
    
    print("[Uninstall - "+packID.upper()+" : Logos]")
    os.system("sudo rm /var/www/images/radio-logos/thumbs/networks-"+packCOUNTRY+"-"+packID+".jpg")
    
    
    
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
