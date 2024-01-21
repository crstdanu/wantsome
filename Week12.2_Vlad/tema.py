# 1
# Folosind subprocess, executati comanda "ipconfig /all" si extrageti din output un dictionar de forma
# {
#     "ipconfig": [{
#         "name": "Wireless LAN adapter WiFi",
#         "description": "Intel(R) Dual Band Wireless-AC 8265",
#         "physical_address": "34-41-5D-3A-AB-7E",
#         "ipv4_address": "192.168.111.206"
#     }]
# }
# Veti avea cate un dictionar ca in exemplu pentru fiecare interfata pe care o returneaza comanda


# 2
# Avand o functie care calculeaza daca un numar este patrat perfect,
# calculeaza cate numere sunt patrat perfect intre 1-1000000
# Cronometreaza cat timp se calculeaza fara a folosi nici un thread
# apoi folosind threads (cu 1, 2 apoi 3 thread-uri in paralel, folosind semaphore)
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Jaguar8@",
    database='sql_store'
)

mycursor = db.cursor()


mycursor.execute("SELECT * FROM customers")
