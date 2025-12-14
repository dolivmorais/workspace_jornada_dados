from fastapi import APIRouter
from fakeapi.services.fake_service import gerar_compra

router = APIRouter()


@router.get("/gerar_compra")
async def gerar_compra_endpoint():
    return gerar_compra()


@router.get("/gerar_compra/{qtd}")
async def gerar_compra_lote(qtd: int):
    if qtd < 1:
        return {"error": "Quantidade inválida"}

    return [gerar_compra() for _ in range(qtd)]

