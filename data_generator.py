import numpy as np
import pandas as pd

def generate_data(n_samples=200, noise=0.1):
    np.random.seed(42)
    nutrients = np.random.rand(n_samples, 3)  # 3 types de nutriments
    a, b, c = 2.5, 1.0, 3.0  # sensibilité fictive
    response = a * nutrients[:,0] + b * nutrients[:,1]**2 + c * np.sin(nutrients[:,2]*np.pi)
    response += np.random.normal(0, noise, size=response.shape)

    labels = (response > np.median(response)).astype(int)  # classons comme "forte" ou "faible" croissance

    df = pd.DataFrame(nutrients, columns=["nutrient_A", "nutrient_B", "nutrient_C"])
    df["response"] = response
    df["label"] = labels
    return df
