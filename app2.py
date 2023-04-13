############################## HISTOGRAMME OBJETS TROUVES ##########################
import streamlit as st
import pandas as pd
import plotly.express as px


df= pd.read_csv("csv/concat.csv")

daf=df[['fields.gc_obo_type_c', 'fields.gc_obo_gare_origine_r_name','fields.date']]
daf.rename(columns={"fields.date":"date"},inplace=True)
daf.rename(columns={"fields.gc_obo_type_c":"type"},inplace=True)
daf.rename(columns={"fields.gc_obo_gare_origine_r_name":"nom_gare"},inplace=True)
# daf['date'] = daf['date'].str.slice(stop=10)
daf['date']=daf['date'].apply(lambda x : x [:10])



tp=daf['type'].value_counts()
list=[]
for i in tp.index:
    list.append(i)

list.append('total')                  #integration de liste deroulante de tous les types d'objets perdus


hobby = st.multiselect("Hobbies: ",    # je donne le choix du type objet perdu
                     list)

if(st.button("voir le graphique")):
    if 'total' in hobby:
            
        fig = px.histogram( daf, x='date' , title='Histogramme des objets perdus par semaine', color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_xaxes(
            tickangle=90,
            tickformat="%b %Y",
            dtick="W1",
            ticklabelmode="period"
        )
        
        fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=12),
    bargap=0.2,
    bargroupgap=0.1,
    barmode='overlay',
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    xaxis=dict(
        title='Date',
        titlefont=dict(size=14),
        tickfont=dict(size=12),
        tickformat="%b %Y",
        dtick="W1",
        ticklabelmode="period"
    ),
    yaxis=dict(
        title='Nombre d\'objets perdus',
        titlefont=dict(size=14),
        tickfont=dict(size=12),
    ),
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            size=12,
        ),
    )
)


    # Afficher le graphique
        fig.show()
    else:
    # selection= tp.loc[tp['sports'] == hobby, 'type'].values[0]
        fig = px.histogram( daf[daf['type'].isin(hobby)], x='date' ,nbins=200, title='Histogramme des objets perdus par semaine', color_discrete_sequence=px.colors.qualitative.Pastel)
        fig.update_xaxes(
            tickformat="%b %Y",
            dtick="W1",
            ticklabelmode="period"
        )
        
        fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=12),
    bargap=0.2,
    bargroupgap=0.1,
    barmode='overlay',
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    xaxis=dict(
        title='Date',
        titlefont=dict(size=14),
        tickfont=dict(size=12),
        tickformat="%b %Y",
        dtick="W1",
        ticklabelmode="period"
    ),
    yaxis=dict(
        title='Nombre d\'objets perdus',
        titlefont=dict(size=14),
        tickfont=dict(size=12),
    ),
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            size=12,
        ),
    )
)
        # Afficher le graphique
        fig.show()
        
        

############################ MAP FOLIUM #######################################

import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

df_gare = pd.read_csv("infos_gares.csv")

# Créer la carte Folium
m = folium.Map(location=[48.856614, 2.3522219], zoom_start=12)

for i in range(len(df_gare)):
    nom_gare = df_gare.loc[i, "nom_gare"]
    frequent_2019 = df_gare.loc[i, "frequent_2019"]
    frequent_2020 = df_gare.loc[i, "frequent_2020"]
    frequent_2021 = df_gare.loc[i, "frequent_2021"]
    lat = df_gare.loc[i, "lat"]
    long = df_gare.loc[i, "long"]
        
    objet_trouve_2019 = df_gare.loc[i,"objet_trouve_2019"]
    objet_trouve_2020 = df_gare.loc[i,"objet_trouve_2020"]
    objet_trouve_2021 = df_gare.loc[i,"objet_trouve_2021"]
    objet_trouve_2022 = df_gare.loc[i,"objet_trouve_2022"]
    
    popup_text = f"Nom de la gare: {nom_gare}<br>Fréquentation en 2019: {frequent_2019:,.0f}<br>Fréquentation en 2020: {frequent_2020:,.0f}<br>Fréquentation en 2021: {frequent_2021:,.0f}<br>Objet trouvé en 2019: {objet_trouve_2019:,.0f}<br>Objet trouvé en 2020: {objet_trouve_2020:,.0f}<br>Objet trouvé en 2021: {objet_trouve_2021:,.0f}<br>Objet trouvé en 2022: {objet_trouve_2022:,.0f}"
    
    marker = folium.Marker(location=[lat, long], radius=2, fill=True)
    popup = folium.Popup(popup_text, max_width=300)
    
    marker.add_child(popup)
    marker.add_to(m)

# Afficher la carte Folium dans Streamlit
folium_static(m)



import sqlite3
connexion=sqlite3.connect('bddt.db')
curseur= connexion.cursor()
    
curseur.execute("""
                    SELECT saison.saison, objets_trouves.typo, COUNT(objets_trouves.id) AS nb_objets
                    FROM objets_trouves
                    JOIN saison ON objets_trouves.date_meteo = saison.date
                    GROUP BY objets_trouves.typo, saison.saison
                     
                    
                    """)
dernier=curseur.fetchall()



########################## HISTOGRAMME OBJETS/SAISON ############################
    
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Votre code pour la création de votre graphique
data = {}
categories = set([x[1] for x in dernier])
#là t'as une liste de toutes les catégories qui ont été créé
n_categories = len(categories)
#reprend le nombre de types différent d'objets
palette = sns.color_palette(n_colors=n_categories)
#on demande une couleur pr chaque entité de catégorie
for saison in ['automne', 'hiver', 'printemps', 'été']:
    data[saison] = []
    #on crée une nouvelle clé (ds le dico "data" pr chaque saison)
    for categorie in categories:
        #on itére sur chaque catégorie à partir de la saison>> [ex: automne-appareil photo puis jouet etc]
        objets_saison = [x[2] for x in dernier if x[0] == saison and x[1] == categorie]
        #x[2]>> correspond au nombre d'objets pr chaque cat
        #ainsi si [x catégorie] = saison qu'on itére T0, et à la catégorie, on l'ajoute à la liste 
        #on itére sur chaque ligne: 
        # if objets_saison:
        data[saison].append(sum(objets_saison))
        #on fait la somme du nbre d'objets de la liste de automne/jouets (par ex)
       
        # else:
        #     data[saison].append(0)

# Créer les barres groupées
n_seasons = len(data)
bar_width = 0.6 / n_categories
opacity = 0.8
index = np.arange(n_seasons)
#variable est utilisée pour positionner les barres sur l'axe des x lors de la création du graphique à barres
for i, categorie in enumerate(categories):
    plt.bar(index + i*bar_width, [data[saison][i] for saison in data], bar_width,
            alpha=opacity, color=palette[i], label=categorie)

# Personnaliser le graphique
plt.xlabel('Saison')
plt.ylabel('Nombre d\'objets')
plt.title('Nombre d\'objets par saison et par catégorie')
plt.xticks(index + bar_width*6, ['Automne', 'Hiver', 'Printemps', 'Été'])
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.gcf().set_size_inches(10, 6)

# Afficher le graphique avec Streamlit
# Si vous ne souhaitez pas voir ce message d'avertissement
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(plt.show())



######################## SCATTERPLOT OBJETS TROUVES TEMPERATURE ####################""

import streamlit as st
import sqlite3 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Connexion à la base de données
connexion = sqlite3.connect('bddt.db')
curseur = connexion.cursor()

# Récupération des données depuis la base de données
curseur.execute("""
                    SELECT meteo.temperature, COUNT(objets_trouves.id) 
                    FROM objets_trouves
                    JOIN meteo ON objets_trouves.date_meteo = meteo.date
                    GROUP BY meteo.temperature
                """)
data = curseur.fetchall()

# Transformation des données en DataFrame pandas
df = pd.DataFrame(data, columns=["Temperature", "Nb_Objets"])

# Création du scatter plot avec plotly express
fig = px.scatter(df, x="Temperature", y="Nb_Objets", title="Nombre d'objets perdus selon la température")

# Affichage de la figure avec streamlit
st.plotly_chart(fig)


# import streamlit as st
# import sqlite3 
# import pandas as pd
# import numpy as np
# import plotly.express as px

# # Connexion à la base de données
# connexion = sqlite3.connect('bddt.db')
# curseur = connexion.cursor()

# # Récupération des données de la base de données
# curseur.execute("""
#     SELECT saison.saison, COUNT(DISTINCT objets_trouves.id)
#     FROM objets_trouves
#     INNER JOIN saison ON objets_trouves.data = saison.date
#     GROUP BY objets_trouves.data, saison.saison                 
# """)
# data = curseur.fetchall()

# # Création d'un dataframe Pandas à partir des données récupérées
# df = pd.DataFrame(data, columns=['Saison', 'NbObjetsTrouves'])

# # Dictionnaire qui reprend, pour chaque saison, une valeur d'objets trouvés par jour
# saisons = {}
# for saison, valeur in data:
#     if saison not in saisons:
#         saisons[saison] = []
#     saisons[saison].append(valeur)



# # Création du graphique en boîte
# couleurs = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3']
# fig = px.box(df, x='Saison', y='NbObjetsTrouves', color='Saison', color_discrete_sequence=couleurs)
# fig.update_layout(title="Distribution des objets trouvés par saison")

# # Affichage du graphique avec Streamlit
# st.plotly_chart(fig)

# # À partir du dictionnaire, reprise de la valeur médiane (à partir des valeurs de chaque saison)
# for saison, valeurs in saisons.items():
#     mediane = np.median(valeurs)
#     st.write(f"La valeur médiane pour la saison {saison} est {mediane}.")


import sqlite3 
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Connexion à la base de données
connexion = sqlite3.connect('bddt.db')
curseur = connexion.cursor()

# Récupération des années disponibles
curseur.execute("""
    SELECT DISTINCT strftime('%Y', saison.date)
    FROM saison
""")
annees = [int(x[0]) for x in curseur.fetchall()]

# Sélection de l'année avec un widget selectbox
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

# À partir du dictionnaire, reprise de la valeur médiane (à partir des valeurs de chaque saison)
saisons = {}
for saison, valeur in data:
    if saison not in saisons:
        saisons[saison] = []
    saisons[saison].append(valeur)

for saison, valeurs in saisons.items():
    mediane = np.median(valeurs)
    st.write(f"La valeur médiane pour la saison {saison} en {annee} est {mediane}.")
