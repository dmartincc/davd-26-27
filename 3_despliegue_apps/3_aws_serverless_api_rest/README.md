# Despliegue de una API Flask serverless en AWS

Pasos para desplegar una API Flask en AWS Lambda + API Gateway con el [Serverless Framework](https://www.serverless.com/).

## Requisitos previos

- Cuenta de AWS y [AWS CLI](https://aws.amazon.com/cli/) configurado (`aws configure`)
- [Node.js](https://nodejs.org/) (para el CLI de Serverless)
- [Python](https://www.python.org/downloads/) 3.10+
- [Serverless Framework](https://www.serverless.com/framework/docs/getting-started)

```bash
npm install -g serverless
```

## Configuración inicial

Desde esta carpeta:

```bash
npm install
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
serverless login   # si usas la cuenta de Serverless Dashboard
```

## Despliegue

```bash
serverless deploy
```

Al terminar, Serverless mostrará la URL de API Gateway.

## Prueba

```bash
curl https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
```

## Ejecución local

```bash
pip install -r requirements.txt
serverless wsgi serve
```

## Personalización

Ajusta `serverless.yml` (región, stage, memoria, timeout, dominio, autorización, etc.) según tus necesidades.
