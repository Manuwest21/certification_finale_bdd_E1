Projet SNCF : analyse des objets perdus et de la luminosité
1. Présentation Générale
Introduction du Projet

La SNCF a fait appel à notre expertise pour résoudre un problème récurrent : la fréquence élevée des objets perdus dans ses gares, un problème majeur pour les passagers et pour la logistique interne de gestion des réclamations. Ce projet vise à analyser la relation entre le nombre d'objets perdus et les conditions de luminosité météorologique.

L'objectif principal est d'explorer l'hypothèse selon laquelle des facteurs liés à la luminosité influenceraient la concentration des voyageurs et entraîneraient une hausse des pertes d'objets. Pour cela, nous allons étudier les données des gares parisiennes, qui constituent un échantillon significatif en termes de fréquentation, ainsi que des données météorologiques de la ville de Paris, afin d'analyser ces relations.
2. Objectifs Fonctionnels et Techniques
Objectifs Fonctionnels

    Analyse des tendances des objets perdus : Étudier les facteurs associés à la luminosité et leur impact potentiel sur les pertes d'objets dans les gares.
    Gestion efficace des données : Fournir une base de données structurée permettant d'analyser le lien entre luminosité, fréquentation des gares et pertes d'objets.
    Accès simplifié aux données : Développer une interface utilisateur intuitive pour consulter ces données et les résultats d’analyse.

Objectifs Techniques

    Base de données SQL Azure : Mise en place d'une base de données cloud pour stocker les données des objets perdus et des conditions météorologiques.
    Scripts d'extraction et d'intégration : Développer des scripts pour extraire, nettoyer et intégrer les données de l’API SNCF et des fichiers météorologiques CSV.
    API REST sécurisée : Créer une API REST avec authentification pour permettre un accès sécurisé aux données analysées.

3. Structure du Projet
Données Recueillies

    Objets perdus : Données récupérées via l'API SNCF.
    Fréquentation des gares : En se concentrant sur les gares parisiennes.
    Données météorologiques : Luminosité, temps, et autres variables environnementales pour la ville de Paris.

Processus Technique

    Création et gestion d'une base de données : Utilisation de SQL Azure pour centraliser les données d'objets perdus et de météo.
    Scripts d'intégration : Développement de scripts pour automatiser le nettoyage et l'intégration des données en provenance de différentes sources.
    Pondération par fréquentation : Ajustement des analyses par le nombre de voyageurs dans chaque gare afin de normaliser les résultats.
    API REST sécurisée : Fournir un accès simplifié et sécurisé aux données via une interface pour les utilisateurs autorisés.

4. Technologies Utilisées

    Environnement de Développement :
        Visual Studio Code (VSCode) : IDE utilisé pour écrire et exécuter le code.

    Langages :
        Python (3.10.12) : Langage de programmation principal pour le développement de l'application.
        SQL : Utilisé pour interagir avec SQLite3 et Azure SQL.

    Bibliothèques :
        pandas : Pour le nettoyage, la transformation et l’agrégation des données.
        pyodbc : Pour la connexion et l'interaction avec la base de données Azure SQL.
        dotenv : Pour sécuriser les informations sensibles via des variables d'environnement.
        jose : Pour la création et la vérification des tokens JWT.
        pydantic : Pour la modélisation et la validation automatique des données.

    Modules :
        requests : Pour envoyer des requêtes HTTP afin de récupérer des données depuis l'API SNCF.
        os : Pour la gestion des fichiers locaux, y compris la manipulation des fichiers CSV.
        FastAPI : Framework pour la création d'une API REST, permettant des fonctionnalités CRUD.

    Bases de Données :
        SQLite3 : Pour le stockage temporaire des données, permettant du feature engineering avant la migration vers Azure SQL.
        Azure SQL Database : Pour un accès cloud aux données avec des niveaux d'accès restreints via authentification, et chiffrement des connexions.

5. Conclusion

Ce projet permettra à la SNCF de mieux comprendre les facteurs influençant la perte d'objets dans ses gares, tout en offrant une solution centralisée et efficace pour la gestion et l'analyse des données. Les résultats pourraient améliorer la gestion des réclamations et potentiellement réduire le nombre d'objets perdus grâce à des recommandations spécifiques basées sur les conditions environnementales, comme la luminosité.
