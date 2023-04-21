import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import folium
import numpy as np
import streamlit as st


def plot_histogram(daf, hobby):
    if 'total' in hobby:
        fig = px.histogram(daf, x='date' , title='Histogramme des objets perdus par semaine', color_discrete_sequence=px.colors.qualitative.Pastel)
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
                font=dict(size=12),
            )
        )
    else:
        fig = px.histogram(daf[daf['type'].isin(hobby)], x='date', nbins=200, title='Histogramme des objets perdus par semaine', color_discrete_sequence=px.colors.qualitative.Pastel)
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
                font=dict(size=12),
            ))
        return fig

def create_map(df_gare):
    

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

    return m




def plot_nb_objets_par_saison_categorie(dernier):
    data = {}
    categories = set([x[1] for x in dernier])
    n_categories = len(categories)
    palette = sns.color_palette(n_colors=n_categories)
    for saison in ['automne', 'hiver', 'printemps', 'été']:
        data[saison] = []
        for categorie in categories:
            objets_saison = [x[2] for x in dernier if x[0] == saison and x[1] == categorie]
            data[saison].append(sum(objets_saison))
    
    n_seasons = len(data)
    bar_width = 0.6 / n_categories
    opacity = 0.8
    index = np.arange(n_seasons)
    for i, categorie in enumerate(categories):
        plt.bar(index + i*bar_width, [data[saison][i] for saison in data], bar_width,
                alpha=opacity, color=palette[i], label=categorie)
    
    plt.xlabel('Saison')
    plt.ylabel('Nombre d\'objets')
    plt.title('Nombre d\'objets par saison et par catégorie')
    plt.xticks(index + bar_width*6, ['Automne', 'Hiver', 'Printemps', 'Été'])
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.gcf().set_size_inches(10, 6)
    
    fig = plt.gcf()
    return fig