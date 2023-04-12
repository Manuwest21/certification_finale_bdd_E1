# import pandas as pd
# import plotly.express as px


# df= pd.read_csv("csv/concat.csv")
# daf=df[['fields.gc_obo_type_c', 'fields.gc_obo_gare_origine_r_name','fields.date']]
# daf.rename(columns={"fields.date":"date"},inplace=True)
# daf.rename(columns={"fields.gc_obo_type_c":"type"},inplace=True)
# daf.rename(columns={"fields.gc_obo_gare_origine_r_name":"nom_gare"},inplace=True)
# # daf['date'] = daf['date'].str.slice(stop=10)
# # daf['date']=daf['date'].apply(lambda x : x [:10])
# daf['date'] = pd.to_datetime(daf['date'])
# daf

# st.write("ici le graphique")
# st.radio("Select gender:", ("male", "fem"))
# fig = px.histogram(daf, x='date', nbins=200, title='histo objectttttts')
# fig.update_xaxes(
#     tickformat="%b %Y",
#     dtick="W1",
#     ticklabelmode="period"
# )

# # Afficher le graphique
# fig.show()