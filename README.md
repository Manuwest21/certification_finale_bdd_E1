Projet Data Science SNCF

Ce projet vise à analyser les données des objets trouvés dans les gares parisiennes entre 2019 et 2022 à partir de l'API open data de la SNCF et des données météorologiques disponibles sur internet.
Collecte de données

Les données ont été récupérées à partir de l'API open data de la SNCF pour les objets trouvés entre 2019 et 2022 dans les gares parisiennes. Les données météorologiques (températures moyennes journalières sur Paris) pour la même période ont été récupérées sur internet.
Stockage des données

Les données ont été stockées dans une base de données SQL dont le schéma a été préalablement défini.
Analyse des données et visualisation

Une application Streamlit a été développée pour permettre l'analyse et la visualisation des données.

    La somme du nombre d'objets trouvés par semaine entre 2019 et 2022 a été calculée et affichée sur un histogramme Plotly. Il est possible de choisir les types d'objets à afficher.
    Une carte de Paris a été affichée avec le nombre d'objets trouvés en fonction de la fréquentation de voyageurs de chaque gare. Il est possible de faire varier par année et par type d'objets.
    Le nombre d'objets trouvés a été affiché en fonction de la température sur un scatterplot. Il a été analysé si le nombre d'objets perdus est corrélé à la température.
    La médiane du nombre d'objets trouvés a été calculée en fonction de la saison. Il a été analysé s'il y a une corrélation entre ces deux variables.
    Le nombre d'objets trouvés a été affiché en fonction du type d'objet et de la saison sur un graphique. Il a été analysé s'il y a une corrélation entre ces deux variables.

Conclusion

Ce projet a permis d'analyser les données des objets trouvés dans les gares parisiennes entre 2019 et 2022 et de les visualiser de différentes manières. 
