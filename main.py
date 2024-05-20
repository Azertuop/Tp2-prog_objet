#Elvis Basic

#PRODUIT NON-TAXABELE
def produit_non_taxable(produit):
    nom = input("Ajouter un article non-taxable: ")
    prix_unitaire = float(input("Prix unitaire de l'article: "))
    quantité = int(input("Quantité de l'article: "))
    total = prix_unitaire * quantité
    produit.append({'nom': nom, 'prix_unitaire': prix_unitaire, 'quantite': quantité, 'total': total})

#PRODUIT TAXABLE
def produit_taxable(produit):
    nom = input("Ajouter un article taxable: ")
    prix_unitaire = float(input("Prix unitaire de l'article: "))
    quantité = int(input("Quantité de l'article: "))
    total = ((prix_unitaire * quantité) * 1.14975)
    produit.append({'nom': nom, 'prix_unitaire': prix_unitaire, 'quantite': quantité, 'total': total})

#PRODUIT QU'ON VEUT SUPPRIMER
def supprimer_produit(produit):
    nom = input("L'article que vous voulez enlever: ")
    for item in produit:
        if item['nom'] == nom:
            produit.remove(item)
            break
#LE RECU
def recu(produit):
    total = 0
    print("______________________RECU_________________________")
    print("Quantité     Produits        P.U          Tot.")
    print("___________________________________________________")
    for item in produit:
        print(f"{item['quantite']}      -     {item['nom']}     -    {item['prix_unitaire']}    -   {item['total']:.2f}$")
        total += item['total']
    print("___________________________________________________")
    print("Total à payer:", total, "$")
    print("Merci")
#LE MENU
def menu(produit):
    while True:
        print("LE MENU DISPONIBLE A VOTRE CAISSE EST LE SUIVANT: ")
        print("1.  Ajouter un article non-taxable.")
        print("2.  Ajouter un article taxable.")
        print("3.  L'article que vous voulez enlever.")
        print("4.  Votre recu.")
        nombre = int(input("Que voulez vous faire: "))

        if nombre == 1:
            produit_non_taxable(produit)

        elif nombre == 2:
            produit_taxable(produit)

        elif nombre == 2:
            produit_taxable(produit)

        elif nombre == 3:
            supprimer_produit(produit)

        elif nombre == 4:
            recu(produit)
            break


produit_liste = []
menu(produit_liste)

