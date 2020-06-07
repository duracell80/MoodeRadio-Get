# Radio Manager for Moode 6.4 and 6.5

Scripts allow the bulk management of user radio stations. The radio browser functionality pulls from the Community Radio Browser API to allow users to bulk import raw station playlists into their RADIO directory. Provides a powerful radio focused API for IoT at http://moode/radio

Todo:
- Bulk deletion of user stations
- Enhanced Meta data support
- Drag and drop station import/export for enhanced and easier UX
- Add the posibility to make Moode a local FM over IP server with rtl_fm_streamer

```
$ cd ~/
$ git clone https://github.com/duracell80/MoodeRadio-Get.git
$ cd MoodeRadio-Get/scripts/make-radio-manager/

$ sudo chmod 755 install.sh
$ ./install.sh
```

### API

```
Play the first default station
http://moode/radio?ch=1

Play a radio URL direct
http://moode/radio?type=cast&src=http://ice1.somafm.com/bootliquor-128-aac

Play a radio genre from the community database of tags
http://moode/radio?type=tag&play=ambient

Play a podcast feed via an MPD playlist
http://moode/radio/sources/pod?type=podcast&src=https://www.spreaker.com/show/3287246/episodes/feed&items=20&name=skynews

```

## Accessing the UI
Go to http://moode/radio to access the community browser and radio options. There are two huge buttons there to access the supercool radio management in Moode UI.

![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/radio-feature-index.png)

## Navigating the Radio Options UI
There are some really nice things in the radio options screen (http://moode/rdo-config.php) such as bulk adding of user defined stations, exporting user stations to the SDCARD and importing user stations from the SDCARD. Ask in the Moode forum how to access Moode's network file share folders. There is the ability to hide the inbuilt default stations.


### Import / Export
The biggest advantage is a simple way to export and import stations via a zip file when upgrading your Moode installation. The file must be called stations.zip and located in your SDCARD folder. Ask in the Moode forums how to access your Moode folders via network file shares. Drag / Drop is planned as a future enhancement to ease this process further and avoid the need to know about Samba shares.

![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/radio-user-stations.png)

### Bulk Addition and Logo Management
To use the bulk add feature, add your station names and url's first. Whereas the original add form only lets you add one station at a time the bulk add form here allows for the addition of multiple URL's by use of the +1 link to increase the number of form fields available. If you don't have radio logos ready at the time of addition you can of course add them later, this is an enhancement over the existing Moode station management in that you could only add logos once and only at the time of addition.

![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/radio-user-stations-logos.png)


### Station Shortcuts and Bookmarks
The station lineups are simply reading from the Moode Radio DB by index and allow you to drag and drop "chicklets" to your web browsers bookmarks folder. In this way you can start playing a radio station using browser bookmarks without needing to call up the Moode UI and find your station. It's simply calling http://moode/radio?ch=1 for example. Additonally your bookmarks will NEVER get stale. If a URL is updated by Moode, the URL in the bookmark is totally independent of an actual radio stream. Which is pretty darn cool !!

![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/radio-moode-lineup.png)


### Basic Podcast Player
Using the playlist ability of MPD along with a Python library the podcast feature can turn an XML feed into an M3U file. Go to http://moode/radio and install the podcastparser library. Reboot just to make sure then return to http://moode/radio with your XML Feed. Enter the feed into the box, add a name for your podcast and how many episodes you wish to stream. The podcasts are not downloaded so you may run this with a 4GB sdcard. "Playing" the last item in the playlist will trigger the refreshing of the feed to grab the latest episodes if any are there.


### Future Plans
Bulk deletion of user stations via checkbox selection, it's a no brainer.

FM Radio Server. There exists a streamer that turns a local FM station obtained via the SDR compatible DVB-T dongles into a feed playable over the local network. This means you could for example use Moode as a radio server to listen to local radio as an online radio stream either on the same device via a playlist file or another device using VLC or a browser. Try it out by running the install-streamer.sh from here https://github.com/duracell80/RTLUtils. 



## Navigating the Community Radio Browser UI
The CRB is a cool tool in that stations are collated via community. It means you could discover a station long before the likes of TuneIn add it, if they ever would. Browse through a list of tags clicking the plus icon next to each selection you wish to make. Clicking or tapping a tag name will start playing the stations in that tag as a preview of what's in that tag. The station range field controls how many stations to return (this cuts down on useless and less useful tags). Adding to the station network field searches the API for stations with those keywords in their names, like somafm. When done hit save. The tag file is cached so from time to time refresh that json file from the UI leave the page and come back.

Station URL's are maintained by the community, some URL's may not work and this is not a malfunction of the scripts. Add new stations to the community browser and participate in maintaing the database of stations here:
http://www.radio-browser.info/gui/#!/add


![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/001.png)



Navigate to the RADIO section of the UI into the new "Underscore Stations" folder where you'll see tags and networks.

![Screenshot](https://raw.githubusercontent.com/duracell80/MoodeRadio-Get/master/scripts/make-radio-manager/002.png)

## Optionally

Add these lines to /var/www/templates/lib-config.html
```
<legend>Radio Sources</legend>
<a href="rdo-config-rb.php"><button class="btn btn-medium btn-primary">Radio Browser</button></a>&nbsp;<a href="rdo-config.php"><button class="btn btn-medium btn-primary">Radio Options</button></a>
<span id="info-rescanrdodb" class="help-block-configs help-block-margin">
Radio Station lookup service provided by <a href="http://www.radio-browser.info" target="_blank">Community Radio Browser</a><br>
</span>
<p></p>
```



## To Uninstall
```
$ cd /home/pi/MoodeRadio-Get/scripts/make-radio-manager/
$ sudo chmod 755 uninstall.sh
$ ./uninstall.sh
```
