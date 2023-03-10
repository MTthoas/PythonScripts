def exo15():

    liste= [17,38,10,25,72]

    liste.sort()
    
    print("liste triée :", liste)

    liste.append(12)
        
    print("liste avec 12 ajouté :", liste)

    liste.reverse()

    print("liste inversée :", liste)

    liste.index(17)

    print("index de 17 :", liste.index(17))

    liste.remove(38)

    print("liste sans 38 :", liste)

    print("liste du 2eme au 3eme élément :", liste[1:3])

    print("liste du 1er au 2eme élément :", liste[:2])

    print("Liste du 3eme au dernier élément :", liste[2:])

    print("Liste :", liste[:])

    return "fin exo 15"
    
def exo16():

    Chaine = "Bonjour tout le monde !"

    print("Inverse de la chaine :", Chaine[::-1])

def exo17():

    car = input("Saississez une chaine de caractères : ")

    if(car == car[::-1]):
        print("C'est un palindrome")
    else:
        print("Ce n'est pas un palindrome")



def exo18():

    car = input("Saississez un email :")

    if "@" and "." not in car:
        print("L'adresse mail n'est pas valide")
    
    index = car[car.rindex('.')+1:]

    if len(index) < 3:
        print("L'adresse mail n'est pas valide")

    return "fin exo 18"


def exo19():

    print("truc :", [])
    print("machin :", [0.0]*5)


def exo20():

    print(list(range(0, 3+1)))
    print(list(range(4, 7+1)))
    print(list(range(2, 8+1,2)))

    chose = list(range(0,5+1))

    print([i in chose for i in [3, 6]])
    
    return "fin exo 20"
            
print(exo20())