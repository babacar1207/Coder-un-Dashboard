import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 
from pandas import DataFrame
import csv

colonnes = ['ville', 'lieen']

# création du tableau qui doit contenir les liens
tableau = DataFrame(columns = colonnes)
path = 'dataset/liensVilles.csv'
tableau.to_csv(path, index=False)

dico = {}
dico['ville'] = ''
dico['lien'] = ''

lien = "https://www.journaldunet.com/management/ville/index/villes?page=1"

with open(path, 'a', encoding='utf8') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=colonnes, lineterminator='\n')
    req = requests.get(lien)
    contenu = req.content
    soup = bs(contenu, "html.parser")

    touslesLiens = soup.findAll('a')

    for lien in touslesLiens:
        if '/ville-' in lien['href']:
            dico['lien'] = lien ['href']
            dico['ville'] = lien.text

        write.writerow(dico)