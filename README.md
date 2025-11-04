# ❤️ Heart Disease Prediction using Logistic Regression
<div align="center">
  <img src="images/Output 1.PNG" width="40%"/>
  <img src="images/output 2.PNG" width="36%"/>
</div>
A predictive machine learning project using **Logistic Regression** to assess the likelihood of heart disease based on patient health indicators.  
This project demonstrates **data preprocessing, model building, evaluation, and deployment** — showcasing essential skills for data science and analytics roles.

---

## 🔍 Project Overview

Heart disease remains one of the leading causes of death globally.  
The goal of this project is to develop a **logistic regression model** that can accurately predict the presence of heart disease using medical attributes such as age, cholesterol level, blood pressure, and more.

This project highlights practical experience in **healthcare data analysis**, **classification modeling**, and **interpretable ML** for data-driven decision-making.

---

## 📈 Results & Model Performance

| Metric | Score |
|:-------|:------:|
| **Accuracy** | 87.5% |
| **Precision** | 0.82 |
| **Recall** | 0.90 |
| **F1-Score** | 0.86 |
| **ROC AUC** | 0.92 |

> The model demonstrates strong predictive power and effective classification performance, indicating its capability to identify potential heart disease risk factors with good reliability.

---

## ⚙️ Project Workflow

1. **Data Cleaning & Preparation**  
   - Handle missing values and categorical encoding  
   - Feature scaling and normalization  

2. **Exploratory Data Analysis (EDA)**  
   - Identify relationships between features and target variable  
   - Visualize feature distributions using Seaborn and Matplotlib  

3. **Model Training**  
   - Train Logistic Regression model using scikit-learn  
   - Tune hyperparameters and evaluate with validation sets  

4. **Evaluation & Interpretation**  
   - Metrics: Accuracy, Precision, Recall, F1-Score, ROC Curve  
   - Feature importance interpretation via model coefficients  

5. **Deployment (Optional)**  
   - Flask-based web app for live prediction (can be integrated later)  

---

## 🧰 Technologies & Libraries Used

| Category | Tools |
|-----------|-------|
| **Programming Language** | Python |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn |
| **Model Saving** | Pickle / Joblib |
| **IDE / Environment** | Jupyter Notebook, VS Code |

---

## 📂 Folder Structure

Heart_Disease_Prediction_using_Log_regression/

├── dataset.csv

├── heart_disease_analysis.ipynb

├── app.py

├── heart_disease_model.pkl

├── templates

│ ├── index.html

├── requirements.txt # Dependencies

└── README.md # Project documentation


---

## 🚀 How to Run the Project

 1️⃣ Clone the Repository  
```bash
git clone https://github.com/UK183/Heart_Disease_Prediction_using_Log_regression.git
cd Heart_Disease_Prediction_using_Log_regression
```

2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Run the Notebook
```bash
jupyter notebook notebooks/heart_disease_analysis.ipynb
```

---
# 🧠 Key Learnings

- Built a binary classification model using logistic regression

- Enhanced understanding of feature importance and interpretability in healthcare ML

- Strengthened skills in data cleaning, visualization, and evaluation metrics

- Improved ability to design reproducible ML pipelines

# ⚠️ Disclaimer: 
This project is for educational and portfolio purposes only.
It is not intended for clinical or diagnostic use without professional validation.
