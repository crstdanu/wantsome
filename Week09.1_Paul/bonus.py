import requests
from xml.etree import ElementTree
import json
import xmltodict

URL1 = "https://data.gov.ro/datastore/dump/05359691-964d-4f82-87d7-bce1df66812e?format=xml"
URL2 = "https://data.gov.ro/datastore/dump/05359691-964d-4f82-87d7-bce1df66812e?format=json"


response1 = requests.get(URL1)
response2 = requests.get(URL2)


data = ElementTree.fromstring(response1.text)


def xml_to_dict(element):
    result = {}
    for child in element:
        if child:
            # Recursively convert child elements to dictionaries
            child_dict = xml_to_dict(child)
            if child.tag in result:
                if isinstance(result[child.tag], list):
                    result[child.tag].append(child_dict)
                else:
                    result[child.tag] = [result[child.tag], child_dict]
            else:
                result[child.tag] = child_dict
        else:
            result[child.tag] = child.text
    return result


my_dict = xml_to_dict(data)


data1 = xmltodict.parse(response1.text)


data2 = response2.json()

print(data2['records'][0])
print(data1['data']['row'][0])


# data2['records'][0] == list(data1['data']['row'][0].values())

lookup_dict = {"_".join(map(str, elem)): True for elem in data2['records']}

# for elem in data2['records'][0]:
# lookup_list.append("_".join(map(str, elem)))
# "1_Arges_Burnesti_111"
# set(data2['records'][0])
# "1_Arges_Burnesti_111"

for elem in data1['data']['row']:
    # lookup_key = "_".join(elem.values())
    lookup_key = f"{elem['@_id']}_{elem['Judet']}_{elem['Localitate']}_{elem['Codpostal']}"
    if not lookup_dict.pop(lookup_key, False):
        print(f"{lookup_key} nu se afla in fisierul json")

for key in lookup_dict:
    print(f"{key} nu se gaseste in fisierul xml")
