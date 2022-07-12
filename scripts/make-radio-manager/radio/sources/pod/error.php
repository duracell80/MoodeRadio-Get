<?php 
$src = $_GET["src"];
?>

<html>
<head>
    <title>Podcast Error</title>
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
            opacity             : 1 !important;
        }
        
        .cmd-msg a,
        .cmd-msg a:hover,
        .cmd-msg a:active,
        .cmd-msg a:visited { color : #fff !important; text-decoration: none;}
        
        .mbox {
            width : 50%; margin : 0 auto; border: 1px solid #fff;
        }
                
                
    </style>
</head>
<body>
    <div class="cmd-msg">
      <div class="mbox">
        <div style="padding: 30px;">
            <h3>Podcast Error</h3>
            <p>There seems to be an issue with the parsing of that podcast feed. Please file a bug report at <a href="https://github.com/gpodder/podcastparser">github.com/gpodder/podcastparser</a> for the feed: <?=$src?></p>
        </div>
      </div>
    </div>
</body>
</html>