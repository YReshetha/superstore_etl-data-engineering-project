import pandas as pd
from sqlalchemy import create_engine
import os

def load_data():
    # Paths
    base_path = os.path.dirname(os.path.abspath(__file__))
    transformed_path = os.path.join(base_path, "..", "data", "transformed", "superstore_dataset_transformed.csv")
    db_path = os.path.join(base_path, "..", "data", "superstore.db")

    # Read transformed CSV
    df = pd.read_csv(transformed_path)

    # Create SQLite engine
    engine = create_engine(f"sqlite:///{db_path}")

    # Load data into SQLite table 'superstore'
    df.to_sql("superstore", engine, if_exists="replace", index=False)

    print(f"Data loaded into SQLite database at: {db_path}")

if __name__ == "__main__":
    load_data()
