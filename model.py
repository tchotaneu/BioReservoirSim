from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(X, y):
    """
    Nous allons entraîner un modèle Random Forest pour prédire le label de croissance bactérienne
    à partir des concentrations en nutriments.

    Args:
        X: variables explicatives (nutriments)
        y: variable cible (0 ou 1)

    Returns:
        clf: modèle entraîné
        acc: précision sur l’ensemble de test
    """
    # Séparation du jeu de données en ensemble d’entraînement et de test (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Création du modèle Random Forest
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    # Prédiction sur l’ensemble de test
    y_pred = clf.predict(X_test)

    # Évaluation de la précision
    acc = accuracy_score(y_test, y_pred)

    return clf, acc
