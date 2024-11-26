# 📝 Énoncé : Gestionnaire de Contacts en Python

Tu vas créer un programme Python pour gérer une liste de contacts. Ce programme permettra d'ajouter, afficher, rechercher et supprimer des contacts. Voici les fonctionnalités que tu devras implémenter :

---

## 🎯 Objectif
Créer un programme qui propose un menu interactif pour manipuler une liste de contacts.

---

## 🚀 Instructions

### 1️⃣ Fonctionnalité principale
Ton programme devra afficher un menu avec les choix suivants :

1. Ajouter un contact  
2. Afficher tous les contacts  
3. Rechercher un contact  
4. Supprimer un contact  
5. Quitter  

### 2️⃣ Détails des fonctionnalités

#### 👉 Ajouter un contact
- Demande à l'utilisateur de saisir un **nom** et un **numéro de téléphone**.
- Enregistre ces informations dans un **dictionnaire** où la **clé** est le nom et la **valeur** est le numéro.
- Affiche un message confirmant que le contact a été ajouté :  
  `Contact ajouté avec succès.`

#### 👉 Afficher tous les contacts
- Si aucun contact n'est enregistré, affiche :  
  `Aucun contact trouvé.`
- Sinon, affiche chaque contact sous la forme :  
  `Nom : Numéro`.

#### 👉 Rechercher un contact
- Demande le **nom** du contact à rechercher.
- Si le contact existe, affiche son numéro :  
  `Numéro de téléphone de <Nom> : <Numéro>`.
- Sinon, affiche :  
  `Contact non trouvé.`

#### 👉 Supprimer un contact
- Demande le **nom** du contact à supprimer.
- Si le contact existe, supprime-le du dictionnaire et affiche :  
  `Contact supprimé avec succès.`
- Sinon, affiche :  
  `Contact non trouvé.`

#### 👉 Quitter
- Si l'utilisateur choisit cette option, le programme se termine avec le message :  
  `Programme terminé.`

---

## 💡 Conseils
- Utilise un **dictionnaire** Python pour stocker les contacts.
- Place chaque fonctionnalité dans une **fonction distincte** pour mieux organiser ton code.
- Crée une fonction **principale** qui affiche le menu et appelle les autres fonctions en fonction du choix de l'utilisateur.
- Vérifie les entrées utilisateur pour éviter des erreurs.

---

## 🔍 Exemple de fonctionnement (version console)

```plaintext
Menu :
1. Ajouter un contact
2. Afficher tous les contacts
3. Rechercher un contact
4. Supprimer un contact
5. Quitter
Entrez votre choix : 1
Entrez le nom du contact : Alice
Entrez le numéro de téléphone : 0612345678
Contact ajouté avec succès.

Menu :
1. Ajouter un contact
2. Afficher tous les contacts
3. Rechercher un contact
4. Supprimer un contact
5. Quitter
Entrez votre choix : 2
Liste des contacts :
Alice : 0612345678

Menu :
1. Ajouter un contact
2. Afficher tous les contacts
3. Rechercher un contact
4. Supprimer un contact
5. Quitter
Entrez votre choix : 5
Programme terminé.
```

## 🚀 Va plus loin !

Si tu veux relever un défi supplémentaire, tu peux imaginer une **interface graphique** pour ton programme en utilisant la bibliothèque **Tkinter**.  
Voici quelques idées pour l'interface graphique :
- **Ajouter des boutons** pour chaque fonctionnalité (Ajouter, Afficher, Rechercher, Supprimer).
- **Utiliser des champs de saisie** pour entrer le nom et le numéro de téléphone.
- Afficher les contacts dans une **liste déroulante** ou une **zone de texte**.

### 📌 Exemple de code pour démarrer avec Tkinter
Voici un petit exemple pour te guider dans l'utilisation de Tkinter :
```python
import tkinter as tk

def afficher_message():
    label_message.config(text="Bonjour !")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestionnaire de Contacts")

# Ajouter un bouton
bouton = tk.Button(fenetre, text="Cliquez ici", command=afficher_message)
bouton.pack()

# Ajouter une étiquette
label_message = tk.Label(fenetre, text="")
label_message.pack()

# Lancer la fenêtre
fenetre.mainloop()
```
