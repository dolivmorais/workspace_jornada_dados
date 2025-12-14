from fastapi import FastAPI
from fakeapi.api.routes import router

app = FastAPI()
app.include_router(router)


# rodar: poetry run uvicorn backend.fakeapi.main:app --reload