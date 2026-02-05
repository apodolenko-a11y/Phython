ring = int(input("Sisestage ringide arv: "))
           
porgandid=0

for i in range(2, ring + 1,2):
    porgandid = porgandid + i
    
print("Saadavate porgandite koguarv on",porgandid)