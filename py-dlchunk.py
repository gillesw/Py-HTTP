import requests
from pprint import pprint
import os.path
import os

r=requests.get("https://github.com/braoru/Kibana/archive/master.zip",
	headers={'Range': 'bytes=4000-8000'}, stream=True)

size=int(r.headers['Content-Length'])

pprint(size)

i=1

with open('master.zip',mode='wb') as f:
	for chunk in r.iter_content(chunk_size=4096):
		f.write(chunk)
		pprint(i)
		i=i+1
		pprint(os.path.getsize("master.zip"))