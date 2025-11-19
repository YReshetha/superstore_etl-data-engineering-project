import requests
import os

def download_csv():
    url = "https://raw.githubusercontent.com/nileshely/SuperStore-Dataset-2019-2022/main/superstore_dataset.csv"
    output_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "superstore_dataset.csv")

    # Skip download if file already exists
    if os.path.exists(output_path):
        print(f"File already exists at: {output_path}")
        return

    print("Downloading Superstore dataset...")
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"Download complete! File saved to: {output_path}")

if __name__ == "__main__":
    download_csv()

