failinimi =input("Sisestage failinimi: ")

fail =open("jukebox.txt" , encoding="UTF-8")

laulud[]
for rida in fail:
    laulud.append(rida.strip())
    
fail.close()

print("Muusikapalade valik:")

for i in range(len(laulud)):
    print(str(i+1) + ".",laulud=(i))
    
valik=int(input("Valige laulu järjekorranumber:"))
arv=1
print(arv)