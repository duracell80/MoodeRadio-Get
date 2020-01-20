<html>
<head>
    <title>Simple Radio Player</title>
    <style>
        body {
            margin              : 0px;
            padding             : 0px;
            font-size           : 75%;
            font-family         : sans-serif;
            color               : #fff;
            background-color    : rgb(32,32,32);
        }
        
        .cmd-msg {
            opacity             : 0.4;
        }
    </style>
</head>
<body>
<?php


/** Radio-Play API
  *
  * Lee Jordan @duracell80
  * 12/26/2019

    

*/


$cmd        = $_GET["cmd"];
$src        = $_GET["src"];
$play       = $_GET["play"];
$type       = $_GET["type"];





$apiPath    = "/var/www/radio";
$playPath   = "/var/lib/mpd/playlists";
$radioPath  = "/var/lib/mpd/music/RADIO";
$radioFile  = "Radio_Play";
$radioList  = "/var/lib/mpd/playlists/Radio_Play.m3u";






?> <div class="cmd-msg"><?php
switch ($type) {
    case "cast":
        
        // EXAMPLE http://192.168.2.4/radio?type=cast&src=http://ice55.securenetsystems.net/DASH7
        $m3u_content  = "#EXTM3U\n";
        $m3u_content .= "#EXTINF:-1,Cast To Moode Audio\n";
        $m3u_content .= $src;
        
        shell_exec("sudo touch /var/lib/mpd/playlists/Radio_Play.m3u");
        shell_exec("sudo chmod 777 /var/lib/mpd/playlists/Radio_Play.m3u");
        file_put_contents($radioList, $m3u_content); 

        $runcmd = "mpc clear; mpc load Radio_Play"; shell_exec($runcmd);
        $runcmd = "mpc play";
        echo(shell_exec($runcmd));
        
        sleep(2);
        header("Location: /");
        
        
        break;
    
    case "tag":
        $runcmd = "sudo python " . $apiPath . "/sources/rb/rb-tags-preview.py " . $play;
        echo("Previewing radio tag: " . $play);
        shell_exec($runcmd);
        //header("Location: /"); 
        break;
    case "station":
        
        break;
    case "country":
        
        break;
        
    case "mpc":
        if(isset($cmd) && !empty($cmd)){
            switch ($cmd) {

                // UPDATE DATABASE
                case "update":
                    $runcmd = "mpc update";
                    echo(shell_exec($runcmd));
                    break;

                // STATUS
                case "status":
                    $runcmd = "mpc status";
                    echo(shell_exec($runcmd));
                    break;

                // LIST Playlists
                case "list":
                    $runcmd = "mpc lsplaylists";
                    $list   = shell_exec($runcmd); 
                    $playlists = explode("\n", $list);

                    header('Content-type: text/javascript');
                    echo(pretty_json(json_encode($playlists)."\n"));

                    break;

                // STOP
                case "stop":
                    $runcmd = "mpc stop";
                    echo(shell_exec($runcmd));
                    break;

                // PLAY
                case "play":
                    $runcmd = "mpc play";
                    echo(shell_exec($runcmd));
                    break;

                // PAUSE
                case "pause":
                    $runcmd = "mpc pause-if-playing";
                    echo(shell_exec($runcmd));
                    break;

                // PREV
                case "prev":
                    $runcmd = "mpc prev";
                    echo(shell_exec($runcmd));
                    break;

                // NEXT
                case "next":
                    $runcmd = "mpc next";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP FORWARD 15s
                case "fwd15":
                    $runcmd = "mpc seek +15";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP FORWARD 30s
                case "fwd30":
                    $runcmd = "mpc seek +30";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP FORWARD 60s
                case "fwd60":
                    $runcmd = "mpc seek +60";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP FORWARD 5m
                case "fwd5m":
                    $runcmd = "mpc seek +300";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP BACK 15s
                case "bck15":
                    $runcmd = "mpc seek -15";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP BACK 30s
                case "bck30":
                    $runcmd = "mpc seek -30";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP BACK 60s
                case "bck60":
                    $runcmd = "mpc seek -60";
                    echo(shell_exec($runcmd));
                    break;

                // SKIP BACK 5m
                case "bck5m":
                    $runcmd = "mpc seek -300";
                    echo(shell_exec($runcmd));
                    break;




                default:
                    break;
            }
        }
        break;
        
    default:
       break;
}
?></div><?php


















?>
</body>
</html>
