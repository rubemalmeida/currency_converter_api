from fastapi import APIRouter, HTTPException, Query
from models import SolicitacaoConversaoMoeda, RespostaConversaoMoeda
from services import converter_moeda

api_router = APIRouter()


@api_router.get("/converter_moeda", response_model=RespostaConversaoMoeda)
async def converter_moeda_api(
    origem: str = Query(
        ...,
        description="A moeda de origem. As opções são: USD, BRL, EUR, BTC, ETH",
        example="USD",
    ),
    destino: str = Query(
        ...,
        description="A moeda de destino. As opções são: USD, BRL, EUR, BTC, ETH",
        example="BRL",
    ),
    valor: float = Query(..., description="O valor a ser convertido", example=100.0),
):
    moedas_aceitas = ["USD", "BRL", "EUR", "BTC", "ETH"]
    if origem not in moedas_aceitas:
        raise HTTPException(
            status_code=400, detail=f"Moeda de origem {origem} não é aceita"
        )
    if destino not in moedas_aceitas:
        raise HTTPException(
            status_code=400, detail=f"Moeda de destino {destino} não é aceita"
        )
    try:
        valor_convertido = converter_moeda(origem, destino, valor)
        return RespostaConversaoMoeda(
            moeda_origem=origem,
            moeda_destino=destino,
            valor=valor,
            valor_convertido=valor_convertido,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@api_router.get("/healthcheck")
async def healthcheck():
    return {"status": "OK"}
