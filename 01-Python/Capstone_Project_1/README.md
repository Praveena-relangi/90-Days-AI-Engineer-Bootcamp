# 📊 Capstone Project 1 - SuperStore Sales Data Analysis

An end-to-end Data Analytics project developed using **Python**, **Pandas**, and **Matplotlib** as part of the **90 Days AI Engineer Bootcamp**.

This project demonstrates the complete data analysis lifecycle, from understanding raw business data to generating actionable business insights through visualizations.

---

# 📌 Table of Contents

- Project Overview
- Business Problem Statement
- Business Requirements
- Project Objectives
- Dataset Information
- Technology Stack
- Project Structure
- Project Workflow
- Key Business Insights
- Visualizations
- Skills Demonstrated
- How to Run the Project
- Future Improvements
- Conclusion

---

# 📖 Project Overview

Retail businesses generate thousands of sales transactions every day.

Without proper analysis, it becomes difficult to answer questions such as:

- Which products generate the highest revenue?
- Which regions perform the best?
- Which customer segment contributes the most sales?
- Which states and cities are the strongest markets?

This project analyzes historical SuperStore sales data and converts raw data into meaningful business insights.

---

# 💼 Business Problem Statement

The management team of SuperStore wants to better understand its sales performance.

Although thousands of sales transactions are available, the raw dataset does not clearly reveal:

- Which product categories are performing well
- Which regions contribute the highest revenue
- Which customer segments are most valuable
- Which states and cities generate maximum sales
- Which products drive overall business growth

The management requires a detailed sales analysis report supported by visualizations to help make data-driven business decisions.

---

# 🎯 Business Requirements

The business requires answers to the following questions:

1. What is the total sales revenue?

2. Which product category generates the highest sales?

3. Which region performs the best?

4. Which customer segment contributes the most revenue?

5. Which states generate the highest sales?

6. Which cities generate the highest sales?

7. Which products generate the highest sales?

8. Present the findings using easy-to-understand charts.

---

# 🎯 Project Objectives

- Explore the dataset.
- Clean and validate the data.
- Perform Exploratory Data Analysis (EDA).
- Generate meaningful business insights.
- Visualize important findings.
- Document the complete analysis process.

---

# 📂 Dataset Information

| Attribute | Value |
|-----------|-------|
| Dataset | SuperStore Dataset |
| Rows | 9800 |
| Columns | 18 |
| Missing Values | 11 (Postal Code) |
| Duplicate Rows | 0 |

---

# 🛠 Technology Stack

- Python
- Pandas
- Matplotlib
- VS Code

---

# 📁 Project Structure

```text
Capstone_Project_1
│
├── Images
│   ├── sales_by_category.png
│   ├── sales_by_region.png
│   ├── sales_by_segment.png
│   ├── top_10_states.png
│   ├── top_10_cities.png
│   └── top_10_products.png
│
├── Reports
│   ├── Final_Report.md
│   ├── Phase1_Data_Exploration_Report.md
│   ├── Phase2_Data_Cleaning_Report.md
│   ├── Phase3_Exploratory_Data_Analysis_Report.md
│   └── Phase4_Data_Visualization_Report.md
│
├── Data_analysis.py
├── Data_cleaning.py
├── exploratory_data_analysis.py
├── Data_visualisation.py
├── SuperStore_Dataset.csv
├── requirements.txt
└── notes.md
```

---

# 🔄 Project Workflow

```
Raw Dataset
      │
      ▼
Data Exploration
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Data Visualization
      │
      ▼
Business Insights
      │
      ▼
Documentation
```

---

# 📊 Key Business Insights

- Total Sales: **$2.26 Million**

- Highest Performing Category:
  - Technology

- Highest Performing Region:
  - West

- Highest Performing Customer Segment:
  - Consumer

- Highest Revenue State:
  - California

- Highest Revenue City:
  - New York City

- Highest Revenue Product:
  - Canon imageCLASS 2200 Advanced Copier

---

# 📈 Visualizations

## Sales by Category

![Sales by Category](Images/sales_by_category.png)

---

## Sales by Region

![Sales by Region](Images/sales_by_region.png)

---

## Sales by Customer Segment

![Sales by Segment](Images/sales_by_segment.png)

---

## Top 10 States by Sales

![Top States](Images/top_10_states.png)

---

## Top 10 Cities by Sales

![Top Cities](Images/top_10_cities.png)

---

## Top 10 Products by Sales

![Top Products](Images/top_10_products.png)

---

# 🚀 Skills Demonstrated

- Python Programming
- Pandas Data Analysis
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Business Analytics
- Documentation
- Problem Solving

---

# ▶️ How to Run

Clone the repository.

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project files phase by phase:

```bash
python Data_analysis.py
```

```bash
python Data_cleaning.py
```

```bash
python exploratory_data_analysis.py
```

```bash
python Data_visualisation.py
```

---

# 🔮 Future Improvements

The current project focuses only on **Sales** analysis.

Future versions can include:

- Profit Analysis
- Quantity Analysis
- Discount Analysis
- Customer Retention Analysis
- Interactive Power BI Dashboard
- Machine Learning Sales Prediction

---

# 🏁 Conclusion

This project demonstrates an end-to-end Data Analytics workflow using Python.

Starting from raw sales data, the project explores, cleans, analyzes, visualizes, and documents business insights that can help stakeholders make informed decisions.

This capstone also serves as a strong portfolio project demonstrating practical data analysis skills using Python, Pandas, and Matplotlib.