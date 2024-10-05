import os
import subprocess

def run_main_import():
    """Exécute le script main_import.py situé dans le dossier importation_données."""
    # Chemin du script main_import.py
    script_path = os.path.join(os.getcwd(), 'lancement_scripts_projet', 'importation_données', 'main_import.py')
    
    try:
        # Exécute le script Python en tant que sous-processus.
        result = subprocess.run(['python', script_path], check=True, text=True, capture_output=True)
        
        # Affiche un message de succès si l'exécution est réussie.
        print("Exécution de main_import.py terminée avec succès.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Affiche un message d'erreur si le script échoue.
        print(f"Erreur lors de l'exécution de main_import.py: {e}")
        print(e.stderr)

# Vérifie si le script est exécuté directement.
if __name__ == "__main__":
    run_main_import()