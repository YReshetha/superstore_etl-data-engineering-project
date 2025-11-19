import pandas as pd
import os

def transform_data():
    # Paths
    base_path = os.path.dirname(os.path.abspath(__file__))
    raw_path = os.path.join(base_path, "..", "data", "raw", "superstore_dataset.csv")
    transformed_path = os.path.join(base_path, "..", "data", "transformed", "superstore_dataset_transformed.csv")

    # Read raw CSV
    df = pd.read_csv(raw_path)

    # Example transformations:
    # 1. Strip whitespace from column names and convert to lowercase
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # 2. Optional: filter out rows with missing 'sales'
    if 'sales' in df.columns:
        df = df[df['sales'].notna()]

    # 3. Save transformed CSV
    os.makedirs(os.path.dirname(transformed_path), exist_ok=True)
    df.to_csv(transformed_path, index=False)

    print(f"Transformation complete! File saved to: {transformed_path}")

if __name__ == "__main__":
    transform_data()
