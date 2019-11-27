# MoodeRadio-Get
Package Manager for Moode Audio Radio Stations

Documentation TBD while functionality being finalzed


# YT Play API

Install the api to the localhost from the make-yt directory by
```
$ sudo chmod 755 ./install.sh
$ sudo ./install.sh
```

Add youtube videos to a playlist in the Radio folder in this way ... Compose a file with the first stream as a message that appears in Moode's player. This will give a sense that things are still happening while the API contacts YouTube to get the json file of the video. Add the actual stream you want to play on the next two lines. The API is a patchwork quilt of a proxy to youtube-dl.

End the M3U file with a call to http://localhost/yt-play/?type=stream&src=1 which will trigger an mpc update and play the "YouTube Play" playlist. You should use localhost or 127.0.0.1 here in the M3U file.

```
#EXTM3U
#EXTINF:-1, Gentle Whispering ASMR ... Fetching, Please Wait
http://localhost/yt-play/?type=stream&src=-1

#EXTINF:-1, Gentle Whispering ASMR - Cleansing Crystals with Sage 
http://localhost/yt-play/?type=stream&src=https://www.youtube.com/watch?v=Hc0MJjcZm40

#EXTINF:-1, Gentle Whispering ASMR ... Done, Go to Playlists > YouTube_Play
http://localhost/yt-play/?type=stream&src=1
```

Save your M3U playlists in the RADIO folder



# Regenerating Expired Streams
The "YouTube Play" playlist will expire so streams will need to be "regenerated" to activate the audio! (replace moode.ip with your moode's lan addr)

```
Regenerate and play a crafted playlist from the RADIO folder ...
http://moode.ip/yt-play/?type=regen&src=_YouTube/asmr/example.m3u
```

```
Regenerate Suzanne Vega into "YouTube Load" playlist
http://moode.ip/yt-play/?type=regen
```

# Get info about a video
For example see Tom's Diner JSON ... (replace moode.ip)

```http://moode.ip/yt-play/?type=info&src=https://www.youtube.com/watch?v=L9x-DENKIts```


# Send YouTube Audio to Moode
Essentially trigger a middle man between a URL and Moode in order to generate the .m4a file.

```
Cast a Tiny Desk stream by Sylvan Esso into "YouTube Play" playlist
http://moode.ip/yt-play/?type=download&src=https://www.youtube.com/watch?v=mhyD2qchkEw

```

# Download with --no-call-home flag
```
Download a Tiny Desk to the uSD Donate to NPR (Lobby ytdl-org for a stream only version)
http://moode.ip/yt-play/?type=download&src=https://www.youtube.com/watch?v=mhyD2qchkEw
```




# YT Play MPC Commands

There are some nice MPC commands in the API these are ...
(replace moode.ip with your moode's lan addr)

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
