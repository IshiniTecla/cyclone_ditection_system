import os
import requests
from src.config import IBTRACS_URL, RAW_DATA_DIR

def download_ibtracs():
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    ibtracs_path = os.path.join(RAW_DATA_DIR, 'ibtracs.csv')
    
    if os.path.exists(ibtracs_path):
        print("IBTrACS already downloaded.")
        return
    
    print("Downloading IBTrACS...")
    response = requests.get(IBTRACS_URL)
    with open(ibtracs_path, 'wb') as f:
        f.write(response.content)
    print("Download completed: ibtracs.csv")
