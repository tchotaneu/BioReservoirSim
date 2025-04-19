import numpy as np
import pandas as pd
from simulate import bacterial_response  # 🧠 Importation de la fonction centrale

def generate_data(n_samples=200, noise=0.1):
    """
    Génère un jeu de données de milieux nutritifs et leur réponse bactérienne simulée.
    """
    np.random.seed(42)

    # Génération aléatoire des concentrations de 3 nutriments
    nutrients = np.random.rand(n_samples, 3)

    # Calcul de la réponse pour chaque combinaison de nutriments
    response = np.array([
        bacterial_response(a, b, c)
        for a, b, c in nutrients
    ])

    # Ajout de bruit aléatoire pour simuler la variabilité expérimentale
    response += np.random.normal(0, noise, size=response.shape)

    # Création des étiquettes binaires selon la médiane
    labels = (response > np.median(response)).astype(int)

    # Création d’un DataFrame pour stocker les résultats
    df = pd.DataFrame(nutrients, columns=["nutrient_A", "nutrient_B", "nutrient_C"])
    df["response"] = response
    df["label"] = labels

    return df
