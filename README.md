# BioReservoirSim – Simulateur de biosenseur bactérien

Ce projet propose une **simulation d’un système de Reservoir Computing bactérien** inspiré de l’article [_Reservoir Computing with Bacteria_ (2024)](https://www.biorxiv.org/content/10.1101/2024.09.12.612674v1).  
L’idée est de modéliser **la réponse phénotypique d’une bactérie à des environnements nutritionnels** et d'utiliser cette réponse comme source de calcul pour des tâches de classification.

---

##  Visualisation interactive

 Explorez la réponse simulée en 3D selon les nutriments A et B :

 [Voir la simulation interactive](https://tchotaneu.github.io/BioReservoirSim/interactive_3D_response.html)

---

## Structure du projet

```
BioReservoirSim/
├── app.py                       # Lancer l'application localement avec streamlit 
├── 2D_simulation_result.png     # Visualisation 2D 
├── 3D_simulation_resultat.png   # Visualisation 3D 
├── biosensor_dataset.csv        # fichier de données sauvegardé 
├── data_generator.py            # Génération des profils nutritionnels et réponses simulées
├── model.py                     # Entraînement d’un modèle de classification
├── main.py                      # Script principal : simulation + visualisation
├── interactive_3D_response.html # Visualisation interactive 3D avec Plotly
├── requirements.txt             # Dépendances Python
├── README.md                    # Documentation du projet
```

---

## Méthodologie

1. **Génération de données**  
   - 3 nutriments aléatoires (A, B, C) → combinaison d'effets (linéaire, quadratique, sinus).
   - Simulation d’une **réponse bactérienne** (croissance) avec bruit aléatoire.

2. **Classification**  
   - Création d’un label binaire : `1` (réponse forte), `0` (réponse faible).
   - Entraînement d’un modèle **Random Forest** pour classer les réponses à partir des nutriments.

3. **Visualisation**
   - Graphe 2D (matplotlib) et 3D (matplotlib 3D).
   - Version **interactive en 3D** avec Plotly pour une exploration enrichie.

---

##  Lancer le projet

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Exécuter le script principal
```bash
python main.py
```

---

### 3. Interface Streamlit

Ce projet inclut une interface interactive développée avec [Streamlit](https://streamlit.io/), permettant de :

- Régler le niveau de bruit biologique simulé,
- Choisir le nombre d’échantillons,
- Visualiser les réponses phénotypiques des bactéries simulées,
- Afficher les performances du modèle de classification (Random Forest),
- Explorer les données générées dynamiquement.

### 4. Lancer l'application localement
```bash
streamlit run app.py
```

##  Auteur

**Giresse Tchotaneu**  
passionné par la bioinformatique, l’intelligence artificielle appliquée au vivant, et les systèmes hybrides .

Contact : [giressetchotaneu@gmail.com]  
GitHub : [https://github.com/tchotaneu](https://github.com/tchotaneu)

---

##  Licence

Projet libre sous licence MIT.