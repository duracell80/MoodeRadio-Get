# Bulk Radio Manager for Moode

Scripts pull from the Community Radio Browser API to allow users to bulk import raw station playlists into their RADIO directory.

```
$ cd /home/pi
$ git clone https://github.com/duracell80/MoodeRadio-Get.git
$ cd MoodeRadio-Get/scripts/make-radio-manager/

$ sudo chmod 755 install.sh
$ ./install.sh
```

## To Uninstall
```
$ cd ~/MoodeRadio-Get/scripts/make-radio-manager/
$ sudo chmod 755 uninstall.sh
$ ./uninstall.sh
```

## Accessing the UI
Go to http://moode/radio to access the community browser and radio options. There are two huge buttons there to access the supercool radio management in Moode UI. You can also play podcast feeds from this screen but be sure to install the podcast parser first. You can also start playing a radio URL from this screen without having to add it to Moode's user radio list.

## Navigating the Radio Options UI
There are some really nice things in the radio options screen (http://moode/rdo-config.php) such as bulk adding of user defined stations, exporting user stations to the SDCARD and importing user stations to the SDCARD. Ask in the Moode forum how to access Moode's network file share folders. There is the ability to hide the inbuilt default stations if you are using a lot of your own custom stations you can easily trim down the list.

To use the bulk add feature, add your station names and url's first. You will be able to add (and update) your radio logos afterwards. Whereas the original add form only lets you add one station at a time the bulk add form here allows for the addition of multiple URL's by use of the +1 link to increase the number of form fields available. If you don't have radio logos ready you can of course add them later.

The station lineups are simply reading from the Moode Radio DB by index and allow you to drag and drop "chicklets" to your web browsers bookmarks folder. In this way you can start playing a radio station using browser bookmarks without needing to call up the Moode UI and find your station. It's simply calling http://moode/radio?ch=1 for example.

## Navigating the Community Radio Browser UI
Browse through a list of tags clicking the plus icon next to each selection you wish to make. Clicking or tapping a tag name will start playing the stations in that tag as a preview of what's in that tag. The station range field controls how many stations to return. Adding to the station network field searches the API for stations with those keywords in their names, like somafm. When done hit save. The tag file is cached so from time to time refresh that json file from the UI leave the page and come back.

![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/001.png)



Navigate to the RADIO section of the UI into the new "Underscore Stations" folder where you'll see tags and networks.

![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/002.png)
