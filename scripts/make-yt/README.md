# YT Play API

Why is this useful? Why would you want only audio and not video? Well ... video uses a lot of data, there are some videos also that just have a static image and are essentially audio tracks. Things like 4 hours of Thunderstorms. I dunno it's whatever you want to listen to, you could use this for TedTalks, Poetry, 6 hours of Chillstep. Using this API you can keep playlists of YouTube content and you can listen directly from Moode as if they were radio stations.

Install the api to the localhost from the make-yt directory by
```
$ cd /home/pi/MoodeRadio-Get/scripts/make-yt/
$ sudo chmod 755 ./install.sh
$ sudo ./install.sh
```

The install script will fetch dependencies. Use the API inside playlists to activate audio streams. Use the API in your mobile device browser or desktop browser to interact with Moode. Essentially though you should be able to add YouTube to Moode using only playlists.

Add individual YouTube videos to a playlist in the Radio folder in this way ...

## Example Moode Playlist ...

```
#EXTM3U
#EXTINF:-1, Gentle Whispering ASMR ... Fetching, Please Wait
http://localhost/yt-play/?type=stream&src=-1

#EXTINF:-1, Gentle Whispering ASMR - Cleansing Crystals with Sage 
http://localhost/yt-play/?type=stream&src=https://www.youtube.com/watch?v=Hc0MJjcZm40

#EXTINF:-1, Gentle Whispering ASMR ... Done, Go to Playlists > YouTube_Play
http://localhost/yt-play/?type=stream&src=1
```

Save your YouTube M3U playlists in the RADIO folder when you want to listen to them, load them as if they were radio stations with Clear/Play from the menu.


## Cast Individual YouTube Videos (?type=cast)
Trigger generating the audio directly from a desktop or tablet/phone browser, clearing the current playlist and playing the file as soon as it's ready! An API call to essentially cast audio to Moode from YouTube.

```
Cast a Tiny Desk stream by Sylvan Esso into "YouTube Play" playlist
http://moode.ip/yt-play/?type=cast&src=https://www.youtube.com/watch?v=mhyD2qchkEw

```

## Cast A Whole YouTube Playlist (?type=list)
Send a whole YouTube Playlist from your PC/Laptop/Phone browser to Moode ... Find a playlist for example:

```
Beatiful Calm Acoustics
https://www.youtube.com/watch?v=eWnaD0dvkVM&list=PLKK4T0Fm7nwGEZUZtQn7hbciVbN6hkVFl
```
Copy the ID in the list= section and do this ...
```
http://moode.ip/yt-play/?type=info&src=PLKK4T0Fm7nwGEZUZtQn7hbciVbN6hkVFl
```

If you want to build "Moode playlists" of these URL's (M3U files) you can, it's totally up to you. If you don't see any point in collecting these playlists keep using the above method to cast. If you don't see the point of any of this then this functionality isn't for you and that's ok. Otherwise there is an example playlist called yt-example-list.m3u in the folder: RADIO/YouTube/mahogany. Copy it and change it to your needs.

It's as easy as this:
```
#EXTM3U

#EXTINF:-1, Mahogany Sessions ... Contacting YouTube, Please Wait
http://localhost/yt-play/?type=list&src=PLKK4T0Fm7nwGEZUZtQn7hbciVbN6hkVFl
```
To play it find it in the Radio tab in Moode UI and then do Clear/Play as if it were a Radio station.


## Get info about a video (?type=info)
For example see Tom's Diner JSON ...

```http://moode.ip/yt-play/?type=info&src=https://www.youtube.com/watch?v=L9x-DENKIts```



## Regenerating Streams (?type=regen)
The "YouTube_Play" playlist will expire so streams in it will need to be "regenerated". This is why there is a slight delay in which you may think the functionality isn't working. Just Clear/Play on the list in the RADIO section that you want to relisten to, or you can do this from a PC/Laptop/Phone browser ...

```
Regenerate and play a crafted playlist from the RADIO folder ...
http://moode.ip/yt-play/?type=regen&src=_YouTube/asmr/example.m3u

Regenerate Suzanne Vega into "YouTube Load" playlist
http://moode.ip/yt-play/?type=regen
```



## YT Play MPC Commands(?cmd=)

There are some nice MPC commands in the API these are ...
(replace moode.ip with your moode's lan addr)

```
SEEK FORWARD
fwd15s,30s,60s and 5m
http://moode.ip/yt-play/?cmd=fwd30

SEEK BACK (may not work for streams)
bck15s,30s,60s and 5m
http://moode.ip/yt-play/?cmd=bck5m


mpc status         : http://moode.ip/yt-play/?cmd=status
mpc update         : http://moode.ip/yt-play/?cmd=update
mpc lsplaylists    : http://moode.ip/yt-play/?cmd=list
mpc stop           : http://moode.ip/yt-play/?cmd=stop
mpc play           : http://moode.ip/yt-play/?cmd=play
mpc pause          : http://moode.ip/yt-play/?cmd=pause
mpc prev           : http://moode.ip/yt-play/?cmd=prev
mpc next           : http://moode.ip/yt-play/?cmd=next
```
