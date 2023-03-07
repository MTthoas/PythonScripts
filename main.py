def exo1(): 

    def CalculSpeed(temps, distance):
        return temps * distance

    vitesse = CalculSpeed(6.892, 19.7)
    print(f"La vitesse est : {vitesse:.1f} m/s")

    return "Fin exo1"

def exo2():

    while True:
        try:
            nom = input("Entrez votre nom : ")
            age = str(nom)
            break
        except ValueError:
            print("Vous n'avez pas entré un nombre !")
    
    while True:
        try:
            age = input("Entrez votre age : ")
            age = int(age)
            break
        except ValueError:
            print("Vous n'avez pas entré un nombre !")
    

    print(f"Bonjour {nom}, vous avez {age} ans.")

    return "Fin exo2"

def exo3():

    while True:
        try:
            nombre = float(input("Entrez un nombre flottant : "))
            if(nombre >= 0):
                racine = nombre ** 0.5
                print(f"la racine de {nombre} est {racine}")
                break
            else:
                print("Erreur : le nombre doit être positif ou nul !")
        except ValueError:
            print("Erreur : vous n'avez pas entré un nombre flottant !")
    

    return "Fin exo3"

def exo4():

    motOne = input("Saissisez le premier mot : ")
    motTwo = input("Saissisez le deuxième mot : ")

    if(motOne < motTwo):
        print(f"{motOne} est plus petit que {motTwo}")
    elif(motOne > motTwo):
        print(f"{motOne} est plus grand que {motTwo}")
    else:
        print("Les deux mots sont identiques")

    return "Fin exo4"
    
def exo5():

    pSeuil = 2.3;
    vSeuil = 7.41;

    while True:
        try:
            pression = float(input("Entrez la pression : "))
            volume = float(input("Entrez le volume : "))
        except ValueError:
            print("Erreur : vous n'avez pas entré un nombre flottant !")

        if(pression > pSeuil and volume > vSeuil):
            print("Arrêt immédiat !\n")
        elif(pression > pSeuil):
            print("augmenter le volumede l’enceinte\n")
        elif(volume > vSeuil):
            print("diminuer le volume\n")
        else:
            print("tout va bien\n")
            break
            
print(exo5())