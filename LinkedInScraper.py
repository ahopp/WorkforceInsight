# -*- coding: utf-8 -*-
"""
Self-Assesed Skills Scraper Using the LinkedIn API

@author: Andrew A. Hopp
"""
#Import resources
import oauth2 as oauth
import urlparse
from linkedin import linkedin

#Assign API key data to variables and initialize the OAuth Client (https://developer-programs.linkedin.com/documents/getting-oauth-token-python)

consumer_key           = "75yxwojxsfq5ql"
consumer_secret        = "FZwrAcpxuxSY7JVo"
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

#Get a request token

request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'
resp, content = client.request(request_token_url, "POST")
if resp['status'] != '200':
    raise Exception("Invalid response %s." % resp['status'])
 
request_token = dict(urlparse.parse_qsl(content))

print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
print

authorize_url =      'https://api.linkedin.com/uas/oauth/authorize'
print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
print

accepted = 'n'
while accepted.lower() == 'n':
    accepted = raw_input('Have you authorized me? (y/n) ')
oauth_verifier = raw_input('What is the PIN? ')

access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
token = oauth.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth.Client(consumer, token)
 
resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))