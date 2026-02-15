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