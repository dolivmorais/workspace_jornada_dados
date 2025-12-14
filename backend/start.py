from datasource import APICollector
from contrats.schema import CompraSchema, GenericSchemaType

import schedule
import time

def job():
    print("⏳ Executando coleta...")
    collector = APICollector(CompraSchema)
    arquivo = collector.start(3)
    print("✅ Arquivo gerado:", arquivo)


# agenda a cada 10 segundos
schedule.every(10).seconds.do(job)

print("🚀 Scheduler iniciado (a cada 10 segundos)")

while True:
    schedule.run_pending()
    time.sleep(1)



#backend.fakeapi.start.py
# poetry run python backend/start.py
