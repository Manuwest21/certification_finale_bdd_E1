import pandas as pd

# insertion d'un champ de donnée "saison" quia ssocie chaque jour à une saison

df= pd.read_csv("concat.csv")
daf=df[['fields.gc_obo_type_c', 'fields.gc_obo_gare_origine_r_name','fields.date']]
daf.rename(columns={"fields.date":"date"},inplace=True)
daf.rename(columns={"fields.gc_obo_type_c":"type"},inplace=True)
daf.rename(columns={"fields.gc_obo_gare_origine_r_name":"nom_gare"},inplace=True)
# daf['date'] = daf['date'].str.slice(stop=10)
daf['saison']=daf['date'].apply(lambda x : x [5:10])
daf['date']=daf['date'].apply(lambda x : x [0:10])

# # # daf['date'] = pd.to_datetime(daf['date'])
daf['saison']=daf['saison'].str.replace("-","")
# # daf['date']=daf['date'][0].replace("0","")
# # daf['date']=daf['date'].apply(lambda x:x[0])
# # if daf['date'][0]=='0':
daf['saison'] = daf['saison'].apply(lambda x: x.lstrip('0') if x.startswith('0') else x)
daf['saison']=daf['saison'].astype('int')

def conversion_saison(date=int):
    if 321<=date <=620:
        return "printemps"
    elif 621<=date <=922:
        return "été"
    elif 923<=date <=1220:
        return "automne"
    elif 1221<=date<=1231 or 0<=date <=320:
        return "hiver"
#on met la saison
daf['saison']=daf['saison'].apply(conversion_saison)