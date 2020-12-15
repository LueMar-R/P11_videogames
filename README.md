# P11_videogames
Analyzes sales data from more than 16,500 games


## Dataset
Source sur [Kaggle](https://www.kaggle.com/gregorut/videogamesales)

__Infos générales sur la table :__

```
RangeIndex: 16598 entries, 0 to 16597
Data columns (total 11 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Rank          16598 non-null  int64  
 1   Name          16598 non-null  object 
 2   Platform      16598 non-null  object 
 3   Year          16327 non-null  float64
 4   Genre         16598 non-null  object 
 5   Publisher     16540 non-null  object 
 6   NA_Sales      16598 non-null  float64
 7   EU_Sales      16598 non-null  float64
 8   JP_Sales      16598 non-null  float64
 9   Other_Sales   16598 non-null  float64
 10  Global_Sales  16598 non-null  float64
dtypes: float64(6), int64(1), object(4)
```

__Prétraitement des données :__
  - traitement des valeurs manquantes (remplacement pas "Unknown" pour _Publisher_ et suppression des lignes concernées pour _Year_ (soit 1.6% des entrées supprimées)
  - modification du format de _Year_ en 'int'
  - création de 3 tables intermédiaires pour les données qualitatives suivantes : Genre (12 valeurs uniques), Platform (31) et Publisher (578)
  - export des données prétraitées en csv.

Voir le code python du traitement des données dans le notebook en [annexe 1]()

On obtient 4 fichiers csv : la table principale des ventes et les tables Genre, Platform et Publisher


