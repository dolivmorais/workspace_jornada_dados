import streamlit as st
import pandas as pd


class CSVCollector:
    def __init__(self, schema: dict, cell_range: str):
        self._schema = schema
        self.cell_range = cell_range

    def start(self):
        file = self.getData()
        if file is None:
            return None

        df = self.extractData(file)
        return df

    def getData(self):
        return st.file_uploader(
            "Escolha um arquivo CSV",
            type="csv"
        )

    def extractData(self, file):
        df = pd.read_csv(file)

        # aplica schema (cast seguro)
        for col, expected_type in self._schema.items():
            if col in df.columns:
                try:
                    df[col] = df[col].astype(expected_type)
                except Exception:
                    df[col] = None

        return df
    
    def validateData(self, df: pd.DataFrame) -> bool:
        for col, expected_type in self._schema.items():
            if col in df.columns:
                if not pd.api.types.is_dtype_equal(df[col].dtype, expected_type):
                    return False
        return True
    
    def transformData(self, df: pd.DataFrame) -> pd.DataFrame:
        # Exemplo simples de transformação: remover linhas com valores nulos
        df = df.dropna()
        return df   
    
    def loadData(self, df: pd.DataFrame, destination: str):
        df.to_csv(destination, index=False)
