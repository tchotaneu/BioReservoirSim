# 🧬 BioReservoirSim – Simulateur de biosenseur bactérien

Bienvenue sur mon projet de simulation d’un système de *Reservoir Computing* biologique, inspiré de l'article _[Reservoir Computing with Bacteria](https://www.biorxiv.org/content/10.1101/2024.09.12.612674v1).  

Ce mini projet a pour but de **modéliser la réponse de bactéries (ex. E. coli) à des profils nutritionnels**, et d’utiliser ces réponses simulées pour effectuer des tâches de **classification** avec des modèles d’intelligence artificielle.

---

##  Objectifs

- Reproduire, en Python, le principe du *Bacterial Reservoir Computing*.
- Simuler la **réponse phénotypique (croissance)** à des milieux de culture définis par 3 nutriments.
- Entraîner un modèle IA à partir de ces réponses simulées (ex : Random Forest).
- Visualiser le comportement du système avec des **graphiques 2D et 3D** (dont une version interactive).

---

## Visualisation interactive

Explorez la simulation de croissance bactérienne en 3D directement dans votre navigateur :

 **[Cliquez ici pour voir le graphe interactif](./interactive_3d_response.html)**

Vous pouvez faire pivoter, zoomer, et survoler les points pour obtenir des informations (nutriments, réponse, classe...).

---

##  Structure du projet
BioReservoirSim/ ├── data_generator.py # Génération des profils nutritionnels et réponses simulées ├── model.py # Entraînement d’un modèle de classification ├── main.py # Script principal : simulation + visualisation ├── interactive_3d_response.html # Visualisation interactive en 3D avec Plotly ├── requirements.txt # Dépendances Python ├── README.md # Documentation du projet 
