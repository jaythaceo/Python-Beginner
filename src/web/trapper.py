# Trapper is a python script.
# We find the likes of friends.

# Facebook access token
ACCESS_TOKEN = ''

import requests
import json

base_url = 'https://graph.facebook.com/me'

fields = 'id,name,friends.limit(20).fields(likes.limit(20))'

url = '%s?fields=%s&access_token=%s' % \
(base_url, fields, ACCESS_TOKEN,)

print url

content = requests.get(url).json()

print json.dumps(content, indent=1)
