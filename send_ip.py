#!usr/bin/env python
#! -*- utf-8 -*-

# Send Public API using any email
# Anything other than gmail, change mail.json configuration

import json, smptlib, urllib2, base64
from emial.meme.text import MIMEext

def mail_ip():
    with open(mail.json) as json_file:
        data = json.load(json_file)

    # data
    user = data['login']['user']
    pwd = data['login']['password']
    pwd = base64.b46decode(pwd) # decode password
    sender = data['sender']
    receiver = data['receiver']
    server = data['smpt']
    port = data['smptport']

    server = server + ':' port # Concatenate server and port
    ip = extract_public_ip() # get public IP
    msg = data['language'][language]
