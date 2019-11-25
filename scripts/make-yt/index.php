<?php

//$header     = "#EXTM3U\n";
//$meta       = "#EXTINF:-1, YouTube Audio Stream \n";
//$boot       = "http://localhost/yt-play/?src=0";
$src        = $_GET["src"];


if($src == "0"){
    $runcmd = "sudo /var/www/yt-play/playlist_clear.sh ";
    shell_exec($runcmd);
    echo("YouTube Playlist Cleared");

}elseif($src == "1"){
    $runcmd = "sudo /var/www/yt-play/playlist_start.sh " . $src;
    shell_exec($runcmd);
    echo("YouTube Playlist Started");

} else {
    $runcmd = "sudo /var/www/yt-play/playlist_load.sh " . $src;
    shell_exec($runcmd);
    echo("YouTube Playlist Updated");
}


?>
