from typing import List
import pandas as pd
import requests
from pathlib import Path
from datetime import datetime


class APICollector:
    def __init__(self, schema: dict):
        self._schema = schema

        # 📁 diretório fixo
        self.base_path = Path(
            r"C:\Users\Diego\Documents\workspace_jornada_dados\backend\arq_parquet_api"
        )
        self.base_path.mkdir(parents=True, exist_ok=True)

    def start(self, param: int):
        response = self.getData(param)

        # garante lista
        if isinstance(response, dict):
            response = [response]

        extracted = self.extractData(response)
        df = self.transformDf(extracted)

        file_path = self.convertToParquet(df)

        return file_path  # 🔥 retorna caminho do arquivo

    def getData(self, param: int):
        if param > 1:
            return requests.get(
                f"http://127.0.0.1:8000/gerar_compra/{param}"
            ).json()

        return requests.get(
            "http://127.0.0.1:8000/gerar_compra"
        ).json()

    def extractData(self, response):
        result = []

        for item in response:
            index = {}
            for key, expected_type in self._schema.items():
                value = item.get(key)
                index[key] = value if isinstance(value, expected_type) else None
            result.append(index)

        return result

    def transformDf(self, response):
        return pd.DataFrame(response)

    def convertToParquet(self, df: pd.DataFrame):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"compras_api_{timestamp}.parquet"
        file_path = self.base_path / file_name

        try:
            df.to_parquet(file_path, index=False)
            print(f"✅ Arquivo Parquet gerado em: {file_path}")
            return file_path
        except Exception as e:
            print(f"❌ Erro ao gerar Parquet: {e}")
            return None

