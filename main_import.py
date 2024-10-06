import os                                                                                                    # Permet d'interagir avec le système d'exploitation, comme les chemins de fichiers.
import subprocess                                                                                            # Permet de lancer des sous-processus, comme l'exécution de scripts Python.

def run_script(script_name, success_message):
    """Exécute un script Python via subprocess et affiche un message de succès."""
                                                                                                             # Définit le chemin du répertoire contenant les scripts à lancer.
    scripts_directory = os.path.join(os.getcwd(), 'lancement_scripts_projet', 'importation_données')
    
                                                                                                             # Construit le chemin complet du script à partir du répertoire des scripts et du nom du script.
    script_path = os.path.join(scripts_directory, script_name)
    
    try:
                                                                                                             # Exécute le script Python en tant que sous-processus.
                                                                                                             # 'python' est le programme à exécuter, et script_path est le script à lancer.
        result = subprocess.run(['python', script_path], check=True, text=True, capture_output=True)
        
                                                                                                             # Affiche un message de succès si l'exécution est réussie.
        print(f"✅ {success_message}")
                                                                                                             # Affiche la sortie du script (ce qu'il imprime).
        print(result.stdout)
    except subprocess.CalledProcessError as e:                                                               # Attrape les erreurs si le script échoue (retourne un code d'erreur).
       
                                                                                                             # Affiche un message d'erreur avec le nom du script et le détail de l'erreur.
        print(f"❌ Erreur lors de l'exécution de {script_name}: {e}")
                                                                                                             # Affiche la sortie d'erreur du script (le texte d'erreur).
        print(e.stderr)

                                                                                                             # Ce bloc s'assure que le code ci-dessous ne sera exécuté que si ce fichier est exécuté directement,
                                                                                                             # et non pas s'il est importé en tant que module dans un autre script.
if __name__ == "__main__":
                                                                                                             # Liste des scripts Python à exécuter avec les messages de succès correspondants.
    scripts = [
        ('frequentation_api.py', "Les données de la fréquentation ont bien été importées."),
        ('objets_trouves_api.py', "Les données des objets trouvés ont bien été importées."),
        ('concat.py', "Les données météorologiques ont bien été concaténées.")
    ]
    
                                                                                                             # Boucle à travers chaque script dans la liste.
    for script_name, success_message in scripts:
                                                                                                             # Appelle la fonction run_script pour exécuter chaque script et afficher le message de succès.
        run_script(script_name, success_message)
