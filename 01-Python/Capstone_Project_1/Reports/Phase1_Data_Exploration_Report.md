# 📊 Capstone Project 1
## Phase 1 – Data Exploration Report

---

## Project Information

**Project Name:** SuperStore Sales Data Analysis

**Dataset:** SuperStore_Dataset.csv

**Phase:** 1 – Data Exploration

---

# Objective

The objective of Phase 1 is to understand the dataset before performing any data cleaning, analysis, or visualization.

---

# Dataset Overview

| Metric | Value |
|---------|------:|
| Number of Rows | 9800 |
| Number of Columns | 18 |
| Memory Usage | 1.3 MB |

---

# Dataset Columns

```
Row ID
Order ID
Order Date
Ship Date
Ship Mode
Customer ID
Customer Name
Segment
Country
City
State
Postal Code
Region
Product ID
Category
Sub-Category
Product Name
Sales
```

---

# Data Types

| Data Type | Count |
|-----------|------:|
| Integer | 1 |
| Float | 2 |
| String | 15 |

---

# Missing Values

| Column | Missing Values |
|---------|---------------:|
| Postal Code | 11 |

### Observation

- Only the **Postal Code** column contains missing values.
- All other columns contain complete data.

---

# Statistical Summary (Numeric Columns)

## Sales

| Metric | Value |
|---------|-------:|
| Minimum | 0.444 |
| Maximum | 22638.480 |
| Average | 230.769 |
| Median | 54.490 |

---

## Postal Code

| Metric | Value |
|---------|-------:|
| Minimum | 1040 |
| Maximum | 99301 |

---

# Key Observations

### ✅ Dataset Size

The dataset contains **9800 sales records** with **18 columns**, making it suitable for data analysis.

---

### ✅ Data Quality

The dataset is clean with only **11 missing values** in the Postal Code column.

---

### ✅ Data Types

Most columns are stored as **string** values.

The **Sales** column is stored as **float**, which is appropriate for numerical analysis.

The **Order Date** and **Ship Date** columns are currently stored as strings and will be converted to datetime format during the data cleaning phase.

---

### ✅ Sales Distribution

The average sales amount (**230.769**) is much higher than the median (**54.490**).

This indicates that:

- Most sales are relatively small.
- A few high-value orders significantly increase the average sales amount.

This suggests the dataset is **right-skewed**.

---

# Conclusion

Phase 1 successfully explored the dataset structure and identified the following:

- Dataset loaded successfully.
- No major data quality issues were found.
- Only 11 missing Postal Code values require cleaning.
- Date columns need conversion to datetime format.
- Dataset is ready for Phase 2 (Data Cleaning).

---

# Next Phase

➡️ Phase 2 – Data Cleaning

Topics to be covered:

- Missing Value Handling
- Duplicate Checking
- Data Type Conversion
- Date Formatting
- Data Validation

---

**Status:** ✅ Phase 1 Completed