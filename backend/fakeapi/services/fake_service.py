from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker("pt_BR")

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "produtos.csv"

df = pd.read_csv(CSV_PATH)

def gerar_compra():
    index = random.randint(0, len(df) - 1)
    row = df.iloc[index]

    return {
        "client": fake.name(),
        "creditcard": fake.credit_card_number(),
        "product_name": str(row["Product Name"]),
        "ean": int(row["EAN"]),     
        "price": float(round(row["Price"] * 1.20, 2)),
        #"price": "teste",  
        "store": "Compra gerada com sucesso",
        "date_time": fake.iso8601(),
        "client_position": list(fake.local_latlng(country_code="BR")),  
    }

# rodar: poetry run uvicorn backend.fakeapi.main:app --reload
