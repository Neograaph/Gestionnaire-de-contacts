def ajouter_contact(contacts):
    nom = input("Entrez le nom du contact : ")
    numero = input("Entrez le numéro de téléphone : ")
    contacts[nom] = numero
    print("Contact ajouté avec succès.")

def afficher_contacts(contacts):
    if not contacts:
        print("Aucun contact trouvé.")
    else:
        print("Liste des contacts :")
        for nom, numero in contacts.items():
            print(f"{nom} : {numero}")

def rechercher_contact(contacts):
    nom_recherche = input("Entrez le nom du contact à rechercher : ")
    if nom_recherche in contacts:
        print(f"Numéro de téléphone de {nom_recherche} : {contacts[nom_recherche]}")
    else:
        print("Contact non trouvé.")

def supprimer_contact(contacts):
    nom_supprimer = input("Entrez le nom du contact à supprimer : ")
    if nom_supprimer in contacts:
        del contacts[nom_supprimer]
        print("Contact supprimé avec succès.")
    else:
        print("Contact non trouvé.")

def gestionnaire_contacts():
    contacts = {}
    while True:
        print("\nMenu :")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_contact(contacts)
        elif choix == "2":
            afficher_contacts(contacts)
        elif choix == "3":
            rechercher_contact(contacts)
        elif choix == "4":
            supprimer_contact(contacts)
        elif choix == "5":
            print("Programme terminé.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Appel de la fonction principale
gestionnaire_contacts()
