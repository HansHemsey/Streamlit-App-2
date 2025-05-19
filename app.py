import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titre principal de l'application (affiché en haut de la page)
st.title("Manipulation de données et création de graphique")

# Liste des noms des datasets
options = ['flights', 'taxis', 'iris']

# menu déroulant pour le choix du dataset
selection = st.selectbox("Quel dataset veux-tu utiliser", options) 

# initialisation du df avec la selection
url = f"https://raw.githubusercontent.com/mwaskom/seaborn-data/master/{selection}.csv"
df = pd.read_csv(url)

# affichage du df sous forme de tableau 
st.dataframe(df)

# choix des colonnes X et Y
column_options = df.columns.tolist()

# menu déroulant pour le choix de la colonne X
x_selection = st.selectbox("Choisissez la colonne X", column_options) 

# menu déroulant pour le choix de la colonne Y
y_selection = st.selectbox("Choisissez la colonne Y", column_options) 

# menu déroulant pour le choix du graphique
charts = ['Bar Chart', 'Scatter Plot', 'Line Chart']
chart_selection = st.selectbox("Quel graphique veux-tu utiliser ?", charts) 

# paramètres des figures
fig, ax = plt.subplots(figsize=(10, 6))

# affichage du graphique selon le choix de l'utilisateur
try:
    if chart_selection == 'Bar Chart':
        sns.barplot(x=x_selection, y=y_selection, data=df, ax=ax)
    elif chart_selection == 'Scatter Plot':
        sns.scatterplot(x=x_selection, y=y_selection, data=df, ax=ax)
    else:  # Line Chart
        sns.lineplot(x=x_selection, y=y_selection, data=df, ax=ax)
    
    plt.xlabel(x_selection)
    plt.ylabel(y_selection)
    plt.title(f"{chart_selection} de {y_selection} vs {x_selection}")
    plt.tight_layout()
    st.pyplot(fig)
except Exception as e:
    st.error(f"Erreur lors de la création du graphique: {e}")
    st.write("Astuce: Certaines colonnes peuvent ne pas être compatibles entre elles pour certains types de graphiques.")

# case à cocher pour la matrice de corrélation
corr_box = st.checkbox(label="Afficher la matrice de corrélation")

if corr_box:
    # paramètres des figures
    fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
    
    # calculer la matrice de corrélation (seulement pour les colonnes numériques)
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax_corr)
        plt.title("Matrice de corrélation")
        plt.tight_layout()
        st.pyplot(fig_corr)
    else:
        st.write("Pas de données numériques pour créer une matrice de corrélation")
else:
    st.write('___')