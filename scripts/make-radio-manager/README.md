# Bulk Radio Manager for Moode

Scripts pull from the Community Radio Browser API to allow users to bulk import raw station playlists into their RADIO directory.

```
$ cd /home/pi
$ git clone https://github.com/duracell80/MoodeRadio-Get.git
$ cd cd MoodeRadio-Get/scripts/make-radio-manager/

$ sudo chmod 755 install.sh
$ ./install.sh
```

## Accessing the UI without changing core moode UI
Go to http://192.168.2.7/rdo-config.php to access the UI replacing the IP with your Moode IP.

## Navigating the UI

## Optionally
Add these lines to /var/www/lib-config.php

```
// update radio playlists
if (isset($_POST['updaterdo'])) {
	submitJob('updmprdo', '', 'Radio update started...', '');
}
```

Add these lines to /var/www/templates/lib-config.html
```
<legend>Radio Sources</legend>
<a href="rdo-config.php"><button class="btn btn-medium btn-primary">Radio Options</button></a>&nbsp;
<span id="info-rescanrdodb" class="help-block-configs help-block-margin">
Radio Station lookup service provided by <a href="http://www.radio-browser.info" target="_blank">Community Radio Browser</a><br>
</span>
<p></p>
```
