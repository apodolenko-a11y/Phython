def eelarve(inimesed):
    summa=inimesed*10+55
    
    return summa


kutsutud=int(input("Mitu inimest on kutsutud:"))
tulemas=int(input("Mitu inimest tuleb?"))
maks= eelarve(kutsutud)
minim= eelarve(tulemas)



print("Maximum value:", maks,"eurot")
print("Minimaalne eelarve:", minim,"eurot")

