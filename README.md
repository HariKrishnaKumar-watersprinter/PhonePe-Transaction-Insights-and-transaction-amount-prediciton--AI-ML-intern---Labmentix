PhonePe Transaction Insights: Data Engineering & Predictive Analytics


📊 Project Overview
This project is an end-to-end Data Science and Business Intelligence solution designed to analyze the PhonePe Pulse GitHub data. It transforms raw, nested JSON data into a structured SQL database, performs rigorous data wrangling, and applies advanced Machine Learning techniques to decode transaction dynamics, user engagement, and insurance penetration across India.

The final output is an interactive Streamlit Dashboard that serves as a one-stop solution for strategic decision-making, offering insights into market expansion, customer segmentation, and predictive growth analytics.

🎯 Problem Statement
With the increasing reliance on digital payment systems like PhonePe, understanding the dynamics of transactions, user engagement, and insurance-related data is crucial for improving services and targeting users effectively. The raw data is locked in complex, nested JSON formats across various geographical hierarchies. This project aims to:

Decentralize Data: Convert unstructured JSON into a queryable SQL database.
Analyze Trends: Identify growth patterns, seasonal trends, and regional disparities.
Predict Future Growth: Use Machine Learning to forecast transaction volumes.
Segment Markets: Cluster states/districts for targeted marketing.
🛠️ Tech Stack
Language: Python 3.9+
Database: MySQL / PostgreSQL
Libraries:
Data Manipulation: Pandas, NumPy
Visualization: Plotly, Matplotlib, Seaborn
Machine Learning: Scikit-learn, XGBoost, LightGBM
Database Connector: SQLAlchemy, MySQL Connector
Dashboarding: Streamlit

## 🚀 Approach & Methodology

### 1. Data Extraction (ETL)
The PhonePe Pulse data is structured in a complex directory format (`Aggregated`, `Map`, `Top`). A robust Python script was developed to:
*   Traverse the directory tree for States, Years, and Quarters.
*   Parse nested JSON structures to extract metrics (Count, Amount).
*   Load data into **9 normalized SQL tables**.

### 2. Data Transformation & Wrangling
*   **Merging:** Created **2 Master Tables** (`master_state_data`, `master_district_data`) by joining transaction, user, and insurance tables for holistic analysis.
*   **Cleaning:** Handled missing values, standardized state/district names (Title Case), and corrected data types.

### 3. Exploratory Data Analysis (EDA)
Conducted analysis on:
*   **Transaction Dynamics:** Year-over-year growth and seasonal spikes (Q4 peaks).
*   **Insurance Penetration:** Correlation between digital transactions and insurance adoption.
*   **Device Dominance:** Market share of mobile brands among PhonePe users.

### 4. Machine Learning Implementation
Implemented a robust pipeline with Cross-Validation and Hyperparameter Tuning:
*   **Regression Models:** Linear Regression, XGBoost, LightGBM to predict future transaction volume.
*   **Clustering (K-Means):** Segmented states into "High Value", "Growing", and "Dormant".
*   **Anomaly Detection (Isolation Forest):** Identified statistical outliers for potential fraud detection.

### 5. Statistical Hypothesis Testing
Validated key business assumptions using rigorous statistical tests:
*   **Pearson Correlation:** Validated the correlation between user count and transaction amount.
*   **T-Test:** Compared performance between Southern and Northern states.
*   **ANOVA:** Confirmed the statistical significance of seasonality across quarters.

## 📈 Key Insights
1.  **Seasonality:** Q4 (October-December) consistently records the highest transaction volumes, correlating with festive seasons.
2.  **Regional Leaders:** Southern states (Karnataka, Maharashtra, Tamil Nadu) dominate in transaction value, while Northern states show high growth potential.
3.  **Insurance Gap:** States with high transaction volumes do not always have proportional insurance adoption, indicating a massive cross-selling opportunity.

## 🖥️ Dashboard Features
The Streamlit application provides an interactive interface with multiple modules:
1.  **Home:** Executive summary with Key Performance Indicators (KPIs).
2.  **Strategic Insights:** Visualizations of transaction, insurance, and user trends.
3.  **ML Analytics:** 
    *   View Customer Segmentation maps.
    *   Identify Anomalies/Fraud outliers.
    *   Predict future transaction volume using the trained model.
4.  **Geographical Analysis:** Treemaps for state/district-wise market expansion strategies.

## ⚙️ Installation & Usage

### Prerequisites
*   Python 3.8 or higher
*   MySQL Server (or PostgreSQL)

### Steps to Run

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/phonepe-insights.git
    cd phonepe-insights
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Setup Database**
    *   Create a database named `phonepe_pulse` in your SQL server.
    *   Update the connection string in `etl_pipeline.py`, `app.py`, and `ml_pipeline_advanced.py` with your credentials:
      ```python
      engine = create_engine("mysql+mysqlconnector://root:your_password@localhost:3306/phonepe_pulse")
      ```

4.  **Run ETL Pipeline**
    *   Ensure you have the PhonePe Pulse data folder in the project directory.
    ```bash
    python etl_pipeline.py
    ```

5.  **Run Data Wrangling & ML Training**
    ```bash
    python data_wrangling.py
    python ml_pipeline_advanced.py
    ```

6.  **Launch Dashboard**
    ```bash
    streamlit run app.py
    ```

## 🧪 Statistical Validation Results
| Hypothesis | Test Used | P-Value | Conclusion |
| :--- | :--- | :--- | :--- |
| **User Count vs Transaction Amount** | Pearson Correlation | < 0.001 | Significant positive correlation confirmed. |
| **Southern vs Northern States** | Welch's T-Test | < 0.05 | Southern states statistically outperform Northern states. |
| **Quarterly Seasonality** | ANOVA | < 0.05 | Significant difference exists across quarters. |

## 💡 Future Scope
*   Integrate live API data for real-time analytics.
*   Develop a recommendation engine for merchants based on transaction history.
*   Deploy the dashboard on cloud platforms (AWS/Azure) for public access.

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgements
*   **PhonePe Pulse** for providing the open-source data.
*   **Streamlit** for the easy-to-use dashboarding framework.
