# Day 12 – Research Plots & Visualization Gallery
100 Days of AI/ML Challenge

## Objective
Understand and implement visualization techniques commonly used in AI/ML research papers.  
Learn how to present model performance clearly and organize plots professionally.

---

## Time Breakdown
- Understanding research plots: 30 min
- Coding & plotting: 1.5–2 hrs
- Folder organization + README: 45 min
- Review & reflection: 15 min

---

## Part 1: Research Plots – Conceptual Understanding

### 1. Accuracy vs Epoch
- Shows how model accuracy improves over training
- Helps detect underfitting or overfitting
- Common in deep learning papers

### 2. Loss vs Epoch
- Shows how training error decreases
- Used to verify model convergence
- Helps detect unstable training

### 3. Confusion Matrix
- Shows correct vs incorrect predictions
- More informative than accuracy
- Used in classification problems

### 4. Feature Importance
- Shows which features impact predictions the most
- Helps with model interpretability
- Common in tree-based models

---

## Part 2: Implementation Tasks

### Folder Structure
Create the following structure:

Day10/
├── research_plots/
│   ├── accuracy_vs_epoch.png
│   ├── loss_vs_epoch.png
│   ├── confusion_matrix.png
│   ├── feature_importance.png
├── README.md

---

### Plot 1: Accuracy vs Epoch
- Create dummy epoch data
- Plot accuracy using Matplotlib
- Add title, x-label, y-label
- Save plot in `research_plots/`

---

### Plot 2: Loss vs Epoch
- Use dummy loss values
- Plot loss curve
- Label axes clearly
- Save plot

---

### Plot 3: Confusion Matrix
- Create dummy classification results
- Plot heatmap using Seaborn
- Add labels for actual vs predicted
- Save plot

---

### Plot 4: Feature Importance
- Create dummy feature names and scores
- Plot horizontal bar chart
- Label axes
- Save plot

---

## Part 3: Visualization Gallery (README.md)

In README.md, document:

### For each plot:
- Plot name
- Library used (Matplotlib / Seaborn)
- Purpose of the plot (1–2 lines)

---

## Part 4: Review Questions

Answer briefly:
1. Which plot helps detect overfitting?
2. Why is confusion matrix better than accuracy?
3. Which plots are used only in classification?
4. Which plots help understand model learning?

---

## Final Checklist
- [ ] All 4 research plots created
- [ ] Plots saved correctly
- [ ] Folder structure clean
- [ ] README.md updated
- [ ] Concepts understood

---

## Outcome
By completing Day 10C, you can:
- Understand plots used in ML research papers
- Explain model performance visually
- Organize plots professionally
- Complete Day 10 of the AI/ML Challenge
