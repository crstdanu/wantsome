import datetime as dt
import os

lista_date = []
with open("Week9.1_Paul\pgadmin.log") as f:
    for line in f.readlines():
        lista_date.append(line[:19])


# now = dt.datetime.now()
# str_now = now.strftime("%d-%m-%Y %H:%M:%S")
# dt_now = dt.datetime.strptime(str_now, "%d-%m-%Y %H:%M:%S")

# inceput = lista_finala[0]
# sfarsit = lista_finala[-1]
# # print(inceput)
# dt_inceput = dt.datetime.strptime(inceput, "%d.%m.%Y %H:%M:%S")
# dt_sfarsit = dt.datetime.strptime(sfarsit, "%d.%m.%Y %H:%M:%S")

# timedelta = dt_sfarsit - dt_inceput
# print(timedelta.seconds)


for i in range(len(lista_date[:-1])):
    time_inceput = dt.datetime.strptime(lista_date[i], "%d.%m.%Y %H:%M:%S")
    time_sfarsit = dt.datetime.strptime(lista_date[i+1], "%d.%m.%Y %H:%M:%S")
    diferenta = time_sfarsit - time_inceput
    print(diferenta.seconds)
