def banner(a):
    return a.upper()

ok=int(input("Mitu korda soovite reklaamlauset kuvada?"))
lause=input("Sisestage reklaamlauset kuvada?")

for i in range(ok):
    print(banner(lause))