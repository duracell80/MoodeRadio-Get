<?php
/**
 * moOde audio player (C) 2014 Tim Curtis
 * http://moodeaudio.org
 *
 * This Program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This Program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * 2019-12-24 TC moOde 6.3.0
 * Contrib: Lee Jordan
 */

require_once dirname(__FILE__) . '/inc/playerlib.php';

playerSession('open', '' ,'');



// SAVE BUTTON - THE MAIN ACTION
if (isset($_POST['save']) && $_POST['save'] == '1') {
    
    $_out = "";
    foreach ($_POST['config'] as $key => $value) {
		$_SESSION[$key] = $value;
        $c++;
    }
    $_usrmsg = "<strong>Success: Playlists regenerated in RADIO/_Stations</strong>";
	$_SESSION['notify']['title'] = 'Changes Saved';
    
    
    $filedest       = "/var/lib/mpd/music/RADIO";
    
    for ($x = 0; $x <= $c; $x++) {
        $s_name     = $_SESSION["userstation_".$x."_name"];
        $s_url      = $_SESSION["userstation_".$x."_url"];
    
        $s_content  = "[playlist]\nFile1=" . $s_url . "\nTitle1=" . $s_name . "\nLength1=-1\nNumberOfEntries=1\nVersion=2";
        
        $s_file     = fopen($filedest . "/" . $s_name . ".pls", "w") or die("Unable to open file!");
        fwrite($s_file, $s_content);
        fclose($s_file);
    }
    
    
    
    
    shell_exec("mpc update");
    
} else {
    //$_usrmsg = "<strong>Information: Select Tags</strong><br>Tap a tag name to preview the stations in Moode ...";
    $_consolevis    = "none";
}




// TOGGLE MOODE DEFAULT STATIONS
if (isset($_POST['update_station_hide'])) {
	if (isset($_POST['station_hide'])) {
		$_SESSION['notify']['title'] = $_POST['station_split'] == '1' ? 'Moode stations hidden' : 'Moode stations restored';
		$_SESSION['notify']['duration'] = 3;
        $_station_hide   = $_POST['station_hide'];
        $_SESSION['station_hide'] = $_station_hide;
        
        $_select['toggle_station_hide1'] = "<input type=\"radio\" name=\"station_hide\" id=\"toggle_station_hide0\" value=\"1\" " . (($_POST['station_hide'] == '1') ? "checked=\"checked\"" : "") . ">\n";           
        $_select['toggle_station_hide0'] = "<input type=\"radio\" name=\"station_hide\" id=\"toggle_station_hide1\" value=\"0\" " . (($_POST['station_hide'] == '0') ? "checked=\"checked\"" : "") . ">\n";
        
        
        
        // LOOK UP MOODE STATIONS IN DB ONLY ACTION THESE, LEAVE USER STATIONS ALONE
        $db = new SQLite3('/var/local/www/db/moode-sqlite3.db');
        $results = $db->query('SELECT * FROM cfg_radio WHERE type = "s"');
        
        
        if ($_POST['station_hide'] == '1') {
            while ($row = $results->fetchArray()) {
                
                if($row['logo'] == "local"){
                    
                    // with quotes
                    shell_exec("sudo sudo mv /var/lib/mpd/music/RADIO/'".$row['name'].".pls' /var/www/radio/sources/moode");

                    // with double quotes
                    shell_exec("sudo sudo mv /var/lib/mpd/music/RADIO/\"".$row['name'].".pls\" /var/www/radio/sources/moode");

                    // without
                    shell_exec("sudo sudo mv /var/lib/mpd/music/RADIO/".$row['name'].".pls /var/www/radio/sources/moode");
                } else {
                    // BBC 320kb STATIONS ...
                    $name           = $row['logo'];
                    $name           = str_replace("images/radio-logos/", "", $name);
                    $name           = str_replace(".jpg", "", $name);
                    
                    // with quotes
                    shell_exec("sudo sudo mv /var/lib/mpd/music/RADIO/'".$name.".pls' /var/www/radio/sources/moode");

                    // with double quotes
                    shell_exec("sudo sudo mv /var/lib/mpd/music/RADIO/\"".$name.".pls\" /var/www/radio/sources/moode");

                    // without
                    shell_exec("sudo sudo mv /var/lib/mpd/music/RADIO/".$name.".pls /var/www/radio/sources/moode");    
                }
                
                
                
            }
        } else {
            while ($row = $results->fetchArray()) {
                // Restoring much faster ...
                shell_exec("sudo sudo mv /var/www/radio/sources/moode/*.pls /var/lib/mpd/music/RADIO");
                
                
            }
        }
        shell_exec("mpc update");
        
	}
} else {
    $_select['toggle_station_hide1'] = "<input type=\"radio\" name=\"station_hide\" id=\"toggle_station_hide0\" value=\"1\" " . (($_SESSION['station_hide'] == '1') ? "checked=\"checked\"" : "") . ">\n";          
    $_select['toggle_station_hide0'] = "<input type=\"radio\" name=\"station_hide\" id=\"toggle_station_hide1\" value=\"0\" " . (($_SESSION['station_hide'] == '0') ? "checked=\"checked\"" : "") . ">\n";
}








// BULK UPLOAD USER STATIONS VIA PARSING AN UPLOADED PLAYLIST
if (isset($_POST['update_userstations'])) {
	
    
    
    // upload the file    
    if($_FILES['m3u_file']['size'] > 0){
        
        
        $tempfile       = "/tmp/radio-logos/userstations.m3u";
        $tempdest       = "/var/www/radio/sources/moode";
        // KEEP HOLD OF THE TEMP FILE
        copy($_FILES['m3u_file']['tmp_name'], $tempfile);

        // MOVE THE TEMP FILE INTO LOGO THUMBS
        $runcmd = "sudo mv -f " . $tempfile . " " . $tempdest;
        $_userlogos = shell_exec($runcmd); 
        
        
         
        
        $_SESSION['notify']['title'] = 'Stations imported';
    }
}







session_write_close();



waitWorker(1, 'rdo-config-usr');

$tpl = "rdo-config-usr.html";
$section = basename(__FILE__, '.php');
storeBackLink($section, $tpl);

include('/var/local/www/header.php');
eval("echoTemplate(\"" . getTemplate("templates/$tpl") . "\");");
include('footer.php');
