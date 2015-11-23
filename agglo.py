import requests
from pprint import pprint
from urllib.parse import urlparse
import os.path
#import os
#import re

#To be upgraded later with some file-parsing function
url="http://localhost/i.jpg"
#End of URL


def url_filename(url):
	"""
	Parse URL to return the url_filename
	:url: URL to be parsed
	:return: Filename
	"""
	return urlparse(url).path.replace("/","")

def file_dsize(headers):
	"""
	Return the size of the distant file, based on HTTP headers
	:headers: HTTP Headers from requests.get
	:return: size in bytes
	"""
	return int(r.headers['Content-Length'])

def file_lsize(path):
	"""
	Return the size of the local file. 
	Would be upgraded to have another path
	::
	:return: size in bytes
	"""
	return(os.path.getsize(path))


r=requests.get(url)
path=url_filename(url)

dsize=file_dsize(r.headers)
lsize=file_lsize(path)

pprint(dsize==lsize)

#r=requests.get("http://localhost/i.jpg",
#	headers={'Range': 'bytes=4000-8000'}, stream=True)

#pattern='([0-9]+)-([0-9]+)/([0-9]+)'

#comp=re.compile(pattern)

#result=comp.search(istring)

#print(result)

#if result==None:
#	print("Mismatch")
#else :
#	print(result.group(3))
#size=int(r.headers['Content-Length'])

#test=r.headers['Content-Range']

#match=re.match('^b',test).span

#pprint(size)
#pprint(test)
#pprint(match)

#i=1

#with open('i.jpg',mode='wb') as f:
#	for chunk in r.iter_content(chunk_size=4096):
#		f.write(chunk)
#		pprint(i)
#		i=i+1
#		pprint(os.path.getsize("i.jpg"))