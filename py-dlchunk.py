import requests
from pprint import pprint
import os.path

r=requests.get("https://github.com/braoru/Kibana/archive/master.zip",stream=True)

open('master.zip',mode='wb').write(r.content)
pprint(int(r.headers['Content-Length']))

i=1

with open('master.zip',mode='wb') as f:
	for chunk in r.iter_content(chunk_size=1024):
		f.write(chunk)
		f.flush
		pprint(i)
		i=i+1
		pprint(os.path.getsize("master.zip"))