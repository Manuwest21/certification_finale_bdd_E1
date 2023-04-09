import sqlite3

# def recup_ses_actions_(mon_id:int):
#     connexion=sqlite3.connect('bdd.db')
#     curseur= connexion.cursor()
        
#     curseur.execute("""
#                         SELECT meteo.date, gare.nom_gare, objets_trouves.date_meteo, 
#                         FROM carnet_operation
#                         INNER JOIN action ON carnet_operation.action_id=action.id
#                         INNER JOIN asso_suivi_suiveur ON asso_suivi_suiveur.suiveur =carnet_operation.user_id 
#                         INNER JOIN utilisateur ON utilisateur.id= asso_suivi_suiveur.suiveur
#                         WHERE action_id =?
#                         AND 
                        
#                         """,(mon_id,))
#     rslt=curseur.fetchall()
#     return rslt


# def creer_action(entreprise:str, prix:int) -> None:
#     connexion = sqlite3.connect("bdd.db")
#     curseur = connexion.cursor()

#     curseur.execute("""
#                     INSERT INTO objets_trouves
#                         VALUES (NULL, ?, ?)   
#                     """, (entreprise, prix))
#     connexion.commit()
# # qd il y a points d'interrogation >>>il va chercher la valeur qui sera donnée plus tard)cf : .format()
#     connexion.close()
def recup_ses_actions_(mon_id:int):
    connexion = sqlite3.connect("bdu.db")
    curseur.execute("""
        UPDATE objets_trouvés
        SET nom_gare = gare.nom_gare
        FROM gare
        WHERE objets_trouvés.gare = gare.nom_gare
        """)
    connexion.commit()