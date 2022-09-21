import tkinter #naimportujem si plátno
canvas=tkinter.Canvas(height=300,width=300,bg='white') #určím si akú šírku, výšku a farbu pozadia bude mať plátno
canvas.pack() #vytvorím si plátno

zoznam=[] #vytvorím si zoznam
nastupujuci=[0]*8 #vytvorím si zoznam na nastupujúcich ľudí
vystupujuci=[0]*8 #vytvorím si zoznam na vystupujúcich ľudí
zastavky=[None]*8 #vytvorím si zoznam na zástavky
i=0 #premennú i si nastavím na 0
x=50 #premennú x si nastavím na 50
y=25 #premennú y si nastavím na 25
b=10 #premennú b si nastavím na 10

subor=open('vytazenost_autobusovej_linky.txt','r',encoding='UTF-8') #otvorím si daný súbor na čítanie
for riadok in subor: #for cyklus na prechádzanie každého riadku v súbore
    zoznam=riadok.split(' ') #do zoznamu si dám riadok
    zoznam.append(' ') #uložím si ho ako zoznam
    if zoznam[3]!='': #podmienka pokiaľ sa tam nenachádza nič
        zoznam[2]=zoznam[2]+' '+zoznam[3] #do zoznamu si uložím názov zástavky
        zoznam.pop(3) #odstránim si prvok na danej pozícii
    nastupujuci[i]=zoznam[0] #do zoznamu nastupujuci si uložím nastupujúcich
    vystupujuci[i]=zoznam[1] #do zoznamu vystupujucich si uložím vystupujúcich
    zastavky[i]=zoznam[2] #do zoznamu zastavky si uložím zástavky
    i+=1 #premennú i zväčšujem o 1
    
subor.close() #zavriem súbor

for pocet in range(i): #for cyklus na vypísanie zastávok
    canvas.create_text(x,y,text=zastavky[pocet],font='Arial 10 bold') #vypisujem zastávky
    y+=25 #premennú y zväčšujem o 25
    
def naplnenost(ktora): #funkcia pod ktorou mám vykreslenia všetkých indikátorov
    global b #premennú b si nastavím na globálnu
    dielik=100//50 #pomocná premenná dielik, aby som vedel vykresliť indikátor
    if ktora==1: #podmienka, ktoru kontrolujem hodnotu premennej ktora
        naplnenost=110+(int(nastupujuci[0])*dielik)-(int(vystupujuci[0])*dielik) #premenná naplnenost, aby som vedel kedy je autobus preplnený
        if naplnenost>=210: #podmienka, ktorou komtrolujem aký počet cestujúcich vezie autobus či je preplneny alebo nie
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,120+(int(nastupujuci[0])*dielik)-(int(vystupujuci[0])*dielik),b+20,fill='red') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25  
        else:
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,110+(int(nastupujuci[0])*dielik)-(int(vystupujuci[0])*dielik),b+20,fill='green') #vykreslujem obdĺžnik
            b+=25  #premennú b zväčšujem o 25   
    if ktora==2: #podmienka, ktoru kontrolujem hodnotu premennej ktora
        naplnenost=140+(int(nastupujuci[1])*dielik)-(int(vystupujuci[1])*dielik) #premenná naplnenost, aby som vedel kedy je autobus preplnený
        if naplnenost>=210: #podmienka, ktorou komtrolujem aký počet cestujúcich vezie autobus či je preplneny alebo nie
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,150+(int(nastupujuci[1])*dielik)-(int(vystupujuci[1])*dielik),b+20,fill='red') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
        else:
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,140+(int(nastupujuci[1])*dielik)-(int(vystupujuci[1])*dielik),b+20,fill='green') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
    if ktora==3: #podmienka, ktoru kontrolujem hodnotu premennej ktora
        naplnenost=210+(int(nastupujuci[2])*dielik)-(int(vystupujuci[2])**dielik) #premenná naplnenost, aby som vedel kedy je autobus preplnený
        if naplnenost>=210: #podmienka, ktorou komtrolujem aký počet cestujúcich vezie autobus či je preplneny alebo nie
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,220+(int(nastupujuci[2])*dielik)-(int(vystupujuci[2])*dielik),b+20,fill='red') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
        else:
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,210+(int(nastupujuci[2])*dielik)-(int(vystupujuci[2])*dielik),b+20,fill='green') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
    if ktora==4: #podmienka, ktoru kontrolujem hodnotu premennej ktora
        naplnenost=190+(int(nastupujuci[3])*dielik)-(int(vystupujuci[3])*dielik) #premenná naplnenost, aby som vedel kedy je autobus preplnený
        if naplnenost>=210: #podmienka, ktorou komtrolujem aký počet cestujúcich vezie autobus či je preplneny alebo nie
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,200+(int(nastupujuci[3])*dielik)-(int(vystupujuci[3])*dielik),b+20,fill='red') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
        else:
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,190+(int(nastupujuci[3])*dielik)-(int(vystupujuci[3])*dielik),b+20,fill='green') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
    if ktora==5: #podmienka, ktoru kontrolujem hodnotu premennej ktora
        naplnenost=230+(int(nastupujuci[4])*dielik)-(int(vystupujuci[4])*dielik) #premenná naplnenost, aby som vedel kedy je autobus preplnený
        if naplnenost>=210: #podmienka, ktorou komtrolujem aký počet cestujúcich vezie autobus či je preplneny alebo nie
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,240+(int(nastupujuci[4])*dielik)-(int(vystupujuci[4])*dielik),b+20,fill='red') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
        else:
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,230+(int(nastupujuci[4])*dielik)-(int(vystupujuci[4])*dielik),b+20,fill='green') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
    if ktora==6: #podmienka, ktoru kontrolujem hodnotu premennej ktora
        naplnenost=170+(int(nastupujuci[5])*dielik)-(int(vystupujuci[5])*dielik) #premenná naplnenost, aby som vedel kedy je autobus preplnený
        if naplnenost>=210: #podmienka, ktorou komtrolujem aký počet cestujúcich vezie autobus či je preplneny alebo nie
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,180+(int(nastupujuci[5])*dielik)-(int(vystupujuci[5])*dielik),b+20,fill='red') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
        else:
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,170+(int(nastupujuci[5])*dielik)-(int(vystupujuci[5])*dielik),b+20,fill='green') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
    if ktora==7: #podmienka, ktoru kontrolujem hodnotu premennej ktora
        naplnenost=160+(int(nastupujuci[6])*dielik)-(int(vystupujuci[6])*dielik)
        if naplnenost>=210: #podmienka, ktorou komtrolujem aký počet cestujúcich vezie autobus či je preplneny alebo nie
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,240+(int(nastupujuci[6])*dielik)-(int(vystupujuci[6])*dielik),b+20,fill='red') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
        else: 
            canvas.create_rectangle(110,b,210,b+20) #vykreslujem obdĺžnik
            canvas.create_rectangle(110,b,160+(int(nastupujuci[6])*dielik)-(int(vystupujuci[6])*dielik),b+20,fill='green') #vykreslujem obdĺžnik
            b+=25 #premennú b zväčšujem o 25 
            
def prva(event): #funkcia na volanie ďalšej funkcie a vykreslenia indikátora
    ktora=1 #premennú ktora nastavím na 1
    naplnenost(ktora) #volám funkciu naplnenost s hodnotou ktora

def druha(event): #funkcia na volanie ďalšej funkcie a vykreslenia indikátora
    ktora=2 #premennú ktora nastavím na 2
    naplnenost(ktora) #volám funkciu naplnenost s hodnotou ktora

def tretia(event): #funkcia na volanie ďalšej funkcie a vykreslenia indikátora
    ktora=3 #premennú ktora nastavím na 3
    naplnenost(ktora) #volám funkciu naplnenost s hodnotou ktora

def stvrta(event): #funkcia na volanie ďalšej funkcie a vykreslenia indikátora
    ktora=4 #premennú ktora nastavím na 4
    naplnenost(ktora)#volám funkciu naplnenost s hodnotou ktora

def piata(event): #funkcia na volanie ďalšej funkcie a vykreslenia indikátora
    ktora=5 #premennú ktora nastavím na 5
    naplnenost(ktora) #volám funkciu naplnenost s hodnotou ktora

def siesta(event): #funkcia na volanie ďalšej funkcie a vykreslenia indikátora
    ktora=6 #premennú ktora nastavím na 6
    naplnenost(ktora) #volám funkciu naplnenost s hodnotou ktora
    
def siedma(event): #funkcia na volanie ďalšej funkcie a vykreslenia indikátora
    ktora=7 #premennú ktora nastavím na 7
    naplnenost(ktora) #volám funkciu naplnenost s hodnotou ktora
    
canvas.bind_all('<a>',prva) #nabidovaná klávesa a pre danú funkciu
canvas.bind_all('<b>',druha) #nabidovaná klávesa b pre danú funkciu
canvas.bind_all('<c>',tretia) #nabidovaná klávesa c pre danú funkciu
canvas.bind_all('<d>',stvrta) #nabidovaná klávesa d pre danú funkciu
canvas.bind_all('<e>',piata) #nabidovaná klávesa e pre danú funkciu
canvas.bind_all('<f>',siesta) #nabidovaná klávesa f pre danú funkciu
canvas.bind_all('<g>',siedma) #nabidovaná klávesa g pre danú funkciu

print('Ak chceš vykresliť indikátor zástavky Štúrovo nám.stlač klávesu a.') #vypíšem text do shellu
print('Ak chceš vykresliť indikátor zástavky Mestský park stlač klávesu b.') #vypíšem text do shellu
print('Ak chceš vykresliť indikátor zástavky Dargovská stlač klávesu c.') #vypíšem text do shellu
print('Ak chceš vykresliť indikátor zástavky Nemocnica stlač klávesu d.') #vypíšem text do shellu
print('Ak chceš vykresliť indikátor zástavky Bratská stlač klávesu e.') #vypíšem text do shellu
print('Ak chceš vykresliť indikátor zástavky Mestský úrad stlač klávesu f.') #vypíšem text do shellu
print('Ak chceš vykresliť indikátor zástavky Partizánska stlač klávesu g.') #vypíšem text do shellu
print('Pre zástavku Bernolákova nemusíš stláčať žiadnú kláves, lebo autobus odtiaľ ide prázdny.') #vypíšem text do shellu