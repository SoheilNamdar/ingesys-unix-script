import pandas as pd
import matplotlib.pyplot as plt

# Lire les données depuis un fichier Excel
df = pd.read_excel('data.ods', sheet_name='Sheet1')

# Afficher les premières lignes du DataFrame pour vérifier les données
print(df.head())

# Tracer les données
#plt.figure(figsize=(10, 6))
#plt.plot(df['A'], df['B'], marker='o', linestyle='-', color='b')

# Ajouter des titres et des étiquettes
#plt.title('Graphique des données de A vs B')
#plt.xlabel('A')
#plt.ylabel('B')

# Afficher la grille
#plt.grid(True)

# Afficher le graphique
#plt.show()
