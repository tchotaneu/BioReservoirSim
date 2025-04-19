import matplotlib.pyplot as plt
from data_generator import generate_data
from model import train_model

df = generate_data()
X = df[["nutrient_A", "nutrient_B", "nutrient_C"]]
y = df["label"]

clf, acc = train_model(X, y)

plt.scatter(df["nutrient_A"], df["response"], c=df["label"], cmap="coolwarm")
plt.title(f"Bacterial Response Simulation (accuracy={acc:.2f})")
plt.xlabel("Nutrient A")
plt.ylabel("Response")
plt.colorbar(label="Label")
plt.show()
