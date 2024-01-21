import requests
import re

# De la urmatoarele linkuri, salvati pozele cu dimensiunea cea mai mica
# https://www.chilieathonita.ro/2022/11/10/hramul-sfantului-dumitru-2022-video-fotoreportaj-ips-amfilohie-de-adrianoupoleos/

# srcset="https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020.jpg 1080w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020-200x300.jpg 200w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020-683x1024.jpg 683w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020-768x1152.jpg 768w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020-1024x1536.jpg 1024w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020-97x146.jpg 97w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020-33x50.jpg 33w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image020-50x75.jpg 50w"

URL = "https://www.chilieathonita.ro/2022/11/10/hramul-sfantului-dumitru-2022-video-fotoreportaj-ips-amfilohie-de-adrianoupoleos/"

response = requests.get(URL).text


# with open("Week10.1_Vlad/pagina.html", 'wb') as f:
#     f.write(response.content)


pattern = re.compile(
    r'srcset="(https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/11/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w)"')

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
    with open(f'week10.1_Vlad/HOMEWORK/Link2/{elem[-18:]}', 'wb') as f:
        f.write(r.content)
