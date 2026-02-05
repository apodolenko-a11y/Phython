from datetime import*
fail=open("nimekiri.txt" , encoding ="UTF-8")

failinimi=input("Sistestage failinimi: ")
arv=1
for rida in fail:
    if arv == datetime.now().day:
        print(rida,end="")
    arv=arv+1    
         
         
fail.close()