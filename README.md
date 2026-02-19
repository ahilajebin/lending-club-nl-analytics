Lending Club NL Analytics
**Natural Language to SQL Analytics Platform using Vertex AI & BigQuery**

## Project Summary

I built a production-ready Natural Language to SQL analytics platform that allows users to query a financial dataset using plain English.

For example:
> “What is the average DTI for loans with grade A?”

The system automatically:

1. Converts the question into valid BigQuery SQL using Google’s Gemini model
2. Executes the query against a structured dataset
3. Returns the computed result via a web interface

The entire system is deployed serverlessly on Google Cloud.

This project encompases real-world LLM integration, prompt engineering, cloud deployment, and data infrastructure design.

---

## Problem It Solves

Business stakeholders often need insights from structured datasets but:

* Don’t know SQL
* Depend on data teams for simple queries
* Face delays in analytics workflows

This application removes that bottleneck by enabling natural-language-driven data access while maintaining SQL control and guardrails.

---

## Architecture

User Question -> Flask Web App (Cloud Run) -> Vertex AI (Gemini) → Generates BigQuery SQL -> BigQuery → Executes Query -> Formatted Result Returned to User

### Google Cloud Services Used:

* Cloud Run (serverless backend)
* Vertex AI (LLM inference)
* BigQuery (data warehouse)
* IAM (secure service-to-service authentication)

The entire system runs without local credentials and uses a service account with least-privilege access.

---

## Key Technical Components

### Prompt Engineering for Structured Output

I designed a constrained system prompt to ensure:

* Only allowed columns are used
* Valid BigQuery SQL is generated
* SQL-only output (no explanation text)
* Protection against schema hallucination

This reduces LLM unpredictability and improves reliability in structured environments.

---

### NL → SQL Execution Pipeline

The core pipeline:

* User input → Gemini model
* SQL generated dynamically
* BigQuery job executed programmatically
* Result parsed and returned as a clean response

The application bridges generative AI with deterministic analytics execution.

---

### Serverless Production Deployment

Instead of running locally, I:

* Containerized the Flask app
* Deployed via GitHub → Cloud Run integration
* Configured IAM roles (Vertex AI User, BigQuery Job User)
* Managed environment variables securely
* Debugged model access and API permissions

This mirrors real-world production deployment scenarios.

---

## Technologies Used

* Python 3.12
* Flask
* Vertex AI (Gemini)
* BigQuery
* Cloud Run
* Docker
* GitHub CI/CD

---

## Example Queries

The system successfully handles:

* Aggregations (AVG, COUNT, GROUP BY)
* Filtering (WHERE conditions)
* Multi-condition queries
* Ranking (ORDER BY + LIMIT)
* Comparative analysis

Example:

> “Show the top 5 loan purposes with the highest average interest rate.”

Generated SQL automatically and returned ranked results.

---

## Security & Guardrails

* Service account–based authentication (no hardcoded keys)
* Restricted IAM roles
* Column-level constraints in prompt
* SELECT-only query pattern
* No raw user SQL execution

This prevents common LLM + database security risks.

---

## Challenges Solved

During deployment, I:

* Debugged Cloud Run container errors
* Resolved IAM permission conflicts
* Enabled Generative AI model access at the project level
* Fixed gRPC model-not-found errors
* Configured environment variables correctly in production

These issues required understanding how Vertex AI, IAM, and Cloud Run interact under the hood.

---

## This project shows my ability to

* Integrate LLMs into structured data systems
* Deploy production cloud applications
* Debug distributed cloud architecture
* Design safe NL → SQL systems
* Apply prompt engineering in practical use cases
* Work across ML, backend, and cloud infrastructure layers
