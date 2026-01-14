from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
BASE_DIR = Path(__file__).resolve().parent

# Create research_plots inside Day12 directory
PLOTS_DIR = BASE_DIR / "research_plots"
PLOTS_DIR.mkdir(exist_ok=True)

epochs = range(1, 11)
accuracy = [0.55, 0.60, 0.65, 0.70, 0.74, 0.78, 0.82, 0.85, 0.87, 0.89]
# Plotting the accuracy over epochs
plt.plot(epochs, accuracy, marker ='o')
plt.title('Model Accuracy over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.savefig(PLOTS_DIR / 'model_accuracy.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close()

