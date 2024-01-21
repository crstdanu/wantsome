import requests
import re

# De la urmatoarele linkuri, salvati pozele cu dimensiunea cea mai mica
# https://www.chilieathonita.ro/2022/10/15/acoperamantul-maicii-domnului-video-fotoreportaj/


# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058.jpg 1620w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-300x200.jpg 300w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-1024x683.jpg 1024w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-768x512.jpg 768w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-1536x1024.jpg 1536w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-219x146.jpg 219w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-50x33.jpg 50w,
# https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-113x75.jpg 113w


URL = "https://www.chilieathonita.ro/2022/10/15/acoperamantul-maicii-domnului-video-fotoreportaj/"

response = requests.get(URL).text


pattern = re.compile(
    r'(https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w), (https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image[0-9]+[0-9x\-?]+.jpg [0-9]+w)')

# rezultate = re.finditer(pattern, response)
rezultate = pattern.finditer(response)

# aici transform din obiecte in text
lista_rezultate = [match.group() for match in rezultate]

# aici impart fiecare rand in link-uri de genul [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-113x75.jpg 113w]
final_list = [item.split(",") for item in lista_rezultate]

# impart elementele de la pasul precedent in doua elemente: [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-113x75.jpg, 113w]
new_list = [[item.strip().split(" ") for item in elem] for elem in final_list]


# aici scap de w-ul de la final: [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-113x75.jpg, 113]
ultima_lista = [
    [[link[0], link[1].replace('w', '')] for link in line] for line in new_list]


# [[https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058.jpg, 1620],
# [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-300x200.jpg, 300],
# [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-1024x683.jpg, 1024],
# [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-768x512.jpg, 768],
# [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-1536x1024.jpg, 1536],
# [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-219x146.jpg, 219],
# [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-50x33.jpg, 50],
# [https://chilieathonita.b-cdn.net/wp-content/uploads/2022/10/Image058-113x75.jpg, 113]]


lista_link = []
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
    with open(f'week10.1_Vlad/HOMEWORK/Link1/{elem[-18:]}', 'wb') as f:
        f.write(r.content)
