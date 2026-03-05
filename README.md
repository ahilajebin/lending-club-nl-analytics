# Lending Club NL Analytics

Natural Language -> SQL-> BigQuery using Vertex AI (Gemini) + Cloud Run

## Overview

This project is a cloud-based Natural Language to SQL analytics application built on Google Cloud.

Users can ask questions in plain English. e.g.,

> *"What is the average DTI for loans with grade A?"*

The system:

1. Converts the question into **BigQuery SQL** using **Vertex AI (Gemini)**
2. Executes the query against a BigQuery dataset
3. Returns the computed result through a Flask web app

The entire application is deployed serverlessly on **Google Cloud Run**.


## Architecture

User Question -> Flask App (Cloud Run) -> Vertex AI (Gemini Model) → Generates SQL -> BigQuery → Executes SQL -> Result Returned to User


## Tech Stack

* **Python 3.12**
* **Flask**
* **Vertex AI (Gemini)**
* **BigQuery**
* **Cloud Run**
* **Docker**
* **GitHub (CI/CD Deployment)**


## Project Structure
```
lending-club-nl-analytics/

  -notebooks
      -initial_eda.ipynb
      -feature_selection.ipynb
      -data_cleaning.ipynb
      
  -data
    -processes
      -clean_lending_club.csv
      
  -scripts
    -load_to_bigquery.py   # Script to load data to BigQuery
    
  -app/
    -app.py                # Flask entry point
    -templates
      -index.html

  -src/
    -nlp/
      -nl_to_sql.py      # Gemini prompt + SQL generation
      -prompt_templates.py
    -gcp
      -bigquery_client.py  # Script to query the BigQuery dataset
      -vertex_ai.py        # Vertex AI to get the question and return answer in English
      
  -requirements.txt
  -Dockerfile
  -README.md
```

## How It Works

### Prompt Engineering

The model is guided with a strict system prompt:

* Uses only specified columns
* Generates valid BigQuery SQL
* Returns SQL only
* Targets table loaded from cleaned data into BigQuery

Example:

```python
BASE_PROMPT = """
You are a data analyst.
Generate a BigQuery SQL query for table `lending_club.loans`.

Columns:
loan_amnt, int_rate, annual_inc, emp_length,
grade, home_ownership, purpose, loan_status, issue_d, dti

Rules:
- Use only these columns
- Use valid BigQuery SQL
- Return SQL only
"""
```


## Deployment

The application is deployed using:

* Google Cloud Run
* Direct GitHub integration
* Automatic container build
* Serverless execution

Environment Variables required:

```
GCP_PROJECT_ID = <project-id>
```

IAM Roles required for Cloud Run service account:

* Vertex AI User
* BigQuery Job User
* BigQuery Data Viewer


## Example Queries

Try asking:

* What is the average DTI for loans with grade A?
* What is the average interest rate by loan grade?
* Which loan purpose has the highest average loan amount?
* Show the top 5 loan purposes with the highest average interest rate.

---

## Security Considerations

* Model prompt restricts allowed columns
* SQL limited to SELECT operations
* BigQuery permissions scoped to required roles
* Cloud Run uses service account authentication

---


## Learning Outcomes

This project demonstrates:

* Production deployment of LLM-powered apps
* Cloud IAM debugging
* Vertex AI integration
* Serverless architecture design
* Prompt engineering for structured outputs
* NL -> SQL system design

---

## Author

Name: Ahila J
University / Program: MSc Data Science, University of Surrey
LinkedIn / Portfolio Link: www.linkedin.com/in/ahilajebin 


