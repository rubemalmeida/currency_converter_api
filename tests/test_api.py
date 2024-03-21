from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_convert_currency():
    response = client.post(
        "/converter_moeda/",
        json={"moeda_origem": "USD", "moeda_destino": "BRL", "valor": 100},
    )
    assert response.status_code == 200
    data = response.json()
    assert data.get("moeda_origem") == "USD"
    assert data.get("moeda_destino") == "BRL"
    assert data.get("valor") == 100
    assert data.get("valor_convertido") > 0


def test_convert_currency_invalid_currency():
    response = client.post(
        "/converter_moeda/",
        json={"moeda_origem": "INVALID", "moeda_destino": "BRL", "valor": 100},
    )
    assert response.status_code == 400


def test_convert_currency_negative_value():
    response = client.post(
        "/converter_moeda/",
        json={"moeda_origem": "USD", "moeda_destino": "BRL", "valor": -100},
    )
    assert response.status_code == 400
