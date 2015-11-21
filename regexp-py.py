import re

#istring='bytes 4000-8000/3022098'

istring='bytes 4'

pattern='^bytes'

comp=re.compile(pattern)

result=comp.search(istring)

print(result.group)