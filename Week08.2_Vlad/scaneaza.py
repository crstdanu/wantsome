import os
import sys

fisiere = {}


def scaneaza(start_folder):
    for el in os.listdir(start_folder):
        path_full = os.path.join(start_folder, el)
        print(path_full)
        if os.path.isfile(path_full):
            size = os.path.getsize(path_full)
            fisiere[path_full] = size
        else:
            scaneaza(path_full)


# print(sys.argv)
# if len(sys.argv) == 1:
#     print("Am nevoie de folderul destinatie!!!")
#     exit()


folder = "c:\Program Files"
scaneaza(folder)
# for k, v in fisiere.items():
#     print(f"{k}: {v}")
