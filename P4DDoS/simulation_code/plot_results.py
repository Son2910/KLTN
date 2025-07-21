import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

plt.figure(figsize=(8,6))

for method in df["Method"].unique():
    subset = df[df["Method"]==method]
    plt.plot(subset["Attack"], subset["Accuracy"].astype(float), marker="o", label=method)

plt.xlabel("Attack traffic proportion (%)")
plt.ylabel("Detection Accuracy")
plt.ylim(0,1.05)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("accuracy_comparison.png")
plt.show()
