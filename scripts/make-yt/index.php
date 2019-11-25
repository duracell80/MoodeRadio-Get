<?php

//playlist_clear     : "http://localhost/yt-play/?src=0";
//playlist_load      : "http://localhost/yt-play/?src=videoid";
//playlist_start     : "http://localhost/yt-play/?src=1";
//playlist_dl        : "http://localhost/yt-play/?dl=1&src=videoid";

$src        = $_GET["src"];
$dl         = $_GET["dl"];



if($dl == "1"){
    $runcmd = "sudo /var/www/yt-play/yt-dl.sh $src";
    shell_exec($runcmd);
    echo("YouTube Audio Downloaded"); 
} else {
    

    switch ($src) {

        // CLEAR PLAYLIST
        case "0":
            $runcmd = "sudo /var/www/yt-play/playlist_clear.sh ";
            shell_exec($runcmd);
            echo("YouTube Playlist Cleared");

        // PLAY PLAYLIST 
        case "1":
            $runcmd = "sudo /var/www/yt-play/playlist_start.sh " . $src;
            shell_exec($runcmd);
            echo("YouTube Playlist Started");

        // DOWNLOAD 140
        case "2":
            $runcmd = "sudo /var/www/yt-play/yt-dl.sh " . $src;
            //shell_exec($runcmd);
            echo("YouTube Audio Downloaded to /var/lib/mpd/music/SDCARD/YT");


        default:
            $runcmd = "sudo /var/www/yt-play/playlist_load.sh " . $src;
            shell_exec($runcmd);
            echo("YouTube Playlist Updated");
    }

}


?>
