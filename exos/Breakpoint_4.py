def exo21():

    nombre = input("Saissit un nombre : ")
    max = input("Combien de fois voulez vous le saisir dans le fichier ? ")

    if not nombre.isdigit():
        print("Ce n'est pas un nombre !")
        return

    with open("data.txt", "w") as f:
        for i in range(int(max)):
            f.write(nombre + "\n")


    return "fin exo 21"

def exo22():

    with open("data.txt", "r") as f:
        for line in f:
            print(line)

            if "@" and "." not in line:
                print("L'adresse mail n'est pas valide")

            index = line[line.rindex('.')+1:]

            if len(index) < 3:
                print("L'adresse mail n'est pas valide")


    return "fin exo 22"


print(exo22())