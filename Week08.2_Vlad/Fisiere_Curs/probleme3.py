import requests as req
import re

r = req.get('https://sport.ro')
#with open('pagina.html', 'wb') as f:
#    f.write(r.content)
urls = re.findall(r'http[s]*://[a-z0-9:\.]+/', r.text)
text = "\n".join(list(set(urls)))
with open('urls.txt', 'w') as f:
    f.write(text)

