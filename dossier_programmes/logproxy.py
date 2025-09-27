import csv
import os

# Recule au parent er affiche le chemin actuel
os.chdir("..")
print(os.getcwd())

# Liste pour stocker les données extraites du fichier log
data_list = []

# Saisie une date au format YYYY-MM-DD
saisie_date = input(str("Entrez une date au format YYYY-MM-DD : "))


def extract_data(date_saisie):
    """
    Cette fonction extrait les données du fichier de log correspondant à la date saisie.

    :param date_saisie: Date utilisée pour identifier le fichier de log.
    :return: Liste des données extraites.
    """
    # Construit le chemin d'accès au fichier log
    file_path = f"dossier_logs_proxy/log_proxy_{date_saisie}.txt"

    # Vérifie si le fichier existe
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} est introuvable.")

    # Lit le contenu du fichier log
    with open(file_path, "r") as f:
        for line in f.readlines():  # Parcourir les lignes du fichier
            data = line.strip().split(" ")  # Séparer les données par espace
            time = data[0]  # Extraire l'heure
            ip_address = data[1]  # Extraire l'adresse IP
            url = data[4]  # Extraire l'URL consultée
            http_method = data[2]  # Extraire la méthode HTTP utilisée
            response_code = data[6]  # Extraire le code de réponse du serveur
            # Ajoute les données extraites à la liste `data_list`
            data_list.append([time, ip_address, url, http_method, response_code])

    return data_list  # Retourner la liste des données extraites


def save_data(list_data, date_saisie):
    """
    Cette fonction sauvegarde les données extraites dans un fichier CSV.

    :param list_data: Liste des données extraites.
    :param date_saisie: Date utilisée pour nommer le fichier CSV.
    """
    # Créer un dossier pour les fichiers CSV s'il n'existe pas
    if not os.path.exists("dossier_csv"):
        os.makedirs("dossier_csv")

    # Construire le chemin d'accès au fichier CSV
    file_path = f"dossier_csv/log_proxy_{date_saisie}.csv"

    # Écrire les données dans le fichier CSV
    with open(file_path, "w", newline="") as f:  # Ouvrir le fichier en mode écriture
        writer = csv.writer(f, delimiter=';')  # Définir le séparateur des colonnes
        # Écrire l'en-tête dans le fichier CSV
        writer.writerow(["heure", "adresse_ip_employe", "url_consultee", "methode_http", "code_reponse"])
        # Écrire chaque ligne de données dans le fichier
        for data in list_data:
            writer.writerow(data)  # Ajouter chaque enregistrement dans le fichier CSV


# Point d'entrée du programme
if __name__ == '__main__':
    # Extraire les données du fichier log
    extract_data(saisie_date)
    # Sauvegarder les données extraites dans un fichier CSV
    save_data(data_list, saisie_date)
