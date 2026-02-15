from google.cloud import bigquery

client = bigquery.Client()

def run_query(sql):
    query_job = client.query(sql)
    return query_job.to_dataframe()