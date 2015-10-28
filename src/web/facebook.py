import facebook
import json

ACCESS_TOKEN = ''

# A helper function to pretty print Python objects as json

def pp(o):
  print json.dumps(o, indent=1)

# Create a connection to the graph API with your acces token

g = facebook.GraphAPI(ACCESS_TOKEN)

print '--------------'
print 'Me'
print '--------------'
pp(g.get_object('me'))
print
print '--------------'
print 'My friends'
print '--------------'
pp(g.get_connections('me', 'friends'))
print
print '--------------'
print 'Social Web'
print '--------------'
pp(g.request("search", {'q' : 'social web', 'type' : 'page'}))


