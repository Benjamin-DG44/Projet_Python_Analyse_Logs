import os
import random

# Création d'une liste pour stocker les données
data_list = []

# Recule au parent et affiche le chemin actuel
os.chdir("..")
print(os.getcwd())


# Lecture des données
def readData(file, liste):
    """
    Lit les données d'un fichier texte et les ajoute à une liste sous forme de sous-listes.

    :param file: Chemin relatif du fichier à lire.
    :param liste: La liste où les sous-listes des données extraites seront ajoutées.
    :return: La liste mise à jour contenant les sous-listes des données extraites.
    """
    # Lecture du fichier
    with open(file, "r") as f:
        for line in f:
            liste.append(line.strip().split(";"))

    return liste


# Calcul de l'âge
def calculerAge(liste, i):
    """
    Cette fonction calcule l'âge de chaque personnalité
    :param liste: liste des personnalités
    :param i: index
    :return: âge calculé
    """
    liste[i].append(2025 - int(liste[i][2]))
    return liste[i][3]


# Liste pour stocker les pseudos
pseudo_list = []


# Générer un pseudo pour chaque entrée
def genererPseudo(liste):
    """
    Cette fonction génère un pseudo pour chaque personnalité
    :param liste: liste des personnalités
    """
    for i in range(len(liste)):
        # Premier caractère du prénom
        prenom = liste[i][0][0]

        # Trois premiers caractères du nom
        nom = liste[i][1][0:3]

        # Nombre aléatoire
        valeur_aleatoire = str(random.randint(10, 99))

        # Calcul de l'âge (appel à la fonction calculerAge)
        age = calculerAge(liste, i)

        # Création du pseudo et conversion en minuscule
        pseudo = (prenom + nom + str(age) + valeur_aleatoire).lower()

        # Ajout dans la liste des pseudos
        pseudo_list.append(pseudo)
        print(pseudo)


# Sauvegarder les pseudos dans un fichier
def saveData(liste):
    """
    Cette fonction sauvegarde les pseudos dans un fichier texte
    :param liste: liste des pseudos
    """
    # Écriture dans le fichier
    with open("dossier_test-txt/testSortie.txt", "w") as f:
        for pseudo in liste:
            f.write(pseudo + "\n")


# Exécution du programme
if __name__ == "__main__":
    # Lire les données depuis le fichier d'entrée
    readData("dossier_test-txt/testEntree.txt", data_list)

    # Générer les pseudos
    genererPseudo(data_list)

    # Sauvegarder les pseudos dans le fichier de sortie
    saveData(pseudo_list)
