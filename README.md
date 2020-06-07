# Radio Manager for Moode

Scripts allow the bulk management of user radio stations. The radio browser functionality pulls from the Community Radio Browser API to allow users to bulk import raw station playlists into their RADIO directory. Provides a powerful radio focused API for IoT useage at http://moode/radio

Todo:
- Bulk deletion of user stations
- Add the posibility to make Moode a local FM over IP server with rtl_fm_streamer

```
$ cd ~/
$ git clone https://github.com/duracell80/MoodeRadio-Get.git
$ cd MoodeRadio-Get/scripts/make-radio-manager/

$ sudo chmod 755 install.sh
$ ./install.sh
```

## Accessing the UI
Go to http://moode/radio to access the community browser and radio options. There are two huge buttons there to access the supercool radio management in Moode UI.

## Navigating the Community Radio Browser UI
Browse through a list of tags clicking the plus icon next to each selection you wish to make. Clicking or tapping a tag name will start playing the stations in that tag as a preview of what's in that tag. The station range field controls how many stations to return. Adding to the station network field searches the API for stations with those keywords in their names, like somafm. When done hit save. The tag file is cached so from time to time refresh that json file from the UI leave the page and come back.

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
