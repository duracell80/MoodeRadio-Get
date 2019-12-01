#!/usr/bin/env python2
import json
with open('source.json') as f:
    f_json = json.load(f)
    
    # Stream 140
    #print f_json['formats'][2]['url']
    
    # Stream 249
    print f_json['formats'][0]['url']
    
    # Stream 250
    # print f_json['formats'][1]['url']
    
    # Stream 251
    # print f_json['formats'][3]['url']