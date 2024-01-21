import re
import requests

# reguar expresions

str1 = "Pentru a comanda pizza sunati la 0755523165"

r = re.findall(r'[0-9]{10}', str1)
print(r)
# [a-z] - alfabet format din

"parsare"
# "parse" w/ regex

r = requests.get('https://www.sport.ro/')

with open("exemplu.html", "wb") as f:
    f.write(r.content)

urls = re.findall(r'http[s]*://[a-z0-9:\.]+/', r.text)

un_set = set(urls)

for elem in un_set:
    print(elem)

text = "\n".join(un_set)

with open("exemplu.html", "w") as f:
    f.write(text)
