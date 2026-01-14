import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "research_plots"
PLOTS_DIR.mkdir(exist_ok=True)


features = ["Age", "Income", "Education", "Experience"]
importance = [0.25, 0.40, 0.20, 0.15]

plt.barh(importance, features, color='yellow')
plt.ylabel("Importance Score")
plt.title("Feature Importance")

plt.savefig(PLOTS_DIR / 'feature_importance.png', dpi=300, bbox_inches="tight")
plt.show()
plt.close()
