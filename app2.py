import pandas as pd
import plotly.express as px
import streamlit as st

df= pd.read_csv("concat.csv")
daf=df[['fields.gc_obo_type_c', 'fields.gc_obo_gare_origine_r_name','fields.date']]
daf.rename(columns={"fields.date":"date"},inplace=True)
daf.rename(columns={"fields.gc_obo_type_c":"type"},inplace=True)
daf.rename(columns={"fields.gc_obo_gare_origine_r_name":"nom_gare"},inplace=True)
# daf['date'] = daf['date'].str.slice(stop=10)
daf['date']=daf['date'].apply(lambda x : x [:10])
daf


tp=daf['type'].value_counts()
list=[]
for i in tp.index:
    list.append(i)

list.append('total')                  #integration de liste deroulante de tous les types d'objets perdus


hobby = st.multiselect("Hobbies: ",    # je donne le choix du type objet perdu
                     list)

if(st.button("voir le graphique")):
    if 'total' in hobby:
        
    # for index, row in tp.iterrows():
    #     if index==hobby:
    #         z=row['type']

    # dff = daf.loc[daf['type'] == hobby]    
    # for index, value in tp.items():
    #     if index==hobby:
    #         z=value
            
        fig = px.histogram( daf, x='date' , title='Histogramme des objets perdus par semaine')
        fig.update_xaxes(
            tickformat="%b %Y",
            dtick="W1",
            ticklabelmode="period"
        )

    # Afficher le graphique
        fig.show()
    else:
    # selection= tp.loc[tp['sports'] == hobby, 'type'].values[0]
        fig = px.histogram( daf.loc[daf['type'] == hobby], x='date' ,nbins=200, title='Histogramme des objets perdus par semaine')
        fig.update_xaxes(
            tickformat="%b %Y",
            dtick="W1",
            ticklabelmode="period"
        )

        # Afficher le graphique
        fig.show()

#je veux créer un df qui reprendra daf[date] et qui associera 




# tp = daf['type'].value_counts()
# hobbies = tp.index.tolist()

# hobby = st.selectbox("Hobbies: ", hobbies)

# z = 'type'  # utilise la colonne 'type' pour l'axe y
# for index, value in tp.items():
#     if index == hobby:
#         z = value

# fig = px.histogram(daf, x='date', y='type', nbins=200, title='Histogramme des objets perdus par semaine')
# fig.update_xaxes(
#     tickformat="%b %Y",
#     dtick="W1",
#     ticklabelmode="period"
# )

# fig.show()