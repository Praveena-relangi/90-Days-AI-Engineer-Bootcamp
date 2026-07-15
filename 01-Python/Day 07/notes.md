# Day 07 Notes

## Module

A Python (.py) file containing reusable code.

Example:

```python
import math
```

## Package

A folder containing multiple modules.

## pip

Package Installer for Python.

Example:

```bash
pip install requests
```

## requirements.txt

Contains all project dependencies.

Generate:

```bash
pip freeze > requirements.txt
```

Install:

```bash
pip install -r requirements.txt
```

## Virtual Environment

Isolated Python environment for each project.

Create:

```bash
python -m venv venv
```

Activate (Windows):

```bash
.\venv\Scripts\activate
```

---

# REST API

Communication bridge between client and server.

### HTTP Methods

GET → Retrieve data

POST → Create new data

PUT → Update existing data

DELETE → Delete data

---

# Response Object

```python
response = requests.get(url)
```

---

Status Code

```python
response.status_code
```

---

Raw JSON

```python
response.text
```

---

Python Dictionary

```python
response.json()
```

---

## HTTP Status Codes

200 → OK

201 → Created

204 → No Content

400 → Bad Request

401 → Unauthorized

403 → Forbidden

404 → Not Found

500 → Internal Server Error

---

## CRUD

Create → POST

Read → GET

Update → PUT

Delete → DELETE

---

## Important Learning

Almost every modern AI application communicates using REST APIs.

OpenAI

Gemini

Claude

Weather APIs

GitHub APIs

All work on the same REST principles.