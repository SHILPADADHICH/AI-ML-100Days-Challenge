import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "research_plots"
PLOTS_DIR.mkdir(exist_ok=True)

cm = np.array([[50, 5],
               [3, 42]])

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.savefig(PLOTS_DIR / 'confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()