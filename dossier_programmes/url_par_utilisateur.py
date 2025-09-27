import os

# Recule au parent er affiche le chemin actuel
os.chdir("..")
print(os.getcwd())

# Afficher les logs disponibles sous forme d'un menu
data_logs = []


def readLogs(file, liste_Data):
    """
    :param liste_Data: liste des données logs
    :param file: le chemin d'accès du fichier
    :return: Renvoie une liste des données de chaque ligne avec les éléments distincts dans un sous tableau
    """
    # Lecture du dossier
    liste_Dos = os.listdir(file)

    # Menu
    index = 0
    for fichier in liste_Dos:
        print(f"{index} - {fichier}")
        index += 1

    demande = int(input("Pour analyser un fichier rentrer son numéro d'index correspondant. Le premier index est 0."))

    # Vérification que l'index saisi soit correcte
    if demande > len(liste_Dos) - 1:
        print("Il n'y a aucun index correspond au numéro saisie.")
        print(demande)
    # Si c'est le cas alors
    else:
        for i in range(len(liste_Dos)):
            if i == demande:
                with open(f"{file}/{liste_Dos[demande]}", "r") as f:
                    # Parcours ligne par ligne
                    for line in f:
                        # Ajout des données dans la liste
                        liste_Data.append(line.strip().split(" "))


def sortData(liste_Data):
    """
    Compte le nombre d'apparitions de chaque adresse IP dans liste_Data
    et les ajoute dans liste_Users.

    :param liste_Data: Liste contenant des sous-tableaux avec des adresses IP.
    :return: None
    """
    print("----- SORTDATA ------")
    # Création de deux listes
    result = []  # liste finale
    unique_ips = []  # liste d'ip uniques

    # On ajoute les adresses ip dans la liste unique_ips
    for element in liste_Data:
        ip = element[1]
        if ip not in unique_ips:
            unique_ips.append(ip)

    # Comptage des URL en fonction de l'ip
    for ip in unique_ips:
        url_counts = []  # création d'une liste pour compter le nombre d'apparitions des URL pour chaque ip

        # On parcourt chaque sous tableau de liste_Data
        for element in liste_Data:
            if element[1] == ip:
                url = element[4]

                # On vérifie si l'URL est déjà présente dans la liste
                for entry in url_counts:
                    if entry[0] == url:
                        entry[1] += 1
                        break  # Empêche le bloc else de s'exécuter si l'URL est déjà présente
                else:
                    # Si elle n'existe pas, on l'ajoute
                    url_counts.append([url, 1])

        #  On cherche l'URL qui a le plus de visites pour l'ip actuelle
        maxVisites = 0
        url = ""
        for i in range(len(url_counts)):
            if url_counts[i][1] > maxVisites:
                maxVisites = url_counts[i][1]
                url = url_counts[i][0]

        # On ajoute l'utilisateur, l'url, et le nombre de visites
        result.append([ip, url, maxVisites])

    # Affichage du résultat
    for elt in result:
        print(f"L'URL la plus visitée par {elt[0]} est {elt[1]} nombre de fois {elt[2]}.")


readLogs("dossier_logs_proxy/", data_logs)
sortData(data_logs)
