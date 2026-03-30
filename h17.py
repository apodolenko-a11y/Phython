import os

tehingute_arv = 0
pos_tehingute_arv = 0
pos_tehingute_summa = 0

with open("pangakonto.txt") as file:
    for rida in file:
        tehingute_arv+=1
    if float(rida.strip()) > 0:
            pos_tehingute_arv+=1
            pos_tehingute_summa+=float(rida.strip())
            print(rida.strip())
            
print(f"Tehingute arv: {tehingute_arv}")
print(f"Pos.tehingute arv: {pos_tehingute_arv}")
print(f"Pos. tehingute summa: {pos_tehingute_summa: .2f}")
            
