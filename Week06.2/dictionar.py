

def get_students(fisier):
    raw_dict = {}
    with open(fisier) as f:
        for line in f:
            key, value = line.split(":")
            raw_dict[key.strip()] = value.strip()

    final_dict = {key: value for key,
                  value in raw_dict.items() if value.isnumeric()}
    return final_dict


def scholarship(dictionar, percent=30):
    sorted_dict = dict(
        sorted(dictionar.items(), key=lambda x: x[1], reverse=True))

    lista_nume = [key for key in sorted_dict]
    best_students = lista_nume[:int(len(sorted_dict)*percent/100)]
    return best_students


output_dictionary = get_students("week6.2/lista_medii.txt")

bursieri = scholarship(output_dictionary)

for item in bursieri:
    print(f"{bursieri.index(item)+1}. {item}")
