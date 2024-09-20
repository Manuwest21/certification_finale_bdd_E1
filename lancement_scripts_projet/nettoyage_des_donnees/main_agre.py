import subprocess
import os

def run_script(script_name):
    """Exécute un script Python en tant que sous-processus."""
    try:
        # Exécute le script Python et attend la fin du processus
        result = subprocess.run(['python', script_name], check=True, text=True, capture_output=True)
        print(f"Exécution de {script_name} terminée avec succès.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {script_name}: {e}")
        print(e.stderr)

def run_notebook(notebook_name):
    """Exécute un fichier Jupyter Notebook avec nbconvert."""
    try:
        # Utilise nbconvert pour exécuter le notebook
        result = subprocess.run(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', notebook_name],
                                check=True, text=True, capture_output=True)
        print(f"Exécution de {notebook_name} terminée avec succès.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {notebook_name}: {e}")
        print(e.stderr)

if __name__ == "__main__":
    # Obtenir le chemin du répertoire actuel
    repertoire_actuel = os.getcwd()

    # Fichiers Python à exécuter
    scripts = ['creation_bdd_sqlite.py', 'crea_sqlite_pondere.py']

    # Exécuter les scripts Python
    for script in scripts:
        run_script(script)

    # Fichier Jupyter Notebook à exécuter
    notebook = 'meteo.ipynb'

    # Exécuter le fichier Jupyter Notebook
    run_notebook(notebook)