<?php 
/** Podcast-Play API
  *
  * Lee Jordan @duracell80
  * 04/27/2020

    

*/


// Main Params
$cmd        = $_GET["cmd"];
$src        = $_GET["src"];
$type       = $_GET["type"];

// Podcast Params
if(isset($_GET["name"]) && !empty($_GET["name"])){ $name = $_GET["name"]; } else { $name = "generic";}
if(isset($_GET["items"]) && !empty($_GET["items"])){ $items = $_GET["items"]; } else { $items = "5";}
if(isset($_GET["interlude"]) && !empty($_GET["interlude"])){ $interlude = $_GET["interlude"]; } else { $interlude = "0";}



$apiPath    = "/var/www/radio/sources/pod";


    switch ($type) {      
    case "podcast":
        if($interlude == "1"){
            // SEND an MP3 Header to Moode rather than a PHP file
            $interlude = "/var/www/radio/sources/pod/interlude.mp3";
            if(file_exists($interlude)) {
                header('Content-Type: audio/mpeg');
                header('Content-Disposition: filename="interlude.mp3"');
                header('Content-length: '.filesize($interlude));
                header('Cache-Control: no-cache');
                header("Content-Transfer-Encoding: chunked"); 

                readfile($interlude);
                
                $runcmd = "python " . $apiPath . "/pod2m3u.py " . $src . " " . $name . " " . $items;
                shell_exec($runcmd);
                
                shell_exec("mpc update");
                shell_exec("mpc stop; mpc clear; mpc load podcast_" . $name . "; mpc play");
                
            } else {
                // MP3 Not Found
                header("HTTP/1.0 404 Not Found");
            }
        } else {
            // EXAMPLE http://192.168.2.4/radio/sources/pod?type=podcast&src=https://www.spreaker.com/show/3287246/episodes/feed&items=5&name=skynews
            $runcmd = "python " . $apiPath . "/pod2m3u.py " . $src . " " . $name . " " . $items;
            $runrst = shell_exec($runcmd);
            if (stripos($runrst, "Podcast Parser Error") !== false) {
                header("Location: /radio/sources/pod/error.php?src=".$src."");
                break;
            } else {
                shell_exec("mpc update");
                shell_exec("mpc stop; mpc clear; mpc load podcast_" . $name . "; mpc play");
                
                header("Location: /");
                break;
            }
        }
        
        break;        
    
    
    case "moode":
        if(isset($cmd) && !empty($cmd)){
            switch ($cmd) {

                // INSTALL Podcast Parser from gpoder
                case "pip-pod":
                    $runcmd = "pip install podcastparser";
                    echo(shell_exec($runcmd));
                    break;

                default:
                    break;
            }
        }    
        
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
?>