import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_generator import generate_data
from model import train_model

# Titre de l'application
st.title(" BioReservoirSim – Simulateur de Biosenseur Bactérien")

# Slider pour régler le bruit dans les données
noise = st.slider("Niveau de bruit biologique", min_value=0.0, max_value=1.0, value=0.1, step=0.05)

# Nombre d'échantillons à générer
n_samples = st.number_input("Nombre d’échantillons", min_value=50, max_value=1000, value=200, step=50)

# Générer les données
df = generate_data(n_samples=n_samples, noise=noise)
X = df[["nutrient_A", "nutrient_B", "nutrient_C"]]
y = df["label"]

# Entraîner le modèle
model, acc = train_model(X, y)

st.write(f"📊 Précision du modèle (Random Forest) : **{acc:.2f}**")

# Afficher les données sous forme de tableau
if st.checkbox("Afficher les données brutes"):
    st.dataframe(df)

# Graphique de la réponse
st.subheader("Réponse simulée de la bactérie")
fig, ax = plt.subplots()
scatter = ax.scatter(df["nutrient_A"], df["response"], c=df["label"], cmap="coolwarm", edgecolors='k')
ax.set_xlabel("Nutrient A")
ax.set_ylabel("Réponse simulée (croissance)")
ax.set_title("Réponse de la bactérie en fonction des nutriments")
st.pyplot(fig)
