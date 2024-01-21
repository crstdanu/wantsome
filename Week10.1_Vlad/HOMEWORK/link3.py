import requests
import re

# De la urmatoarele linkuri, salvati pozele cu dimensiunea cea mai mica
# https://www.chilieathonita.ro/2022/12/07/intrarea-in-biserica-a-maicii-domnului-sarbatoarea-dedicarii-video-fotoreportaj/


# srcset="https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034.jpg 1620w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034-300x200.jpg 300w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034-1024x683.jpg 1024w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034-768x512.jpg 768w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034-1536x1024.jpg 1536w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034-219x146.jpg 219w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034-50x33.jpg 50w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image034-113x75.jpg 113w"

URL = "https://www.chilieathonita.ro/2022/12/07/intrarea-in-biserica-a-maicii-domnului-sarbatoarea-dedicarii-video-fotoreportaj/"

response = requests.get(URL).text


# with open("Week10.1_Vlad/pagina.html", 'wb') as f:
#     f.write(response.content)


pattern = re.compile(
    r'srcset="(https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/12/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w)"')

# rezultate = re.finditer(pattern, response)
rezultate = pattern.finditer(response)


rezultat_final = [match.group() for match in rezultate]
strip_first = [item.replace('srcset="', '') for item in rezultat_final]
strip_second = [item.replace('"', '') for item in strip_first]

final_list = [item.split(",") for item in strip_second]


new_list = [[item.strip().split(" ") for item in elem]
            for elem in final_list]

lista_link = []

ultima_lista = [
    [[link[0], link[1].replace('w', '')] for link in line] for line in new_list]


for elem in ultima_lista:
    min_elem = int(elem[0][1])
    lista_provizorie = []
    for i in range(len(elem)):
        if int(elem[i][1]) < min_elem:
            min_elem = int(elem[i][1])
            lista_provizorie.append(elem[i][0])
    lista_link.append(lista_provizorie[-1])


for elem in lista_link:
    print(elem)
    r = requests.get(elem)
    with open(f'week10.1_Vlad/HOMEWORK/Link3/{elem[-18:]}', 'wb') as f:
        f.write(r.content)
