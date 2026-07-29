# 🧹 Capstone Project 1
## Phase 2 – Data Cleaning Report

---

## Project Information

**Project Name:** SuperStore Sales Data Analysis

**Dataset:** SuperStore_Dataset.csv

**Phase:** 2 – Data Cleaning

---

# Objective

The objective of Phase 2 is to improve the quality of the dataset by identifying missing values, checking for duplicate records, validating data types, and preparing the dataset for exploratory data analysis.

---

# Data Cleaning Tasks Performed

## 1. Missing Value Analysis

Missing values were checked for all columns using the `isnull().sum()` function.

### Result

| Column | Missing Values |
|---------|---------------:|
| Postal Code | 11 |

### Observation

- Only the **Postal Code** column contains missing values.
- All other columns are complete.

---

## 2. Duplicate Record Check

Duplicate records were checked using the `duplicated().sum()` function.

### Result

| Metric | Value |
|---------|------:|
| Duplicate Rows | 0 |

### Observation

- No duplicate records were found.
- The dataset already contains unique records.
- Therefore, no rows were removed.

---

## 3. Date Format Conversion

The following columns were converted from **string** data type to **datetime** format.

- Order Date
- Ship Date

### Observation

Converting these columns to datetime enables:

- Date-based filtering
- Monthly and yearly analysis
- Time-series analysis
- Shipping duration calculations

---

## 4. Postal Code Investigation

The missing Postal Code values were investigated before deciding whether to fill or remove them.

### Investigation Findings

- All 11 missing values belong to:

```
City  : Burlington
State : Vermont
```

Further analysis showed:

| City | State | Postal Code |
|------|--------|------------|
| Burlington | North Carolina | 27217 |
| Burlington | Iowa | 52601 |
| Burlington | Vermont | Missing |

### Observation

Although the city name **Burlington** exists in multiple states, **no valid Postal Code is available for Burlington, Vermont** anywhere in the dataset.

Therefore, the missing values **cannot be inferred from existing data**.

---

# Cleaning Decision

The missing Postal Code values were **not filled** because:

- Filling with **0** would introduce incorrect data.
- Removing the rows would cause unnecessary data loss.
- The dataset contains no reference Postal Code for Burlington, Vermont.
- Preserving the missing values maintains data integrity.

---

# Summary

| Task | Status |
|------|--------|
| Missing Value Check | ✅ Completed |
| Duplicate Check | ✅ Completed |
| Duplicate Removal | Not Required |
| Date Conversion | ✅ Completed |
| Postal Code Investigation | ✅ Completed |
| Missing Postal Code Filled | No |

---

# Conclusion

The dataset was successfully validated and prepared for analysis.

Key outcomes:

- No duplicate records were found.
- Date columns were converted to datetime format.
- Postal Code missing values were investigated in detail.
- Missing values were intentionally preserved because there was insufficient evidence to infer the correct Postal Codes.

The dataset is now ready for **Phase 3 – Exploratory Data Analysis (EDA).**

---

**Status:** ✅ Phase 2 Completed