import re

url = """
hello world
2020-05-11
http://python-engineer.com
https://www.python-engineer.com
http://www.pyeng.net
"""

pattern = re.compile(r"https?://([w]{3}.)?([a-zA-Z0-9-]+)\.([a-z]+)")
matches = pattern.finditer(url)

for match in matches:
    print(match.group(0))
    print(match.group(1))

subbed_urls = pattern.sub(r"\2\3", url)
print(subbed_urls)
