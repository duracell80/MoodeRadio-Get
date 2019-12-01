#!/usr/bin/env python2
import json
with open('source.json') as f:
    f_json = json.load(f)
    print f_json['_filename']