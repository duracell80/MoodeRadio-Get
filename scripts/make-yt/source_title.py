#!/usr/bin/env python2
import json, re
with open('source.json') as f:
    f_json = json.load(f)
    
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    print(emoji_pattern.sub(r'', f_json['fulltitle'])) # no emoji