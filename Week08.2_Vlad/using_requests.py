# https://www.chilieathonita.ro/2022/04/24/lumina-pacii-fotoreportaj-de-la-paste/

import re
import requests

url = "https://www.chilieathonita.ro/2022/04/24/lumina-pacii-fotoreportaj-de-la-paste/"


r = requests.get(url)

with open("pagina.html", "wb") as f:
    f.write(r.content)
