# 📚 Capstone Project 1 – Notes

## Project

SuperStore Sales Data Analysis

---

# Dataset Information

- Rows : 9800
- Columns : 18
- Dataset Size : 1.3 MB

---

# Python Libraries Used

- pandas
- matplotlib

---

# Phase 1 – Data Exploration

## Concepts Learned

- read_csv()
- head()
- tail()
- shape
- columns
- dtypes
- info()
- describe()

## Findings

- Dataset contains 9800 rows.
- Dataset contains 18 columns.
- Only Postal Code contains missing values.
- Sales column is numeric.
- Order Date and Ship Date are initially stored as strings.

---

# Phase 2 – Data Cleaning

## Concepts Learned

- isnull()
- sum()
- duplicated()
- drop_duplicates()
- to_datetime()

## Findings

- Postal Code contains 11 missing values.
- Duplicate rows = 0.
- Order Date converted to datetime.
- Ship Date converted to datetime.
- Burlington (Vermont) Postal Code could not be inferred from the dataset.
- Missing Postal Code values were intentionally preserved.

---

# Phase 3 – Exploratory Data Analysis (EDA)

## Concepts Learned

- unique()
- nunique()
- groupby()
- sort_values()
- head()

## Business Questions Answered

- Total Sales
- Number of Categories
- Sales by Category
- Sales by Region
- Sales by Customer Segment
- Top States
- Top Cities
- Top Products

---

# Phase 4 – Data Visualization

## Concepts Learned

- plt.figure()
- plt.bar()
- plt.title()
- plt.xlabel()
- plt.ylabel()
- plt.xticks()
- plt.tight_layout()
- plt.savefig()
- plt.show()

## Charts Created

- Sales by Category
- Sales by Region
- Sales by Customer Segment
- Top 10 States
- Top 10 Cities
- Top 10 Products

---

# Major Business Insights

- Total Sales exceeded $2.26 Million.
- Technology generated the highest sales.
- West region generated the highest revenue.
- Consumer segment contributed the highest sales.
- California generated the highest state-wise sales.
- New York City generated the highest city-wise sales.
- Canon imageCLASS 2200 Advanced Copier generated the highest product sales.

---

# Lessons Learned

- Always explore data before analysis.
- Never assume missing values should be filled.
- Investigate missing values before making cleaning decisions.
- Visualizations make business insights easier to understand.
- Documentation is as important as coding.