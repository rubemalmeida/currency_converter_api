# Olá, seja bem-vindo ao currency_converter_api! 🚀

Este arquivo README vai te ajudar a rodar a aplicação no seu computador. Let's vamos!

## TL;DR
```bash
docker build -t currency_converter_api . && docker run -d --name currency_converter_api -p 80:80 currency_converter_api && sleep 5 && curl -X GET "http://localhost:80/healthcheck"
```

## O que você precisa ter instalado
- Docker 🐳: O projeto roda dentro de um contêiner Docker, então será preciso ter ele instalado na máquina.

## Colocando a mão na massa

1. Primeiro, clone o repositório. Abra o terminal e digite:
```bash
git clone https://github.com/rubemalmeida/currency_converter_api.git
cd currency_converter_api
```

2. Agora vamos construir a imagem Docker. No mesmo terminal, digite:
```bash
docker build -t currency_converter_api .
```

3. Pronto, agora é só rodar o contêiner Docker:
```bash
docker run -d --name currency_converter_api -p 80:80 currency_converter_api
```

E that's all folks! 🎉 A API já está rodando e disponível em http://localhost:80/docs.
