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
     
    packDB          = "u-" + packD3 + "-" + packBASE
    packFILE        = packBASE + "-" + packD1 + "-" + packD2 + "-" + packD3
    
    
    print("\n\n" + packFILE.upper() + " will shortly be removed from the _Network radio folder ..." )
    time.sleep(2)
    
    
    print("\n[Uninstall - "+packFILE.upper()+" : Playlists]")
    os.system("sudo rm -rf /var/lib/mpd/playlists/"+packFILE+".m3u")
    os.system("sudo rm -rf /var/lib/mpd/music/RADIO/_Stations/"+packD1+"/"+packD2+"/"+packD3)
    
    print("[Uninstall - "+packFILE.upper()+" : Logos]")
    os.system("sudo rm -f /var/local/www/imagesw/radio-logos/thumbs/"+packFILE+".jpg")
    
    if packSCANNER == "true":
        os.system("sudo cp ./logos/ /var/local/www/imagesw/radio-logos/thumbs/scanner-"+packD1+"-"+packD2+"-"+packD3+".jpg")
    
    
    
    # CLEAR ANY EXISTING STATIONS IN THIS PACK FROM THE DATABASE
    print("[Uninstall - "+packDB.upper()+" : Database Entries]")
    defconn = create_connection(database)
    with defconn:
        station_id = delete_stations(defconn, packDB)
    
    time.sleep(1)
    print("\n\n[Uninstall - "+packFILE.upper()+" : DONE]\n\n\n")
    
    os.system("mpc update")
 
 
if __name__ == '__main__':
    main()
