def converter_moeda(moeda_origem: str, moeda_destino: str, valor: float) -> float:
    taxas_conversao = {
        "USD_BRL": 5.5,
        "USD_EUR": 0.85,
        "USD_BTC": 0.000025,
        "USD_ETH": 0.00035,
    }
    conversao = f"{moeda_origem}_{moeda_destino}"
    if conversao not in taxas_conversao:
        raise ValueError(
            f"Conversão de {moeda_origem} para {moeda_destino} não suportada"
        )
    taxa = taxas_conversao.get(conversao)
    return valor * taxa
