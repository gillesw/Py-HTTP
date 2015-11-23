import re

istring='bytes 4000-8000/3022098'

#istring='bytes 4'

pattern='([0-9]+)-([0-9]+)/([0-9]+)'

comp=re.compile(pattern)

result=comp.search(istring)

#print(result)

if result==None:
	print("Mismatch")
else :
	print(result.group(3))
