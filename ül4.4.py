def tervitus(number):

    print ('Võõrustaja: "Tere!"')
    print ("Täna",number,". kord tervitada,mõtiskleb võõrustaja.")
    print('Külaline:"Tere,suur tänu kutse eest!"')
    
külaliste_arv= int(input("sisestage külaliste arv: "))

for i in range(1, külaliste_arv + 1):
    tervitus(i)