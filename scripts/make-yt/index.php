<?php


/** YT-Play API
  *
  * Lee Jordan @duracell80
  * 11/26/2019

    playlist_clear     : http://localhost/yt-play/?type=stream&src=0
    playlist_load      : http://localhost/yt-play/?type=stream&src=videoid
    playlist_start     : http://localhost/yt-play/?type=stream&src=1
    playlist_regen     : http://localhost/yt-play/?type=regen&src=_Networks/yt/asmr/asmr-short-selection.m3u (lists in RADIO directory)
    playlist_vega      : http://localhost/yt-play/?type=regen (Regenerate The Doctor)


    Download item to /mnt/SDCARD/ as .m4a
    audio_dl           : http://localhost/yt-play/?type=download&src=6LEmDEZVa5g

*/


$cmd        = $_GET["cmd"];
$src        = $_GET["src"];
$type       = $_GET["type"];

$apiPath    = "/var/www/yt-play/";
$playPath   = "/var/lib/mpd/playlists/";
$radioPath  = "/var/lib/mpd/music/RADIO/";   



// THE PLAYLIST BUILDER
if(isset($src) && !empty($src)){
    switch ($src) {

        // CLEAR PLAYLIST ?type=stream&src=0
        case "-1":
            shell_exec("sudo " . $apiPath . "playlist_clear.sh");
            echo("YouTube Playlist Cleared");
            break;

        // PLAY PLAYLIST ?type=stream&src=1
        case "1":
            shell_exec("sudo " . $apiPath . "playlist_start.sh");
            echo("YouTube Playlist Started");
            break;

        // ELSE LOAD SRC TO LIST ?type=stream&src=videoid
        
        default:
            $runcmd = "sudo " . $apiPath . "playlist_load.sh " . $src;
            
            if($type == "stream"){
                shell_exec($runcmd);
                echo("YouTube Playlist Updated");
            }
            break;
    }
}











// SOME AWESOME COMMANDS
if(isset($type) && !empty($type)){
    switch ($type) {
        // INSPECT ?type=info&src=videoid
        case "info":
            $runcmd         = "sudo ".$apiPath."yt-info.sh " . $src;
            $json_string    = shell_exec($runcmd);

            header('Content-type: text/javascript');
            echo(pretty_json($json_string));
            break;



        // DOWNLOAD ?type=dl&src=videoid
        case "download":
            if(isset($src) && !empty($src)){
                $runcmd = "sudo ".$apiPath."yt-dl.sh " . $src;
                shell_exec($runcmd);
                echo("YouTube Audio Downloaded"); 
            } else {
                echo("Failed to Download: Video Source Missing"); 
            }
            break;


        // REGENERATE Playlist or Vega
        case "regen":


            if(isset($src) && !empty($src)){
                // Example ?type=regen&src=_Networks/yt/asmr/asmr-short-selection.m3u
                $runcmd = "sudo cp -f ".$radioPath . $src . " " . $playPath . "YouTube_Load.m3u";
                echo("Playlist was Regenerated");

            } else {
                // Example ?type=regen

                $runcmd = "sudo cp -f " . $apiPath . "yt-init.m3u " .$playPath . "YouTube_Load.m3u";
                echo("Suzanne Vega was Regenerated");
            }
            shell_exec($runcmd);
            shell_exec("sudo " . $apiPath . "playlist_regen.sh");
            break;
            
        
        case "stream":

            break;

        default:

            break;

    }
    
}

















/*  NICE TO HAVE COMMANDS
    mpc status         : http://localhost/yt-play/?cmd=status
    mpc update         : http://localhost/yt-play/?cmd=update
    mpc lsplaylists    : http://localhost/yt-play/?cmd=list
    mpc stop           : http://localhost/yt-play/?cmd=stop
    mpc play           : http://localhost/yt-play/?cmd=play
    mpc pause          : http://localhost/yt-play/?cmd=pause
    mpc prev           : http://localhost/yt-play/?cmd=prev
    mpc next           : http://localhost/yt-play/?cmd=next

    SEEK FORWARD
    fwd15s,30s,60s and 5m
    http://localhost/yt-play/?cmd=fwd30

    SEEK BACK
    bck15s,30s,60s and 5m
    http://localhost/yt-play/?cmd=bck5m
*/



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



/**
 * JSON beautifier
 * @Juan Lago
 */


function pretty_json($json, $ret= "\n", $ind="\t") {

    $beauty_json = '';
    $quote_state = FALSE;
    $level = 0; 

    $json_length = strlen($json);

    for ($i = 0; $i < $json_length; $i++)
    {                               

        $pre = '';
        $suf = '';

        switch ($json[$i])
        {
            case '"':                               
                $quote_state = !$quote_state;                                                           
                break;

            case '[':                                                           
                $level++;               
                break;

            case ']':
                $level--;                   
                $pre = $ret;
                $pre .= str_repeat($ind, $level);       
                break;

            case '{':

                if ($i - 1 >= 0 && $json[$i - 1] != ',')
                {
                    $pre = $ret;
                    $pre .= str_repeat($ind, $level);                       
                }   

                $level++;   
                $suf = $ret;                                                                                                                        
                $suf .= str_repeat($ind, $level);                                                                                                   
                break;

            case ':':
                $suf = ' ';
                break;

            case ',':

                if (!$quote_state)
                {  
                    $suf = $ret;                                                                                                
                    $suf .= str_repeat($ind, $level);
                }
                break;

            case '}':
                $level--;   

            case ']':
                $pre = $ret;
                $pre .= str_repeat($ind, $level);
                break;

        }

        $beauty_json .= $pre.$json[$i].$suf;

    }

    return $beauty_json;

}   

?>
