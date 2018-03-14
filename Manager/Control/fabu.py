import requests
import json
# r = requests.get("http://127.0.0.1:6800/listversions.json?project=Mstx_Spider")
r = requests.post("http://127.0.0.1:6800/delproject.json", data={"project":"Mstx_Spider"})
print(r.text)
