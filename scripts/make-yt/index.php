<?php

/* YT-Play API
Author  : Lee Jordan @duracell80
Date    : 11/26/2019

playlist_clear     : http://localhost/yt-play/?src=0
playlist_load      : http://localhost/yt-play/?src=videoid
playlist_start     : http://localhost/yt-play/?src=1
audio_dl           : http://localhost/yt-play/?type=dl&src=videoid
*/


$src        = $_GET["src"];
$type       = $_GET["type"];

   

switch ($type) {
    // DOWNLOAD ?type=dl&src=videoid
    case "dl":
        $runcmd = "sudo /var/www/yt-play/yt-dl.sh " . $src;
        shell_exec($runcmd);
        echo("YouTube Audio Downloaded"); 
        break;
        
        
    default:

        switch ($src) {

            // CLEAR PLAYLIST ?src=0
            case "0":
                shell_exec("sudo /var/www/yt-play/playlist_clear.sh");
                echo("YouTube Playlist Cleared");
                break;

            // PLAY PLAYLIST ?src=1
            case "1":
                shell_exec("sudo /var/www/yt-play/playlist_start.sh");
                echo("YouTube Playlist Started");
                break;
                
            // ELSE LOAD SRC TO LIST ?src=videoid
            default:
                $runcmd = "sudo /var/www/yt-play/playlist_load.sh " . $src;
                shell_exec($runcmd);
                echo("YouTube Playlist Updated");
                break;
        }
        
        

}


?>
