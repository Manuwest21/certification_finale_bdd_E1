Documentation sur le script d'import des données
Contexte des données

Le projet utilise des données ouvertes fournies par plusieurs sources afin de créer un ensemble de données unifié et cohérent pour analyse. Les deux principales sources de données sont l'API SNCF et un site spécialisé dans les données météorologiques historiques pour Paris. L'objectif est de croiser les informations sur les objets perdus dans les gares parisiennes avec des données de fréquentation et des informations météorologiques pour chaque jour.
API SNCF pour les objets trouvés et la fréquentation

L'API utilisée est une interface RESTful version 1 qui ne nécessite pas de clé API. Elle fournit des données ouvertes sur les services ferroviaires en France, avec des endpoints permettant :

    de rechercher des objets perdus dans les gares
    de consulter les statistiques de fréquentation des gares

Les résultats sont renvoyés au format JSON, ce qui facilite l'intégration dans des applications Python à travers des requêtes GET. Nous spécifions les gares et les années pour lesquelles nous souhaitons extraire les données, en filtrant les résultats par date.

Cette API est sécurisée via HTTPS et impose des quotas d'utilisation, régulant le nombre de requêtes pour éviter les abus. Les informations obtenues incluent des détails sur les objets trouvés ainsi que le nombre de voyageurs dans certaines gares à Paris.
Données météorologiques

Les données météorologiques sont récupérées via le site www.historique-meteo.net. Ces données incluent :

    l'heure d'ensoleillement pour chaque jour
    le pourcentage moyen de couverture nuageuse par jour

Les données sont récupérées sous forme de fichiers CSV correspondant aux années de la période étudiée, et sont ensuite agrégées en un seul fichier pour analyse avec la bibliothèque Pandas. Ces informations météorologiques sont essentielles pour établir une corrélation entre les conditions météorologiques et la perte d'objets dans les gares parisiennes.
Fonctionnalités du script import.py

Le script import.py se trouve à la racine du projet et joue un rôle central dans le processus d'importation et de traitement des données. Il inclut :

    Initialisation des dépendances : Les bibliothèques et modules nécessaires à l'exécution des sous-scripts sont initialisés.
    Gestion des erreurs : Une gestion des exceptions est implémentée pour assurer que chaque étape critique du processus d'import se déroule correctement, avec une gestion appropriée des erreurs en cas de problèmes avec les API ou les fichiers.
    Sauvegarde des résultats : Les résultats finaux des données importées et traitées sont sauvegardés dans des fichiers CSV prêts à être utilisés pour les analyses.

Ce script exécute les trois fichiers suivants :

    objets_trouves_api.py : Ce script interroge l'API SNCF pour extraire les données relatives aux objets perdus dans les gares de Paris. Les données sont ensuite sauvegardées dans un fichier CSV nommé objets_trouves.csv.

    frequentation.py : Ce script extrait les données de fréquentation des gares parisiennes via l'API SNCF et enregistre les résultats dans le fichier frequentation.csv.

    concat.py : Ce script récupère 36 fichiers CSV contenant les données météorologiques téléchargées du site "historique-meteo.net" pour Paris. Il les concatène en un seul fichier CSV nommé all_meteo.csv. Ce fichier est ensuite utilisé pour l'analyse croisée avec les données des objets perdus et de fréquentation.

Méthodologie de traitement des données

Les données sont collectées en mode batch, c'est-à-dire que les différentes années et périodes de données sont récupérées en une seule fois avant d'être traitées. Les données météorologiques sont ensuite associées aux lieux et aux périodes de perte d'objets dans les gares parisiennes, permettant une analyse complète des interactions potentielles entre la météo, la fréquentation des gares et la perte d'objets.
Conclusion

Le script import.py centralise les différentes étapes d'importation et de traitement des données issues des API SNCF et des sources météorologiques. Il assure l'initialisation des dépendances, la gestion des erreurs, et la sauvegarde des résultats pour faciliter l'analyse des données croisées. À l'issue de ce processus, trois fichiers CSV seront générés et enregistrés dans le dossier csv_modélisé. Ces fichiers serviront de base pour le nettoyage des données et l'agrégation à effectuer, ainsi que pour la migration des données vers Azure SQL Database. Ces données fourniront un support solide pour des études approfondies sur les objets perdus dans les gares parisiennes en lien avec la fréquentation et les conditions météorologiques.