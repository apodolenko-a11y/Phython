fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []
aasta= int(input("Palun sisestage, millise aasta andmeid vajate:"))
for rida in fail:
    vastuvõetud.append(int(rida))

print(vastuvõetud[aasta-2011])
fail.close()
