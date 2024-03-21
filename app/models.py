from pydantic import BaseModel


class SolicitacaoConversaoMoeda(BaseModel):
    moeda_origem: str
    moeda_destino: str
    valor: float


class RespostaConversaoMoeda(BaseModel):
    moeda_origem: str
    moeda_destino: str
    valor: float
    valor_convertido: float
