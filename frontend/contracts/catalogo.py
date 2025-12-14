from pydantic import BaseModel, PositiveFloat, field_validator
from datetime import datetime
from enum import Enum

class CategoriaEnum(str, Enum):
    Live = "Live"
    East = "East"
    Smart = "Smart"
    Water = "Water"
    Goal = "Goal"
    Future = "Future"
    World = "World"
    Political = "Political"
    Southern = "Southern"
    Global = "Global"
    Close = "Close"
    Half = "Half"

class Catalogo(BaseModel):
    EAN: str
    ProductName: CategoriaEnum
    Price: PositiveFloat

    @field_validator('Price')
    @classmethod
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be a positive float')
        return v