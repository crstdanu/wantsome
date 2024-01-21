import re

str1 = "Pentru a comanda pizza sunati la 9876543210, 0743211800 - 0765 681 190, apoi 0731 997 440 ..."
l_rex = [r'07[0-9]{2}\s[0-9]{3}\s[0-9]{3}', r'07[0-9]{8}']
matches = [re.findall(ll, str1) for ll in l_rex]
print(matches)
