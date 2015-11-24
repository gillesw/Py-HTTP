import requests
from pprint import pprint

#r=requests.get("https://github.com/braoru/Kibana/archive/master.zip")
#r=requests.get("http://localhost/i.jpg",
#	headers={'Range': 'bytes=4000-8000'}, stream=True)
r=requests.get("http://localhost/i.jpg")
open('i.jpg',mode='wb').write(r.content)
pprint(r.headers)
