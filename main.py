import matplotlib.pyplot as plt
from data_generator import generate_data
from model import train_model

# Génération du jeu de données synthétique
df = generate_data()

# Sélection des variables explicatives (nutriments)
X = df[["nutrient_A", "nutrient_B", "nutrient_C"]]

# Variable cible (étiquette : croissance faible ou forte)
y = df["label"]

# Entraînement du modèle IA (Random Forest)
clf, acc = train_model(X, y)

# Visualisation de la réponse simulée
plt.scatter(df["nutrient_A"], df["response"], c=df["label"], cmap="coolwarm", edgecolors='k')
plt.title(f"Bacterial Response Simulation (Accuracy = {acc:.2f})")
plt.xlabel("Nutrient A concentration")
plt.ylabel("Simulated bacterial response")
plt.colorbar(label="Growth label (0 = low, 1 = high)")
plt.grid(True)
plt.show()
