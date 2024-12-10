from math import sqrt
from random import randint
def intro():
    print("Hei")
    print("Dette programmet skal lære deg om abc-formelen.")
    print("Med andre ord skal vi løse likninger på formen ax^2 + bx + c = 0.")
    print("Du trenger penn og papir for å øve på oppgavene du snart skal få.")
    print("Det er også viktig at du vet hvordan abc-formelen ser ut.")
    print("")
    print("Først vil programmet undersøke om du vet hva a, b og c er i en andregradslikning.")
    print("")
    print("I likningen 3x^2 + 7 - 2x = 0")
    print("Hva er a, b og c i denne likningen?")
    a,b,c = 1,1,1
    while a != 3 or b != -2 or c != 7:
        a = int(input("Skriv inn a: "))
        b = int(input("Skriv inn b: "))
        c = int(input("Skriv inn c: "))
        if a == 3 and b == -2 and c == 7:
            print("Gratulerer, det er helt riktig!")
            print("Da er vi klare for å øve på noen oppgaver.")
            print("")
        else:
            print("Se over tallene en gang til. Husk at a er antall x^2, b er antall x og c er konstantleddet.")
            print("Det betyr at a, b og c bare er tall.")


def enlosning(): #Lager en andregradslikning med en løsning. Løsningene skal være [-5,5]
    x1 = randint(-5,5)
    c = x1**2
    b = 2*x1
    a = 0
    while a == 0: #Unngår at a = 0
        a = randint(-2,2)
    c *= a
    b *=a
    return [a,b,c]

def tolosning(): #Lager en andregradslikning med to løsninger. Løsningene skal være [-5,5]
    x1 = randint(-5,5)
    x2 = randint(-5,5)
    while x2 == x1: #Passer på at vi faktisk får to forskjellige løsninger
        x2 = randint(-5,5)
    c = x1*x2
    b = -x1 - x2
    a = 0
    while a == 0: #Unngår at a = 0
        a = randint(-2,2)
    b *= a
    c *= a
    return [a,b,c]

def ingenlosning(): #Lager en andregradslikning uten løsning.
    c = 0
    while c == 0: #Ungår c = 0, da det alltid gir 2 løsninger
        c = randint(-5,5)
    a = 0
    while a == 0: #unngår at a = 0
        a = randint(-5,5)
    if a*c < 0:
        a *=-1
    b = randint(-5,5)
    while b**2 - 4*a*c>=0:
        b = randint(-5,5)
    return [a,b,c]


def losning(liste): #Løser en andregradslikning og legger også ved antall løsninger.
    a = liste[0]
    b = liste[1]
    c = liste[2]
    d = b**2 -4*a*c
    if d > 0:
        x1 = int((-b + sqrt(d))/(2*a))
        x2 = int((-b - sqrt(d))/(2*a))
        return [2,x1,x2]
    elif d == 0:
        x1 = int(-b/(2*a))
        return [1,x1]
    else:
        return [0]

def likninger(n): #Lager en liste med 3*n likninger, 10 av hver type. 
    list = []
    number_of_each = n
    while len(list) < 3*number_of_each:
        ingen = ingenlosning()
        en = enlosning()
        to = tolosning()
        if ingen not in list and en not in list and to not in list:
            list.append(ingenlosning())
            list.append(enlosning())
            list.append(tolosning())
    return list

def likning_to_txt(likning): #Skriver om [a,b,c] til ax^2+bx+c=0, passer på fortegn etc.
    if likning[0] < 0 and likning[0] != -1:
        a_str = str(likning[0]) + "x^2"
    elif likning[0] == 1:
        a_str = "x^2"
    elif likning[0] == -1:
        a_str = "-x^2"
    else:
        a_str = str(likning[0]) + "x^2"
        
    if likning[1] < 0 and likning[1] != -1:
        b_str = str(likning[1])+"x"
    elif likning[1] == 1:
        b_str = "x"
    elif likning[1] == -1:
        b_str = "-x"
    elif likning[1] == 0:
        b_str = ""
    else:
        b_str = "+" + str(likning[1])+"x"
    
    if likning[2] < 0:
        c_str = str(likning[2])
    elif likning[2] == 0:
        c_str = ""
    else:
        c_str = "+"+str(likning[2])
    
    return a_str+b_str+c_str + "=0"

def oving():
    print("Nå vil du bli presentert med noen andregradslikninger som du skal løse.")
    print("")
    while len(oppgaver)>0:
        if len(oppgaver)<=2:
            likning = oppgaver.pop(randint(0,len(oppgaver)-1))
        else:
            likning = oppgaver.pop(randint(0,2))
        print("----------------------------------------")
        print("Løs likningen:")
        print(likning_to_txt(likning))
        los = losning(likning)
        feil = 0
        d = likning[1]**2 - 4*likning[0]*likning[2]
        while True:
            antall = int(input("Hvor mange løsninger har likningen?"))
            if antall < 0 or antall >2:
                print("Antallet løsninger må være 0, 1 eller 2.")
            else:
                if antall == los[0]:
                    print("Riktig.")
                    break
                else:
                    if feil == 0:
                        print("Det var ikke helt riktig.")
                        print("Merk at b^2 =",likning[1]**2)
                        print("og at 4*a*c =",4*likning[0]*likning[2])
                        feil +=1
                    elif feil == 1:
                        print("Tallet inne i roten blir", d )
                        if d > 0:
                            print("Altså er det 2 løsninger.")
                            antall = 2
                        elif d == 0:
                            print("Altså er det 1 løsning.")
                            antall = 1
                        else:
                            print("Altså er det ingen løsninger.")
                            antall = 0
                        break
        print("")
        feil = 0
        while len(oppgaver)>0:
            if antall == 2:
                x1 = int(input("Skriv inn den første løsningen, x ="))
                x2 = int(input("Skriv inn den andre løsningen, x ="))
                if x1 == los[1] and x2 == los[2] or x1 == los[2] and x2 == los[1]:
                    print("Flott, det var riktig")
                    break
                elif x1 == los[1] and x2 != los[2] or x1 == los[2] and x2 != los[1]:
                    print(x1,"var riktig, men du må undersøke den andre løsningen din.") 
                elif x1 != los[1] and x2 == los[2] or x1 != los[2] and x2 == los[1]:
                    print(x2,"var riktig, men du må undersøke den første løsningen din.") 
                else:
                    if feil == 0:
                        print("Det ble dessverre galt.")
                        print("Husk at -b blir",-likning[1])
                        print("og at det inne i kvadratroten (b^2-4*a*c) blir", d)
                        print("og til slutt at 2a blir", 2*likning[0])
                        print("Prøv en gang til.")
                        feil += 1
                    elif feil == 1:
                        print("Det ble dessverre galt.")
                        print("I telleren din får du", -likning[1], "pluss/minus", int(sqrt(d)))
                        print("I nevneren din får du", 2*likning[0])
                        print("Prøv igjen.")
                        feil += 1
                    elif feil == 2:
                        print("Beklager, det ble ikke helt riktig det heller.")
                        print(f"De riktige løsningene er x = {los[1]} og x = {los[2]}.")
                        break
            elif antall == 1:
                x1 = int(input("Skriv inn den eneste løsningen, x="))
                if x1 == los[1]:
                    print("Flott, det var riktig!")
                    break
                else:
                    if feil == 0:
                        print("Det ble dessverre galt.")
                        print("Husk at -b blir",-likning[1])
                        print("og at det inne i kvadratroten (b^2-4*a*c) blir", d)
                        print("og til slutt at 2a blir", 2*likning[0])
                        print("Prøv en gang til.")
                        feil += 1
                    elif feil == 1:
                        print("Det ble dessverre galt.")
                        print("I telleren din får du", -likning[1], "pluss/minus", int(sqrt(d)))
                        print("I nevneren din får du", 2*likning[0])
                        print("Prøv igjen.")
                        feil += 1
                    elif feil == 2:
                        print("Beklager, det ble ikke helt riktig det heller.")
                        print(f"Den riktige løsningen er x = {los[1]}.")
                        break
            elif antall == 0:
                print("Undersøk at du fikk -b lik",-likning[1])
                print("og at tallet inne i kvadratroten ble",d)
                print("og til slutt at nevneren din ble", 2*likning[0])
                break
        print("")
        spm = input("Vil du løse flere likninger? Skriv j for ja eller n for nei.")
        if spm.lower() == "n":
            print("Det var en god økt, håper du har bedre kontroll på andregradslikninger nå.")
            break
        elif len(oppgaver) == 0:
            print("Det er dessverre tomt for oppgaver, hvis du ønsker en ny runde, start programmet på nytt.")
        else:
            print("Da tar vi en runde til")
            print("")
    

oppgaver = likninger(10) #Lager 3*10 likninger
intro()
oving()


