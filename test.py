try:
    import pyodbc
    print("pyodbc importé avec succès")
except ImportError as e:
    print("Erreur lors de l'importation de pyodbc:", e)