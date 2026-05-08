# 📱 PhonePe Transaction Insights & Transaction Amount Prediction
Deployed link:https://phonepeanalysis.streamlit.app/

An end-to-end **FinTech Data Analytics and Machine Learning Project** that analyzes India's digital payment ecosystem using the **PhonePe Pulse dataset** and predicts transaction amounts using advanced regression models.

This project combines:

- 📊 Interactive Data Analytics Dashboard
- 🗺️ Geo-spatial Transaction Visualization
- 🤖 Machine Learning Prediction Models
- 🧠 Business Intelligence Insights
- ⚡ Streamlit Web Application
- 🗄️ MySQL Database Integration

---

# 🚀 Project Overview

Digital payment systems generate massive volumes of transactional data every second. Understanding this data is critical for:

- Identifying transaction trends
- Understanding user engagement
- Predicting transaction growth
- Improving financial accessibility
- Supporting strategic business decisions

This project leverages the publicly available **PhonePe Pulse dataset** to perform:

✅ Data Extraction  
✅ Data Cleaning & Transformation  
✅ SQL Data Warehousing  
✅ Exploratory Data Analysis  
✅ Interactive Visualization  
✅ Transaction Amount Prediction using ML Models

---

# 🎯 Problem Statement

With the rapid growth of UPI and digital payments in India, businesses need intelligent systems to:

- Analyze transaction patterns
- Identify high-performing regions
- Understand customer behavior
- Detect growth opportunities
- Predict future transaction amounts

Traditional dashboards provide historical summaries but lack predictive intelligence.

This project solves that challenge by integrating:

- Advanced analytics
- Predictive machine learning
- Interactive visualization
- Business intelligence reporting

to transform raw transaction data into actionable insights.

---

# 🏗️ Project Architecture

```text
PhonePe Pulse Dataset
        │
        ▼
Data Extraction (JSON Files)
        │
        ▼
Data Cleaning & Transformation
        │
        ▼
MySQL Database Storage
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Machine Learning Models
        │
        ▼
Streamlit Interactive Dashboard
        │
        ▼
Business Insights & Predictions
```

---

# 📂 Dataset Information

This project uses the official **PhonePe Pulse** open-source dataset.

### Dataset Includes

- Aggregated Transactions
- User Engagement Data
- Insurance Transactions
- District-wise Statistics
- State-wise Metrics
- Quarterly Transaction Information

### Dataset Categories

## 1️⃣ Aggregated Data

Contains:

- Transaction Type
- Transaction Count
- Transaction Amount

## 2️⃣ Map Data

Contains:

- District-wise Transactions
- User Activity
- Insurance Metrics

## 3️⃣ Top Data

Contains:

- Top States
- Top Districts
- Top Pincodes

---

# 🛠️ Tech Stack

| Category | Technologies Used |
|---|---|
| Programming Language | Python |
| Database | MySQL |
| Data Processing | Pandas, NumPy |
| Data Visualization | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Machine Learning | Scikit-learn, XGBoost, LightGBM |
| Version Control | Git & GitHub |
| IDE | VS Code / Jupyter Notebook |

---

# 🔥 Key Features

## 📊 Interactive Analytics Dashboard

- State-wise transaction analysis
- Quarterly transaction trends
- Insurance analytics
- User engagement metrics
- Dynamic filtering options

---

## 🗺️ Geo-Spatial Visualization

- Interactive India choropleth maps
- Regional transaction comparison
- State-level growth analysis

---

## 🤖 Machine Learning Prediction

Implemented multiple regression models:

### 📈 Linear Regression

Used for establishing baseline prediction performance.

#### Features

- Simple and interpretable
- Fast training
- Suitable for linear relationships

---

### ⚡ XGBoost Regressor

Advanced gradient boosting algorithm optimized for performance.

#### Features

- Handles complex non-linear relationships
- High prediction accuracy
- Robust against overfitting
- Excellent for structured/tabular data

---

### 🚀 LightGBM Regressor

Efficient gradient boosting framework designed for speed and scalability.

#### Features

- Faster training
- Lower memory usage
- High scalability
- Excellent for large datasets

---

# 📌 Machine Learning Workflow

```text
Data Collection
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train-Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Prediction & Deployment
```

---

# 📊 Exploratory Data Analysis (EDA)

The project includes:

## ✅ Univariate Analysis

- Distribution of transaction amounts
- User registration trends
- Insurance growth patterns

## ✅ Bivariate Analysis

- Transaction count vs amount
- User engagement vs transactions
- Quarter-wise comparisons

## ✅ Multivariate Analysis

- Regional transaction behavior
- Payment category trends
- Multi-feature correlation analysis

---

# 📉 Model Evaluation Metrics

The regression models are evaluated using:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

# 💡 Business Insights Generated

The dashboard helps identify:

✅ High transaction states  
✅ Fast-growing digital regions  
✅ Insurance adoption trends  
✅ User engagement patterns  
✅ Regional market opportunities  
✅ Transaction growth forecasting

---

# 📸 Dashboard Modules

## 🏠 Home Dashboard

- KPI metrics
- Total transaction overview
- User statistics

---

## 📈 Transaction Analysis

- State-wise analysis
- Quarterly growth trends
- Category distribution

---

## 👥 User Engagement Analysis

- Registered users
- App opens
- User activity trends

---

## 🛡️ Insurance Analysis

- Insurance transaction patterns
- Growth opportunities
- Regional adoption insights

---

## 🤖 Transaction Prediction

- ML-powered transaction amount prediction
- Real-time prediction interface
- Comparative model performance

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/HariKrishnaKumar-watersprinter/PhonePe-Transaction-Insights-and-transaction-amount-prediciton--AI-ML-intern---Labmentix.git
```

---

## 2️⃣ Navigate to Project Directory

```bash
cd PhonePe-Transaction-Insights-and-transaction-amount-prediciton--AI-ML-intern---Labmentix
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure MySQL Database

Create database:

```sql
CREATE DATABASE phonepe_db;
```

Update database credentials in configuration files.

---

## 5️⃣ Run Streamlit Application

```bash
streamlit run app.py
```

---

# 📁 Project Structure

```text
📦 PhonePe Transaction Insights
│
├── data/
├── notebooks/
├── exported_csv/
├── models/
├── dashboard/
├── sql/
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

# 📊 Future Enhancements

- 🔍 Fraud Detection System
- 📱 Mobile Responsive Dashboard
- ☁️ Cloud Deployment
- 📈 Real-time Streaming Analytics
- 🤖 Deep Learning Models
- 🔔 Smart Financial Recommendations
- 📡 API Integration

---

# 🧠 Skills Demonstrated

## Data Analytics

- Data Cleaning
- EDA
- Data Visualization
- Business Intelligence

## Machine Learning

- Regression Modeling
- Model Evaluation
- Feature Engineering
- Predictive Analytics

## Software Engineering

- Streamlit Development
- Database Integration
- Modular Code Structure
- End-to-End Deployment

---

# 📈 Business Impact

This project can help financial organizations:

- Improve strategic planning
- Optimize digital payment services
- Identify high-growth markets
- Enhance customer engagement
- Forecast transaction behavior
- Support data-driven decisions

---

# 🏆 Project Highlights

✅ End-to-End FinTech Analytics Solution  
✅ Interactive Streamlit Dashboard  
✅ Real-world Financial Dataset  
✅ Machine Learning Integration  
✅ SQL + Python + Visualization  
✅ Geo-Spatial Analytics  
✅ Business Intelligence Reporting

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- FinTech analytics
- Large-scale data processing
- Machine learning regression
- Dashboard development
- Business insight generation
- Data storytelling
- Predictive modeling

---

# 🙌 Acknowledgements

Special thanks to:

- PhonePe Pulse Dataset
- Streamlit
- Scikit-learn
- XGBoost
- LightGBM

---

# 👨‍💻 Author

## Hari Krishna Kumar

📌 Data Science & AI/ML Enthusiast  
📌 Passionate about FinTech Analytics & Machine Learning  
📌 Interested in Data-Driven Product Development

---

# ⭐ If You Found This Project Useful

Please consider:

✅ Starring the repository  
✅ Forking the project  
✅ Sharing feedback  
✅ Connecting on LinkedIn

---

# 📌 Repository Link

https://github.com/HariKrishnaKumar-watersprinter/PhonePe-Transaction-Insights-and-transaction-amount-prediciton--AI-ML-intern---Labmentix
