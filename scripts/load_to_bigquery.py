from google.cloud import bigquery
import pandas as pd

PROJECT_ID = "lendingclubvertexai"
DATASET_ID = "lending_club_analytics"
TABLE_ID = "loans_cleaned"
CSV_PATH = "../data/processed/clean_lending_club.csv"


def load_csv_to_bigquery():
    client = bigquery.Client(project=PROJECT_ID)

    # Create dataset if it doesn't exist
    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
    try:
        client.get_dataset(dataset_ref)
        print(f"Dataset '{DATASET_ID}' already exists.")
    except Exception:
        dataset_id = f"{PROJECT_ID}.{DATASET_ID}"
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"  
        client.create_dataset(dataset)
        print(f"Created dataset '{DATASET_ID}'.")

    # Step 2: Load CSV into table
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    df = pd.read_csv(CSV_PATH)
    
    # Define explicit schema
    schema = [
        bigquery.SchemaField("loan_amnt", "FLOAT"),
        bigquery.SchemaField("int_rate", "FLOAT"),
        bigquery.SchemaField("annual_inc", "FLOAT"),
        bigquery.SchemaField("dti", "FLOAT"),
        bigquery.SchemaField("emp_length", "STRING"),
        bigquery.SchemaField("grade", "STRING"),
        bigquery.SchemaField("home_ownership", "STRING"),
        bigquery.SchemaField("purpose", "STRING"),
        bigquery.SchemaField("loan_status", "STRING"),
        bigquery.SchemaField("issue_d", "DATE"),
        bigquery.SchemaField("dti", "FLOAT")
    ]

    job_config = bigquery.LoadJobConfig(
        schema=schema,  
        write_disposition="WRITE_TRUNCATE",  # overwrite table if exists
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )
    
    # Convert issue_d to YYYY-MM-DD
    #df["issue_d"] = pd.to_datetime(df["issue_d"], errors="coerce").dt.date

    load_job = client.load_table_from_dataframe(
        df, table_ref, job_config=job_config
    )
    load_job.result()  # wait for completion

    print(f"Loaded {df.shape[0]} rows into {table_ref}")


if __name__ == "__main__":
    load_csv_to_bigquery()
