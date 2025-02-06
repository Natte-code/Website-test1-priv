import webbrowser
import time




love = "Jag älskar dig \n" * 1000
name = ""
g1 = ""
svar = ""




def fråga1():
    global svar
    print("""För första gåtan om mig. \n
Nathaniel är ju mitt namn""")
    svar = input("Mitt namns svenska stavning är nathanael. Från vilket land kommer stavningen Nathaniel? Svara här: ").lower() #jag kommer föralltid fucking hata dig din jävla fucking .lower. FUCK YOU PERSONLIGEN. DU OCH DIN JÄVLA () KAN FAN TA OCH DÖDA ER SJÄLVA
    url = "https://natte-code.github.io/Website-test1-priv/"
    if svar == "usa":
        webbrowser.open(url)

        
def mainq():
    global g1
    g1 = input ("Är du redo? Y/N: ").lower()
    if g1 == "y":
        print("Jasså, Du vågar dig på. Nu kör vi!!")
        fråga1()

    elif g1 == "n":
        nej()


def nej():
    print("Vad tråkigt >:(, nu Kommmer du bli spammad av ett ord och så ska du få göra om detta.")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    
    print(love)
    time.sleep(2)
    print("Nu börjar det om.")
    mainq()

print("""Hej hej! \n
Nu ska du få se vad jag har gjort till dig. \n
Men först Måste du klara en simpel lite gåta""")
mainq()
time.sleep(2)




time.sleep(3)


if g1 == "Y":
    print("Jasså, Du vågar dig på. Nu kör vi!!")
    fråga1()

elif g1 == "N":
    nej()