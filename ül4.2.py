def mahlapakkide_arv(ounad):
    mahlapakkid =round(ounad*0.4/3)
    
    
    return mahlapakkid


ounad=float(input("sisestage õunte kogus kilogrammides:"))

print(mahlapakkide_arv(ounad))