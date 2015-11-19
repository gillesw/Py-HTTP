import requests
from pprint import pprint

#r=requests.get("https://github.com/braoru/Kibana/archive/master.zip")
r=requests.get("https://github.com/braoru/Kibana/archive/master.zip",
	headers={'Range': 'bytes=4000'}, stream=True)
open('master.zip',mode='wb').write(r.content)
pprint(r.headers)