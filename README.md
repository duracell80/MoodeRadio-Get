# MoodeRadio-Get
Package Manager for Moode Audio Radio Stations

![Screenshot](https://github.com/duracell80/MoodeRadio-Get/blob/master/packs/images/000.jpg?raw=true)

## Get from GIT

```
$ cd /home/pi/
$ git clone https://github.com/duracell80/MoodeRadio-Get.git
$ cd MoodeRadio-Get/
```

```
$ chmod 775 ./scripts/make-stations/assets/*
$ chmod 775 ./scripts/make-stations/build/*
$ chmod 775 ./scripts/make-stations/*

$ cd /home/pi/MoodeRadio-Get/scripts/make-stations/
```

## Find the config.json file and edit the details.

For cities ...

```
type	= stations
pack-d1 = country
pack-d2 = state
pack-d3 = airport code

To store in _Stations/us/tn/bna
```

For genres ...

```
type	= stations
pack-d1 = genres
pack-d2 = electronic
pack-d3 = chill

To store in _Stations/genres/electronic/chill
```

Do this before running the build script as doing so beforehand will make sure you have all the right  filenames in your build. In this example we're going to compile a package for /us/tn/bna. Don't worry about adding the URLs in the m3u file at this point, the script is going to place all these  files in an accessible location in the SDCARD directory. When done with the config do:

```
$ sudo python build.py
$ cd /mnt/SDCARD/_Stations (or open the fileshare)
```

# Add your station URLs and station logos
Edit the m3u files to add your URLs in the file. Add your station logos following the filenaming 

convention stations-us-tn-bna.jpg for example so the names match up. When done make sure you are on 

the SDCARD for example ...

cd /mnt/SDCARD/_Stations/us/tn/bna


### To install all stations to Moode from a radio pack

```$ sudo python import.py```

This will run through the pack you just made inserting all the needed entries into the database, copying the station logos to the right place, adding your playlist to the mpd/playlists directory and adding the given structure in the RADIO section in Moode UI. If you selected the split option in the config.json the script will also spit out seperate playlist files so you can add only one station if needed. If the auxlist option was set to true you'll get a special "scanner playlist" meant for non radio sources like ATC scanners.

### To delete all stations in a pack
From the same location this script will pull your stations out of Moode and Moode Database but keep them on the SDCARD

```$ sudo python delete.py ```

# To share a pack
The export script in a pack will compress the pack for easier sharing with other users / backing up.

```$ sudo python export.py```

### Extra config options
The 'installed' configuration option is where you have the MoodeRadio-Get directory from git. Typically this is in /home/pi. 'split' in the config file will split the master playlist file into seperate station files. The auxlist will allow for a secondary playlist which in the case of city based packs is useful for scanner audio sources such as the airport and authority radio scanners.

# YT Play API

See the readme in the make-yt directory. Install the api to the localhost from that subdir by
```
$ sudo chmod 755 ./install.sh
$ sudo ./install.sh
```
