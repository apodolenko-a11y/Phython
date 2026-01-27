#Ülesanne 11
import turtle
import random
def pikim_sona(list):
    pikimArv = 0
    pikimNimi = ""
    for i in list:
        if len(i) > pikimArv:
            pikimArv = len(i)
            pikimNimi = i
        return pikimNimi
    
def kolm_pikimat_nime(list):
    pikimad = ["Mari","Mario","Marek"]
    if len(list)>2:
        list.sort (key=len, reverse=True)
        return list[0:3]
    else:
        return "list on liiga lühike"
    
def ruut(a):
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
for _ in range(5):
    ruut(100)
    turtle.penup()
    turtle.setpos(random.randint(-500,500),random.randint(-500,500))
    turtle.pendown()
        
        
nimed = ["Mari","Mario","Marek","Indrek","Al","Aleksandra"]
print (pikim_sona(nimed))
print (kolm_pikimat_nime(nimed))
    
    
turtle.done()