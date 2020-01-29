#!/usr/bin/env python2
import urllib, random, requests, json, os, re, string, unicodedata, sys

import sqlite3
from sqlite3 import Error

reload(sys)
sys.setdefaultencoding('utf-8')





valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
char_limit = 255

def clean_filename(filename, whitelist=valid_filename_chars):
    
    filename = unicode(filename)
    filename = filename.replace("&", "and").replace("'", "-").replace("\"", "").replace("(", "").replace(")", "")
    cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()
    cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename)>char_limit:
        print("Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit))
    
    return cleaned_filename[:char_limit]








cmd_path        = "/var/www/radio"
pi_path         = "/var/lib/mpd/music/RADIO/"
web_path        = cmd_path + "/sources/moode"
p_path          = web_path + "/userstations.m3u"



# SPLIT EACH URL INTO SEPERATE FILE
q_file  = open(p_path, 'r')
q_lines = q_file.readlines()
q_size  = len(q_lines)
q_file.close()


db_file = "/var/local/www/db/moode-sqlite3.db"
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn



def detect_station(conn, station_file):
    # prevent duplicates
    sql = 'SELECT name FROM cfg_radio WHERE type="u" AND name="'+station_file+'"'
    cur = conn.cursor()
    cur.execute(sql)
    sid_found = 0
    row = 0
    rows = cur.fetchall()


    for row in rows:
        if station_file in row[0]:
            sid_found = 1




    return sid_found



def create_station(conn, station):
    sql = ''' INSERT INTO cfg_radio(station,name,type,logo)
          VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, station)
    print station
    return cur.lastrowid


if q_file:
    
    


    # CREATE THE DB ENTRY
    conn    = create_connection(db_file)
    
    for i in range(0,q_size,1):

        if "#EXTINF" in q_lines[i]:
            station_split       = q_lines[i].split("#EXTINF:-1, ")
            station_name        = str(station_split[1])
        if i+1 < q_size:
            if "://" in q_lines[i+1]:
                station_url         = str(q_lines[i+1])
                station_file        = clean_filename(station_name)
                station_path        = pi_path + station_file + ".pls"


                station_content     = "[playlist]\nFile1=" + station_url + "\nTitle=" + station_name + "Length1=-1\n" + "NumberOfEntries=1\nVersion=2"





               
                #s_found = detect_station(conn, station_file)
                s_found = 0
                print s_found
                
                if(s_found == 0):
                    station_name    = station_file.replace('\n', ' ').replace('\r', '')
                    station_url     = station_url.replace('\n', ' ').replace('\r', '')
                    station_data    = (str(station_url), 'station name', 'u', 'local')
                    station_id      = create_station(conn, station_data)
                    print("[ " + str(station_id)+ " ] : " + station_name)
                    open(station_path, 'wb').write(station_content)
                    os.system("sudo chmod 777 '" + station_path + "'")

                else:
                    
                    print("[ Skip ] : " + station_name)
            
            
        
#os.system("mpc update")