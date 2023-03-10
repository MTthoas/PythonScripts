def exo6():

    while True:

        car = input("Saisissez une chaine de caractère : ")

        suffix = [".com"]

        if not "@" in car:
            print("L'adresse mail n'est pas valide")
            break
            

        for i in range(len(car)-1, len(car)-len(suffix)-1):
            if car[i] != suffix[len(suffix) - (len(car)-i)]:
                print("L'adresse mail n'est pas valide, il n'y a pas de .com")
                
    
def exo7():

    car = input("Saississez une phrase :")

    for i in range(10):
        print(car)

    return "fin Exo 7"


def exo8():

    car = input("Saissisez une phrase :")

    for i in range(len(car)):
        print(car[i])

    return "fin exo 8"


def exo9():
    
    print("a : 0")
    print("b : 10\n")

    for i in range(0, 10):
        print(i)

    return "fin exo 9"

def exo10():
    
    a=0
    b=10

    print("a :", a)
    print("b :", b, "\n")

    while(b != 0):
        b-=1
        if(b % 2 != 0):     
            print(b)

    return "fin exo 10"


def exo11():

    while True:
        try:
            a = input("Saississez un nombre entre 1 et 10 : ")
            a = int(a)

            if(a < 1 or a > 10):
                print("Vous devez entrer un nombre entre 1 et 10 !")
                continue
            break
        except ValueError:
            print("Vous n'avez pas entré un nombre !")
            continue

    return "fin exo 11"


def exo12():

    a = 0
    b = 15

    for i in range(a, b+1, 3):
        print(i)

    return "fin exo 12"


def exo13():
    
    n=10
    i=0

    while i < n:
        print(i*2)
        i+=1
        
    print("\n")

    for i in range(0, n):
        print(i*2)
        
    return "fin exo 13"

# print(exo13())

