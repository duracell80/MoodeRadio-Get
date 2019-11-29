# YT Play API

Install the api to the localhost from the make-yt directory by
```
$ cd /home/pi/MoodeRadio-Get/scripts/make-yt/
$ sudo chmod 755 ./install.sh
$ sudo ./install.sh
```

The install script will fetch dependencies. Use the API inside playlists to activate audio streams. Use the API in your mobile device browser or desktop browser to interact with Moode. Essentially though you should be able to add YouTube to Moode using only playlists.

Add youtube videos to a playlist in the Radio folder in this way ... Compose a file with the first stream as a message that appears in Moode's player. This will give a sense that things are still happening while the API contacts YouTube to get the json file of the video. Add the actual stream you want to play on the next two lines. End the M3U file with a call to http://localhost/yt-play/?type=stream&src=1 which will trigger an mpc update, offer the chance to output a done message and play the "YouTube Play" playlist. 

You should use localhost or 127.0.0.1 here in the M3U file.

## The magic url format /yt-play/?type=stream&src=

```
#EXTM3U
#EXTINF:-1, Gentle Whispering ASMR ... Fetching, Please Wait
http://localhost/yt-play/?type=stream&src=-1

#EXTINF:-1, Gentle Whispering ASMR - Cleansing Crystals with Sage 
http://localhost/yt-play/?type=stream&src=https://www.youtube.com/watch?v=Hc0MJjcZm40

#EXTINF:-1, Gentle Whispering ASMR ... Done, Go to Playlists > YouTube_Play
http://localhost/yt-play/?type=stream&src=1
```

Save your YouTube M3U playlists in the RADIO folder under _YouTube


## Get info about a video (?type=info)
For example see Tom's Diner JSON ... (replace moode.ip)

```http://moode.ip/yt-play/?type=info&src=https://www.youtube.com/watch?v=L9x-DENKIts```


## Cast YouTube Audio (?type=cast)
Trigger generating the .m4a directly from a desktop or tablet/phone browser, clearing the current playlist and playing the file as soon as it's ready! An API call to essentially cast audio to Moode from YouTube.

```
Cast a Tiny Desk stream by Sylvan Esso into "YouTube Play" playlist
http://moode.ip/yt-play/?type=cast&src=https://www.youtube.com/watch?v=mhyD2qchkEw

```

## Regenerating Streams (?type=regen)
The "YouTube_Play" playlist will expire so streams in it will need to be "regenerated". This is why there is a slight delay in which you may think the functionality isn't working. The API calls the library to recontact YouTube to activate the m4a stream to output a fresh set of URL's in the "YouTube_Play" playlist. The src you give it here is the location of the playlist in the RADIO folder that you want to play.

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
