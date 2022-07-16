from collections import Counter
from audioop import add

file = open(r".\istanbul_data\islenmis_istanbul_data.txt","r", encoding = "utf-8")
lines = file.readlines()

my_list = []
for line in lines:
    add_word = [a for a in line.split(' ') if not a.isdigit() and len(a) > 1]
    my_list.extend(add_word)

count_dict = dict(Counter(my_list))
print(count_dict)