import numpy as np
import pandas as pd

def generate_data(n_samples=200, noise=0.1):
    """
    Nous allons génèrer un jeu de données aleatoire représentant des milieux de culture
    et la réponse phénotypique d'une bactérie à ces milieux.

    Args:
        n_samples: nombre d’échantillons à générer
        noise: niveau de bruit aléatoire (pour simuler la variabilité biologique)

    Returns:
        df: DataFrame avec les nutriments, la réponse simulée et l’étiquette (label)
    """
    np.random.seed(42)  # Pour des résultats reproductibles

    # Génère aléatoirement les concentrations de 3 nutriments (valeurs entre 0 et 1)
    nutrients = np.random.rand(n_samples, 3)

    # Définition arbitraire de l'influence de chaque nutriment sur la croissance
    a, b, c = 2.5, 1.0, 3.0
    response = (
        a * nutrients[:, 0] +                    # effet linéaire du nutriment A
        b * nutrients[:, 1]**2 +                 # effet quadratique du nutriment B
        c * np.sin(nutrients[:, 2] * np.pi)      # effet non-linéaire du nutriment C
    )

    # Ajout de bruit aléatoire pour simuler le "bruit biologique"
    response += np.random.normal(0, noise, size=response.shape)

    # Création de labels : 0 = faible croissance, 1 = forte croissance
    labels = (response > np.median(response)).astype(int)

    # Création du DataFrame final
    df = pd.DataFrame(nutrients, columns=["nutrient_A", "nutrient_B", "nutrient_C"])
    df["response"] = response
    df["label"] = labels

    return df
