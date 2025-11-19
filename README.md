# Superstore ETL Project

This project is a simple **ETL pipeline** for the Superstore dataset, built using **Python** and **Apache Airflow** running in **Docker**.

## Project Overview

The pipeline follows the standard ETL steps:

1. **Extract**: Download the Superstore CSV dataset from GitHub.
2. **Transform**: Clean and process the raw data.
3. **Load**: Save the transformed data into a SQLite database.

The ETL is orchestrated using **Airflow DAGs**, allowing manual or scheduled execution.

---

## Folder Structure
├── dags/
│ └── superstore_dag.py # Airflow DAG controlling ETL tasks
├── scripts/
│ ├── extract.py # Downloads CSV dataset
│ ├── transform.py # Transforms raw data
│ └── load.py # Loads data into database
├── data/
│ ├── raw/ # Raw CSV files
│ └── transformed/ # Transformed data
├── docker-compose.yaml # Docker setup for Airflow
└── README.md # Project documentation

## Requirements

- **Docker & Docker Compose** installed  
- Airflow version **2.7.1** (run inside Docker)  
- Python packages used in scripts:
  - `requests`
  - `pandas` (if needed for transformation)

---

## How to Run the Project

1. Start Airflow using Docker Compose:

```bash
docker-compose up -d

Open the Airflow UI in your browser:

http://localhost:8080


Unpause the DAG superstore_etl

Trigger the DAG manually (or schedule it)

Monitor task logs to ensure the ETL runs successfully

ETL Flow
Extract (download CSV) --> Transform (process data) --> Load (save to DB)


Extract: Downloads the dataset only if it doesn’t exist.

Transform: Processes the raw CSV to clean/format the data.

Load: Saves transformed data into data/superstore.db.

Notes

Each DAG run is independent, so triggering multiple times won’t overwrite existing data unless your scripts allow it.

Transformed data is saved in data/transformed/ and loaded into SQLite database in data/superstore.db.

Check logs in the Airflow UI for task execution details.

License

This project is for learning and experimentation purposes.

