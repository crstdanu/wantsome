#Sa se afiseze histograma/frecventele fisierelor care au una din urmatoarele categorii de size
#['G', 'M', 'K']  - [2**30, 2**20, 2**10]
#(100G, 50G), (50G, 10G), (10G, 5G), (5G, 1G), (1G, 100M)
#(100M, 50M), (50M, 10M), (10M, 5M), (5M, 1M), (1M, 100K)
#(100k, 50k), (50k, 10k), (10k, 5k), (5k, 1k), (1k, 100)
#--------------------------------------------------------------
# - fiecare categorie are specific numarul de fisiere si cat ocupa acestea in total {'50M-10M': {145, 12*(2**30)}}
#   - 145 - numarul de fisiere
#   - 12G - total cat ocupa
# informatiile despre fisere, aferente categoriilor de size se vor lista intr-un fiser pe linii separate sau intr-un format de bar-graph/chart
import os
import sys

fisiere = {}

def scaneaza(start_folder):
    for el in os.listdir(start_folder):        
        path_full = os.path.join(start_folder, el)
        if os.path.isfile(path_full):
            size = os.path.getsize(path_full)
            fisiere[path_full] = size        
        else:
            scaneaza(path_full)

print(sys.argv)
if len(sys.argv) == 1:
    print("Am nevoie de folderul destinatie!!!")
    exit()

folder = sys.argv[1]    
scaneaza(folder)
print(fisiere)

