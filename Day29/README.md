# Day 29 — Machine Learning Foundations (README)

## 1. What is Machine Learning?

Machine Learning (ML) is a way of building software where the computer learns patterns from data instead of being given fixed rules.

Traditional Programming:
Rules + Data → Output

Machine Learning:
Data + Correct Outputs → Model learns Rules → Predicts new outputs

The goal of ML is generalization — the ability to perform well on unseen data, not just the data it studied.

---

## 2. Types of Machine Learning

### 2.1 Supervised Learning

The model is trained using labeled data (inputs with correct answers).
It learns a mapping function from input → output.

Common tasks:

* Classification (Spam or Not Spam, Pass/Fail, Disease detection)
* Regression (House price prediction, Sales forecasting)

Key idea: The model learns by comparing its predictions to the correct answers and reducing the error.

---

### 2.2 Unsupervised Learning

The model receives only data without correct answers and must discover patterns on its own.

Common tasks:

* Clustering customers by behavior
* Grouping similar products
* Detecting abnormal activity

Key idea: Find structure in unknown data.

---

### 2.3 Reinforcement Learning

An agent learns by interacting with an environment using rewards and penalties.

Examples:

* Game playing AI
* Self-driving systems
* Robotics movement learning

Key idea: Learn optimal decisions through trial and error.

---

## 3. Dataset Splitting — Train vs Test

A dataset must be divided into two parts:

Training Set (usually 70–80%)
Used to teach the model patterns.

Testing Set (usually 20–30%)
Used to evaluate how well the model works on unseen data.

Why needed?
Because a model that memorizes training data is useless in real life.
We want learning, not memorization.

---

## 4. Overfitting and Underfitting

### Overfitting

The model learns the training data too perfectly, including noise.
Result: Excellent training performance but poor real-world performance.

Signs:

* Very high training accuracy
* Low testing accuracy

Cause:
Model too complex or dataset too small

---

### Underfitting

The model is too simple and fails to learn meaningful patterns.

Signs:

* Low training accuracy
* Low testing accuracy

Cause:
Model lacks capacity to learn relationships

---

### Ideal Model

Learns general patterns that apply to new unseen data.
Balanced performance on training and testing sets.

---

## 5. Machine Learning Workflow

1. Collect Data
2. Clean Data (handle missing values)
3. Convert categorical values into numbers
4. Split dataset (train/test)
5. Train model
6. Make predictions
7. Evaluate performance

---

## 6. Features and Target

Features: Input columns used for prediction
Target: Output column we want to predict

Example:
Predict survival
Features → age, gender, ticket class
Target → survived or not

---

## 7. Model Evaluation

Accuracy:
Percentage of correct predictions made by the model.

Good accuracy depends on the problem. For beginner datasets ~65–80% is reasonable.

---

## 8. What You Achieved Today

By completing Day 29 you have learned:

* How ML differs from traditional programming
* Types of machine learning
* Why datasets are split
* Overfitting vs underfitting
* Basic ML workflow
* How a model makes predictions on new data

This marks the transition from programming logic to data-driven problem solving.
