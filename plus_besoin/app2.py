############################## HISTOGRAMME OBJETS TROUVES ##########################
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from fonction import plot_histogram, create_map, plot_nb_objets_par_saison_categorie
import streamlit as st
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
#                                            - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                           |           Nombre d'objets perdus entre 2019 et 2022         |
#                                           |                       selon le type                         |
#                                            - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    

df= pd.read_csv("csv/concat.csv")
#renomage des colonnes, etaffichages des champs souhaités pour la sélection multiple
daf=df[['fields.gc_obo_type_c', 'fields.gc_obo_gare_origine_r_name','fields.date']]
daf = df.rename(columns={"fields.gc_obo_type_c": "type", "fields.gc_obo_gare_origine_r_name": "nom_gare", "fields.date": "date"})[['type', 'nom_gare', 'date']]
daf['date'] = daf['date'].str[:10]
tp=daf['type'].value_counts()
list = tp.index.tolist()
list.append('total')              


# on donne le choix d'affichage du nombre d'objets perdus selon le type 
hobby = st.multiselect("Hobbies: ",    
                     list)
if(st.button("voir le graphique")):
    #plot_histogram(daf, hobby)
    fig = plot_histogram(daf, hobby)  # on appelle la fonction histogramme en renseignant le dataframe et le choix sélectionné
    st.plotly_chart(fig)   


#                                            - - - - - - - - - - - - - - - - - - - - - - 
#                                           |                Carte Folium                |
#                                           |                                            |
#                                            - - - - - - - - - - - - - - - - - - - - - -    




df_gare = pd.read_csv("csv/infos_gares.csv")

st.write("Carte de Paris avec le nombre d’objets trouvés en fonction de la fréquentation de voyageur de chaque gare")

st.title("Carte des gares")

# Afficher la carte Folium dans Streamlit
m = create_map(df_gare)
folium_static(m)
# Créer la carte Folium
m = folium.Map(location=[48.856614, 2.3522219], zoom_start=12)



#                                                - - - - - - - - - - - - - - - - - -
#                                               |      Scatterplot interactif      |
#                                               |    Objets trouvés et température |
#                                                - - - - - - - - - - - - - - - - - -     



st.title("Scatterplot du nombre d'objets trouvés selon la tempérautre")


# Connexion à la base de données
connexion = sqlite3.connect('bddt.db')
curseur = connexion.cursor()

# Récupération du nombre d'objets trouvés selon chaque température
curseur.execute("""
                    SELECT meteo.temperature, COUNT(objets_trouves.id) 
                    FROM objets_trouves
                    JOIN meteo ON objets_trouves.date_meteo = meteo.date
                    GROUP BY meteo.temperature
                """)
data = curseur.fetchall()

# insertion dans un dataframe du retour de la requête
df = pd.DataFrame(data, columns=["Temperature", "Nb_Objets"])

# Création du scatter plot avec plotly express
fig = px.scatter(df, x="Temperature", y="Nb_Objets", title="Nombre d'objets perdus selon la température")
st.plotly_chart(fig)
st.write(" D'aprés ce graphique, le nombre d'objets perdus semble corrélé à la température avec beaucoup moins d'objets perdus lorsque les températures sont trés basses ou trés hautes ")
st.write("Cependant la fréquentation n'étant pas la même à chaque température, il est nécessaire de prendre en compte cette variable pour étalir une corrélation")


#                                            - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                           |     Comparatif de la médiane journalière d'objets perdus      |
#                                           |         selon les saisons incluant années de 2019 à 2022      |
#                                            - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
st.title("Comparatif de la médiane journalière d'objets perdus selon les saisons, incluant années de 2019 à 2022 ")
curseur= connexion.cursor()
#requête de tuples affichant la saison et le nombre d'objets perdus, chaque ligne correspondant à une date
curseur.execute("""
                    SELECT saison.saison, COUNT(DISTINCT objets_trouves.id)
                    FROM objets_trouves
                    INNER JOIN saison ON objets_trouves.data = saison.date
                    GROUP BY objets_trouves.data                
                                                
                    """)
temp=curseur.fetchall()
#récupération d'un dictionnaire avec pour chaque saison le nombre d'objets perdus
saisons = {}
for saison, valeur in temp:
    if saison not in saisons:
        saisons[saison] = []
    saisons[saison].append(valeur)
mediane_par_saison = [np.median(valeurs) for saison, valeurs in saisons.items()]      
fig, ax = plt.subplots()
ax.bar(saisons.keys(), mediane_par_saison)

# Ajout de la valeur médiane à l'intérieur de chaque barre
for i, v in enumerate(mediane_par_saison):
    ax.text(i, v + 0.1, str(v), ha='center')


plt.xlabel('Saison')
plt.ylabel('Valeur médiane')
plt.title('Valeur médiane journalière des objets trouvés selon la saison', color='purple')
st.pyplot(fig)

st.write("La médiane journalière d'objets perdus apparaît corrélé avec la saison sur ce graphique")


#                                             - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                           |     Comparatif de la médiane journalière d'objets perdus      |
#                                           |               selon les saisons et les années                 |
#                                             - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -    

st.title("Comparatif de la médiane journalière d'objets perdus selon les saisons, et les années ")



connexion = sqlite3.connect('bddt.db')
curseur = connexion.cursor()

# Récupération des années disponibles
curseur.execute("""
    SELECT DISTINCT strftime('%Y', saison.date)
    FROM saison
""")
annees = [int(x[0]) for x in curseur.fetchall()]

# Sélection de l'année avec un  selectbox
annee = st.selectbox("Sélectionnez une année :", annees)

# Récupération des données correspondant à l'année sélectionnée
curseur.execute("""
    SELECT saison.saison, COUNT(DISTINCT objets_trouves.id)
    FROM objets_trouves
    INNER JOIN saison ON objets_trouves.data = saison.date
    WHERE strftime('%Y', saison.date) = ?
    GROUP BY objets_trouves.data, saison.saison                 
""", (str(annee),))
data = curseur.fetchall()

# Création d'un dataframe Pandas à partir des données récupérées
df = pd.DataFrame(data, columns=['Saison', 'NbObjetsTrouves'])

# Création du graphique en boîte
couleurs = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3']
fig = px.box(df, x='Saison', y='NbObjetsTrouves', color='Saison', color_discrete_sequence=couleurs)
fig.update_layout(title=f"Distribution des objets trouvés par saison en {annee}")

# Affichage du graphique avec Streamlit
st.plotly_chart(fig)


saisons = {}
for saison, valeur in data:
    if saison not in saisons:
        saisons[saison] = []
    saisons[saison].append(valeur)

for saison, valeurs in saisons.items():
    mediane = np.median(valeurs)
    st.write(f"<p style='color: darkslategrey;'>La valeur médiane pour la saison {saison} en {annee} est {mediane}.</p>", unsafe_allow_html=True)

st.write("Les différences de valeur de la médiane journalière selon les saisons entre les années montre la nécessité de mettre en lien cette variable avec la fréquentation pour pouvoir établir une corrélation ")


#                                             - - - - - - - - - - - - - - - - - - - - - - - - - - 
#                                           |         Affichage du nombre d'objets perdus       |
#                                           |      selon la saison et la catégorie d'objet     |
#                                             - - - - - - - - - - - - - - - - - - - - - - - - - -    





connexion=sqlite3.connect('bddt.db')
curseur= connexion.cursor()
    
curseur.execute("""
                    SELECT saison.saison, objets_trouves.typo, COUNT(objets_trouves.id) AS nb_objets
                    FROM objets_trouves
                    JOIN saison ON objets_trouves.date_meteo = saison.date
                    GROUP BY objets_trouves.typo, saison.saison
                     
                    
                    """)
dernier=curseur.fetchall()


st.title("Nombre d\'objets perdus selon la saison et la catégorie d\'objet")

fig = plot_nb_objets_par_saison_categorie(dernier)
st.pyplot(fig)

st.write("Il apparraît une différence du type d'objets perdus dans les gares parisiennes selon les saisons d'aprés ce graphique") 