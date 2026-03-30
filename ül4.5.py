fail = open("mündid.txt", encoding="UTF-8")

mündid = []
summa=0

failinimi=input("Sisesta failinimi:")

for rida in fail:
    #mündid.append=(int(rida))
    rida= rida.strip()
    arv = int(rida)
    mündid.append(arv)
    
fail.close()

def pronksikarva_summa(mündid):
    tulemus=0
    
    for i in range(len(mündid)):
        if mündid[i] ==1 or mündid[i]==2 or mündid[i]==5:
            tulemus=tulemus+ mündid[i]
            
    return tulemus



summa=pronksikarva_summa(mündid)

print("Hoiupõrsasse läheb",summa,"senti")
            