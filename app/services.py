def converter_moeda(moeda_origem: str, moeda_destino: str, valor: float) -> float:
    taxas_conversao = {
        "USD_BRL": 5.5,
        "USD_EUR": 0.85,
        "USD_BTC": 0.000025,
        "USD_ETH": 0.00035,
    }
    conversao = f"{moeda_origem}_{moeda_destino}"
    taxa = taxas_conversao.get(conversao, 0.0)
    return valor * taxa
