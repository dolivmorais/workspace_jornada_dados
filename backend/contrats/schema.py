from typing import Dict, Type

# 👉 type hint (opcional)
GenericSchemaType = Dict[str, Type]

# 👉 dict REAL (runtime)
CompraSchema: GenericSchemaType = {
    "ean": int,
    "price": float,
    "store": str,
    "date_time": str,
}

type(CompraSchema)
# <class 'dict'>
