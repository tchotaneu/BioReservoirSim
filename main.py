import matplotlib.pyplot as plt
from data_generator import generate_data
from mpl_toolkits.mplot3d import Axes3D  # nécessaire pour le support 3D
from model import train_model
import plotly.express as px
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
plt.title(f"TITRE : Simulation de la réponse bactérienne (Précision = {acc:.2f})")
plt.xlabel("Concentration du nutriment A")
plt.ylabel("Réponse bactérienne simulée")
plt.colorbar(label="Classe de croissance (0 = faible, 1 = forte)")
plt.grid(True)
plt.savefig("simulation_result.png", dpi=300)
print("Graphe enregistré dans 'simulation_result.png'")


# Création de la figure 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Tracé 3D : Nutrient A (X), Nutrient B (Y), Response (Z)
scatter = ax.scatter(
    df["nutrient_A"],
    df["nutrient_B"],
    df["response"],
    c=df["label"],
    cmap="coolwarm",
    edgecolors='k'
)

# Titre et axes
ax.set_title("TITRE: 3D Simulation dela reponse de la  Bacterie")
ax.set_xlabel("Nutrient A")
ax.set_ylabel("Nutrient B")
ax.set_zlabel("Response")

# Légende des couleurs
legend1 = ax.legend(*scatter.legend_elements(), title="Label", loc="upper right")
ax.add_artist(legend1)

# Affichage et sauvegarde
plt.tight_layout()
plt.savefig("3D_simulation_resultat.png", dpi=300)
#plt.show()

print("Graphique 3D enregistré dans '3D_simulation_resultat.png'")

# Crée une figure 3D interactive avec Plotly
fig = px.scatter_3d(
    df,
    x="nutrient_A",
    y="nutrient_B",
    z="response",
    color="label",
    color_continuous_scale="RdBu",
    title="Bacterial Response - Interactive 3D View",
    labels={"nutrient_A": "Nutrient A", "nutrient_B": "Nutrient B", "response": "Simulated Response"}
)

# Affiche la figure dans le navigateur
fig.show()

# Enregistrement du graphique en fichier html
fig.write_html("interactive_3D_response.html")
print("Graphique interactif enregistré dans 'interactive_3d_response.html'")
