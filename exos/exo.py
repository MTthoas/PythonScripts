class Commande:
    def __init__(self, date, numero, prix):
        self.date = date
        self.numero = numero
        self.prix = prix

    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date

    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero

    def get_prix(self):
        return self.prix
    
    def set_prix(self, prix):
        self.prix = prix

    def calculTVA(self):
        return self.prix + self.prix * 0.196

    def acquitter(self):
        print("La commande a été acquittée")

    
class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse

    def get_nom(self):
        return self.nom
    
    def set_nom(self, nom):
        self.nom = nom

    def get_adresse(self):
        return self.adresse
    
    def set_adresse(self, adresse):
        self.adresse = adresse

    def contacter(self):
        print("Le client " + self.nom +" a été contacté à son adresse : " + self.adresse)

    
c = Commande("2020-01-01", "12354", 100)

print("Date: " + c.get_date())
print("Numéro :" + c.get_numero())
print("Prix :" + str(c.get_prix()))
print("Prix après TVA : " + str(c.calculTVA()))

c.acquitter()

client = Client("ddéscq", "cac@gmail.com")

print("Nom" + str(client.get_nom()))
print("Adresse" + str(client.get_adresse()))

print(Client.contacter(client))