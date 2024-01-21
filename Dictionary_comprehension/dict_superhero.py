my_dict = {
    "Spider": "photographer",
    "Bat": "philantropist",
    "Wonder Wo": "nurse"
}


new_dict = {(key+"man" if key != "Spider" else "Superman"):
            (val if val != "photographer" else "Journalist")
            for (key, val) in my_dict.items()}

print(my_dict)
print(new_dict)
