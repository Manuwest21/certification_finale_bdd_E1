# import os  # Permet d'interagir avec le système d'exploitation, comme les chemins de fichiers.
# import subprocess  # Permet de lancer des sous-processus, comme l'exécution de scripts Python.

# def run_script(script_name):
#     """Exécute un script Python via subprocess."""
#     # Construit le chemin complet du script à partir du nom du script et du répertoire de travail actuel.
#     script_path = os.path.join(os.getcwd(), script_name)
    
#     try:
#         # Exécute le script Python en tant que sous-processus.
#         # 'python' est le programme à exécuter, et script_path est le script à lancer.
#         result = subprocess.run(['python', script_path], check=True, text=True, capture_output=True)
        
#         # Affiche un message de succès si l'exécution est réussie.
#         print(f"Exécution de {script_name} terminée avec succès.")
#         # Affiche la sortie du script (ce qu'il imprime).
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         # Attrape les erreurs si le script échoue (retourne un code d'erreur).
#         # Affiche un message d'erreur avec le nom du script et le détail de l'erreur.
#         print(f"Erreur lors de l'exécution de {script_name}: {e}")
#         # Affiche la sortie d'erreur du script (le texte d'erreur).
#         print(e.stderr)

# # Ce bloc s'assure que le code ci-dessous ne sera exécuté que si ce fichier est exécuté directement, 
# # et non pas s'il est importé en tant que module dans un autre script.
# if __name__ == "__main__":
#     # Liste des noms de fichiers de scripts Python à exécuter.
#     # scripts = ['creation_bdd_lumiere.py','frequentation_api.py', 'objets_trouves_api.py', 'concat.py']
#     scripts = ['creation_bdd_lumiere.py', 'objets_trouves_api.py', 'concat.py']
#     # Boucle à travers chaque script dans la liste.
#     for script in scripts:
#         # Appelle la fonction run_script pour exécuter chaque script.
#         run_script(script)

import os
import subprocess

def run_script(script_name):
    """Exécute un script Python via subprocess."""
    # Définit le chemin du répertoire contenant les scripts à lancer.
    scripts_directory = os.path.join(os.getcwd(), 'lancement_scripts_projet', 'importation_données')
    
    # Construit le chemin complet du script à partir du répertoire des scripts et du nom du script.
    script_path = os.path.join(scripts_directory, script_name)

    try:
        # Exécute le script Python en tant que sous-processus.
        result = subprocess.run(['python', script_path], check=True, text=True, capture_output=True)
        
        # Affiche un message de succès si l'exécution est réussie.
        print(f"Exécution de {script_name} terminée avec succès.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Affiche un message d'erreur si le script échoue.
        print(f"Erreur lors de l'exécution de {script_name}: {e}")
        print(e.stderr)

if __name__ == "__main__":
    # Liste des noms de fichiers de scripts Python à exécuter.
    scripts = ['creation_bdd_lumiere.py', 'frequentation_api.py', 'objets_trouves_api.py', 'concat.py']
    
    # Boucle à travers chaque script dans la liste.
    for script in scripts:
        run_script(script)

