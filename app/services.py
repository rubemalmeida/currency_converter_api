def formatar_valor(valor):
    valor_formatado = format(valor, ".2f")
    if valor < 1:
        str_valor = format(valor, ".15f")
        posicao = str_valor.find(".") + 1
        while str_valor[posicao] == "0":
            posicao += 1
        valor_formatado = str_valor[: posicao + 2]
    return valor_formatado


def converter_moeda(moeda_origem: str, moeda_destino: str, valor: float) -> float:
    taxas_conversao = {
        "USD": 1,
        "BRL": 4.98,
        "EUR": 0.92,
        "BTC": 0.000015,
        "ETH": 0.00029,
    }
    if moeda_origem not in taxas_conversao or moeda_destino not in taxas_conversao:
        raise ValueError(
            f"Conversão de {moeda_origem} para {moeda_destino} não suportada"
        )
    taxa_origem = taxas_conversao.get(moeda_origem)
    taxa_destino = taxas_conversao.get(moeda_destino)
    valor_convertido = (valor / taxa_origem) * taxa_destino
    return formatar_valor(valor_convertido)
