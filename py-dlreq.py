import requests
from pprint import pprint

r=requests.get("https://github.com/braoru/Kibana/archive/master.zip")

open('master.zip',mode='wb').write(r.content)