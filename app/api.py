from fastapi import FastAPI, HTTPException
from app.models import SolicitacaoConversaoMoeda, RespostaConversaoMoeda
from app.services import converter_moeda

app = FastAPI()


@app.post("/converter_moeda/", response_model=RespostaConversaoMoeda)
async def converter_moeda_api(solicitacao: SolicitacaoConversaoMoeda):
    try:
        valor_convertido = converter_moeda(
            solicitacao.moeda_origem, solicitacao.moeda_destino, solicitacao.valor
        )
        return RespostaConversaoMoeda(
            moeda_origem=solicitacao.moeda_origem,
            moeda_destino=solicitacao.moeda_destino,
            valor=solicitacao.valor,
            valor_convertido=valor_convertido,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "OK"}
