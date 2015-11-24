import requests
from pprint import pprint
import os.path
import os
import re

r=requests.get("http://localhost/i.jpg",
	headers={'Range': 'bytes=4000-8000'}, stream=True)

size=int(r.headers['Content-Length'])

test=r.headers['Content-Range']

match=re.match('^b',test).span

pprint(size)
pprint(test)
pprint(match)

i=1

with open('i.jpg',mode='wb') as f:
	for chunk in r.iter_content(chunk_size=4096):
		f.write(chunk)
		pprint(i)
		i=i+1
		pprint(os.path.getsize("i.jpg"))