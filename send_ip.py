#!usr/bin/env python
#! -*- utf-8 -*-

# Send Public API using any email
# Anything other than gmail, change mail.json configuration

import json, smptlib, urllib2, base64
from emial.meme.text import MIMEext

def mail_ip(language):
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

    # get public IP
    server = server + ':' port # Concatenate server and port
    ip = extract_public_ip() 
    msg = data['language'][language]['message'] + ip

    #structure mail
    mime_message = MIMEText(msg, 'plain')
    mime_message['From'] = sender
    mime_message['To'] = receiver
    mime_message['Subject'] = data['language'][language]['subject']

    #send mail
    server = smptlib.SMTP(server)
    server.starttls()
    server.login(user, pwd)
    server.sendmail(sender, receiver.split(','), mime_message.as_string())
	server.quit()    

def extract_ip():
	# Extract public IP with external web server
	sock = urllib2.urlopen('http://checkip.dyndns.com/')
	public_ip = sock.read()
	sock.close()
	public_ip = public_ip.split(': ')[-1]
	public_ip = public_ip.split('</body>')[0]
	return public_ip

if __name__ == "__main__":
	LANGUAGE = 'en' # set desire language from config
	mail_ip(LANGUAGE)