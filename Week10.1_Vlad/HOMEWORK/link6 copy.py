import requests
import re

# De la urmatoarele linkuri, salvati pozele cu dimensiunea cea mai mica
# https://www.chilieathonita.ro/2023/07/26/lucratori-la-secerisul-domnului-sf-paisie-sf-constantin-brancoveanu-ps-varlaam-ploiesteanul-video-fotoreportaj/


URL = "https://www.chilieathonita.ro/2023/07/26/lucratori-la-secerisul-domnului-sf-paisie-sf-constantin-brancoveanu-ps-varlaam-ploiesteanul-video-fotoreportaj/"

# https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image017-2.jpg 1620w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image017-2-300x200.jpg 300w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image017-2-1024x683.jpg 1024w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image017-2-768x512.jpg 768w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image017-2-1536x1024.jpg 1536w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image017-2-113x75.jpg 113w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image017-2-480x320.jpg 480w


response = requests.get(URL).text


# with open("Week10.1_Vlad/HOMEWORK/pagina.html", 'wb') as f:
#     f.write(response.content)


pattern = re.compile(
    r'(https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image[0-9]+\-2.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image[0-9]+\-2[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image[0-9]+\-2[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image[0-9]+\-2[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image[0-9]+\-2[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image[0-9]+\-2[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2023/07/Image[0-9]+\-2[0-9x\-?]+.jpg [0-9]+w)')

# rezultate = re.finditer(pattern, response)
rezultate = pattern.finditer(response)


rezultat_final = [match.group() for match in rezultate]

final_list = [item.split(",") for item in rezultat_final]


new_list = [[item.strip().split(" ") for item in elem]
            for elem in final_list]

lista_link = []

ultima_lista = [
    [[link[0], link[1].replace('w', '')] for link in line] for line in new_list]


for elem in ultima_lista:
    min_elem = int(elem[0][1])
    lista_provizorie = [elem[0][0]]
    for i in range(len(elem)):
        if int(elem[i][1]) < min_elem:
            min_elem = int(elem[i][1])
            lista_provizorie.append(elem[i][0])
    lista_link.append(lista_provizorie[-1])


for elem in lista_link:
    print(elem)
    r = requests.get(elem)
    with open(f'week10.1_Vlad/HOMEWORK/Link6/{elem[-21:]}', 'wb') as f:
        f.write(r.content)
