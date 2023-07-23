# dio-twitter-py

Projeto ORIGEM criado durante o living code [Consumindo a API do Twitter com Python](https://docs.google.com/presentation/d/11DkkyQUIloVQLm8i6hN6w3xyUaP4WSRE/edit?usp=sharing&ouid=102662434190974209165&rtpof=true&sd=true).

## PARA CONCLUSAO DO DESAFIO

### Descrição do Desafio

Expanda seus conhecimentos sobre Python, Banco de Dados e APIs. Para isso, vamos criar um projeto prático com o objetivo de consumir a API REST do Twitter. Nesse sentido, uma série de boas práticas e dicas foram apresentadas pelo nosso expert. Entre elas o Tweepy, que reduziu a complexidade no consumo da API do Twitter. Agora é a sua hora de brilhar! Reproduza o projeto que criamos, dando a sua cara a ele. Para isso, pense em novas funcionalidades e formas de evoluir a solução:

Criar relatórios/dashboards para exibir de forma mais amigável os dados coletados via Twitter API.
Containerizar a aplicação com Docker e modularizar a aplicação.
Dica: você pode dar um "fork" no repositório para organizar melhor as suas alterações e evoluções, mantendo uma referência direta ao código original.

### Links Úteis
Slides
Repositório no [GitHub (implementação de referência) ](https://github.com/guicarvalho/dio-twitter-py)
Documentação [Twitter API](https://developer.twitter.com/en/docs)
Documentação [Twitter API FREE](https://developer.twitter.com/en/portal/products/free)
Documentação [Tweepy](https://docs.tweepy.org/en/stable/)

## LIMITACAO PARA CONCLUSAO

Para replicar o projeto hoje 23/07/2023 o provedor developer.twitter.com obriga no mínimo obter o pacote "Basic access for $100/month", não é possível testar e pilotar projetos da forma que está implementado utilizando o pacote "Free" com apenas os serviços disponibilizados:
	POST /2/tweets { 50 requests / 24 hours PER APP / PER USER }
	DELETE /2/tweets/:id { 50 requests / 24 hours PER APP / PER USER }
	GET /2/users/me { 25 requests / 24 hours PER USER }

## Docker

Devido a limitação do consumo da API do Tweeter, o teste e execução ficou comprometido, caso necessário testar o fonte, faça por sua conta e risco.

## Tecnologias 📚

- Python 3.8.x
- FastAPI
- MongoDB

## Requisitos ✋

- Docker
- Docker compose

## Instalação 💽

Instale o [Docker](https://www.docker.com) e [Docker compose](https://docs.docker.com/compose/) no seu computador.

## Rodando a aplicação 🛸

```sh
pip install poetry
poetry init

poetry shell
python main.py
```

Acesso o [Swagger UI](http://localhost:8000/docs) para listar todos os endpoints.

Use `Ctrl+C` para finalizar o processo servidor.

## Rodando os testes 🧪

```sh
poetry shell
pytest
```
