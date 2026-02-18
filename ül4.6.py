def kuu_nimi(kuu):
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    return kuud[kuu -1]

def kuupaev_sonena(kuupaev):
    paev=kuupaev[:2]
    kuu = int(kuupaev[3:5])
    aasta = kuupaev[6:]
    
    kuu_n = kuu_nimi(kuu)
    
    return paev+"." + kuu_n + " " + aasta +".a"

sisend = input ("Sisesta kuupäev kujul DD.MM.YYYY: ")
print(kuupaev_sonena(sisend))
    