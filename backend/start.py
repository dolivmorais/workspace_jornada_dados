from datasource import APICollector
from contrats.schema import CompraSchema, GenericSchemaType

minha_classe = APICollector(CompraSchema).start(3)

print(minha_classe)


#backend.fakeapi.start.py
# C:\Users\Diego\Documents\workspace_jornada_dados\backend\start.py