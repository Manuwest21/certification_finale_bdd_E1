import subprocess
import os

# Liste des scripts à exécuter
scripts = [
    'creation_bdd_luz.py',
    'concat.py',
    'insertion_donnees_api_bdd.py',
    'frequentation.py'
]

# Chemin vers le répertoire des scripts
scripts_folder = './'  # Met à jour ce chemin si nécessaire

def execute_script(script_path):
    """Exécute un script Python et retourne le résultat et les erreurs."""
    print(f"Exécution de {os.path.basename(script_path)}...")
    
    # Exécuter le script
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    
    # Afficher la sortie et les erreurs
    print(result.stdout)
    if result.stderr:
        print(f"Erreur dans {os.path.basename(script_path)} : {result.stderr}")
    
    return result.returncode

def main():
    """Fonction principale pour exécuter tous les scripts."""
    success = True
    
    for script in scripts:
        script_path = os.path.join(scripts_folder, script)
        
        # Exécuter le script et vérifier le code de retour
        return_code = execute_script(script_path)
        if return_code != 0:
            success = False
    
    if success:
        print("Tous les scripts ont été exécutés avec succès.")
    else:
        print("Certains scripts ont échoué.")

if __name__ == "__main__":
    main()

