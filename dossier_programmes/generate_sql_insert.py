import os
import csv

# Recule au parent er affiche le chemin actuel
os.chdir("..")
print(os.getcwd())


def readDos(file):
    """
    Affiche la liste des fichiers dans un dossier donné et permet à l'utilisateur de sélectionner un fichier.

    :param file: Chemin d'accès au dossier contenant les fichiers.
    :return: La date extraite du nom du fichier sélectionné.
    """
    # Lecture du contenu du dossier
    liste_Dos = os.listdir(file)
    liste_dates = []  # Liste pour stocker les dates extraites des noms de fichiers

    # Affichage des fichiers disponibles sous forme de menu avec index
    index = 0
    for fichier in liste_Dos:
        print(f"{index} - {fichier}")
        # Extraction de la date du nom du fichier
        liste_dates.append(fichier[10:-4])
        index += 1

    # On demande de saisir l'inde correspondant au fichier à lire
    demande = int(input("Pour analyser un fichier, entrez son numéro d'index correspondant. Le premier index est 0."))

    # Récupére la date du fichier sélectionné en fonction de l'index
    for i in range(len(liste_dates)):
        if i == demande:
            date_fichier = liste_dates[i]
            print(date_fichier)  # Affiche la date sélectionnée
            return date_fichier  # Retourne la date pour l'utiliser dans d'autres fonctions


def insert_sql(date_fichier):
    """
    Génère un fichier SQL contenant les commandes d'insertion basées sur un fichier CSV.

    :param date_fichier: Date extraite du nom du fichier log, utilisée pour nommer le fichier SQL.
    :return: None
    """
    # Créé un dossier pour stocker les fichiers SQL si le dossier n'existe pas
    if not os.path.exists("dossier_insert"):
        os.makedirs("dossier_insert")

    # Ouvrir le fichier CSV correspondant à la date donnée
    with open(f"dossier_csv/log_proxy_{date_fichier}.csv", "r") as f:
        reader = csv.reader(f, delimiter=';')  # Lire le fichier CSV avec un délimiteur ';'
        next(reader)  # Ignorer la première ligne (en-tête du fichier CSV)

        # Créer et ouvrir le fichier SQL où écrire les commandes d'insertion
        with open(f"dossier_insert/insert_log_{date_fichier}.sql", "w") as new_f:
            for row in reader:
                # Écrire une commande SQL pour chaque ligne du fichier CSV
                new_f.write(
                    f"INSERT INTO acces_log (date, heure, adresse_ip_employe, url_consultee, methode_http, "
                    f"code_reponse) VALUES ('{date_fichier}', '{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', "
                    f"'{row[4]}');\n"
                )


# Exéction de la fonction
# Lecture des fichiers disponibles et génération du fichier SQL pour la date sélectionnée
insert_sql(readDos("dossier_csv/"))
