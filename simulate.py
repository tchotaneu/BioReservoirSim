import numpy as np

def bacterial_response(nutrient_A, nutrient_B, nutrient_C, a=2.5, b=1.0, c=3.0):
    """
    Calcule une réponse biologique simulée à partir de 3 nutriments.
    
    Args:
        nutrient_A, nutrient_B, nutrient_C: concentrations des nutriments (float)
        a, b, c: coefficients simulant la sensibilité de la bactérie à chaque nutriment

    Returns:
        response: valeur de croissance simulée
    """
    # Réponse linéaire au nutriment A
    term1 = a * nutrient_A

    # Réponse quadratique au nutriment B
    term2 = b * (nutrient_B ** 2)

    # Réponse non linéaire (sinusoïdale) au nutriment C
    term3 = c * np.sin(nutrient_C * np.pi)

    # Somme des 3 termes = réponse finale
    response = term1 + term2 + term3

    return response
