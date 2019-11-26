# MoodeRadio-Get
Package Manager for Moode Audio Radio Stations

Documentation TBD while functionality being finalzed


# YT Play API

Install the api to the localhost from the make-yt directory by
```
$ sudo chmod 755 ./install.sh
$ sudo ./install.sh
```

Add youtube videos to a playlist in the Radio folder in this way ... Compose a file with the first stream as a message that appears in Moode's player. This will give a sense that things are still happening while the API contacts YouTube to get the json file of the video. Add the actual stream you want to play on the next two lines. The API is a proxy running on localhost that uses youtube-dl to do this magic.

End the M3U file with a refrence to http://localhost/yt-play/?type=stream&src=1 which will trigger an mpc update and play the "YouTube Play" playlist. You should use localhost or 127.0.0.1 here in the M3u file.

```
#EXTM3U
#EXTINF:-1, Gentle Whispering ASMR ... Fetching, Please Wait
http://localhost/yt-play/?type=stream&src=-1

#EXTINF:-1, Gentle Whispering ASMR - Cleansing Crystals with Sage 
http://localhost/yt-play/?type=stream&src=Hc0MJjcZm40

#EXTINF:-1, Gentle Whispering ASMR ... Done, Go to Playlists > YouTube_Play
http://localhost/yt-play/?type=stream&src=1
```

# Regenerating Expired Streams
The "YouTube Play" playlist will expire so lists will need to be "regenerated" to activate the .m4a streams!

```
Regenerate and play a crafted playlist from the RADIO folder ...
http://moode.ip/yt-play/?type=regen&src=_Networks/yt/asmr/example.m3u
```

```
Regenerate Suzanne Vega into "YouTube Load" playlist
http://moode.ip/yt-play/?type=regen
```

# Send YouTube Audio to Moode (work in progress)

```
Cast Tom's Diner into "YouTube Play" playlist
http://moode.ip/yt-play/?type=stream&src=L9x-DENKIts

Start the "YouTube Play" playlist via api or Clear/Play from Moode UI
http://moode.ip/yt-play/?type=stream&src=1

```

# Get info about a video
For example Tom's Diner ...

```http://moode.ip/yt-play/?type=info&src=L9x-DENKIts```


# YT Play MPC Commands

There are some nice MPC commands in the API these are ...

```
SEEK FORWARD
fwd15s,30s,60s and 5m
http://moode.ip/yt-play/?cmd=fwd30

SEEK BACK
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
