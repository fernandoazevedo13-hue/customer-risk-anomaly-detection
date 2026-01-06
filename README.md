Customer Risk & Anomaly Detection Pipeline
📌 Project Overview

This project implements an end-to-end analytical pipeline designed to identify customer risk, behavioral anomalies, and churn patterns using real-world datasets from Kaggle. The solution follows a layered data architecture (Bronze, Silver, and Gold), enabling scalable data ingestion, data quality treatment, feature engineering, and analytical modeling.

The objective is to simulate a real business scenario where data-driven insights support decision-making related to customer retention, operational risk, and anomaly detection.

🎯 Business Problem

Organizations that manage large customer bases often struggle to proactively identify:

Customers at high risk of churn

Abnormal behavioral patterns

Sudden changes in usage or financial indicators

Operational risks hidden in historical data

This project addresses these challenges by transforming raw customer data into actionable insights and risk indicators.

🧱 Data Architecture

The pipeline follows a Bronze / Silver / Gold architecture:

Bronze: Raw data ingestion (original Kaggle dataset, unchanged)

Silver: Cleaned and standardized data with data quality rules applied

Gold: Analytical dataset enriched with features, risk scores, and anomaly flags

Bronze → Silver → Gold → Analytics & Dashboards


This structure improves data traceability, reproducibility, and scalability.

📊 Data Source

Source: Kaggle Datasets

Type: Customer behavior / churn data

Volume: Thousands of customer records

Format: CSV

The dataset contains customer attributes, usage metrics, contractual information, and churn indicators.

🔧 Technologies & Tools

Python (pandas, numpy, scikit-learn)

SQL (DuckDB / SQLite)

Streamlit (interactive analytical dashboard)

Power BI (executive-level dashboard)

Kaggle (data source)

⚙️ Project Structure

customer-risk-anomaly-detection/
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── src/
│   ├── ingest.py
│   ├── clean.py
│   ├── features.py
│   ├── anomaly_detection.py
│   └── utils.py
│
├── notebooks/
│   └── 01_eda.ipynb
│
├── dashboard/
│   ├── streamlit_app.py
│   └── powerbi/
│       └── customer_risk.pbix
│
├── requirements.txt
├── README.md
└── .gitignore


📈 Dashboards & Insights
Streamlit (Analytical Dashboard)

Interactive filters

Anomaly visualization

Customer segmentation

Risk score exploration

Live App: (add Streamlit Cloud URL here)

Power BI (Executive Dashboard)

Key business KPIs

Churn and risk overview

Segment-level analysis

Visual storytelling for decision-makers
