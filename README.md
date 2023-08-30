# Loans For Good - Front-End

Neste repositório contem a parte do back-end do projeto [Loans For Good](https://github.com/MiqueiasRihs/Loans-for-good) feito em Django, Postgresql e Celery.

## Rodando o projeto

Para rodar o projeto, siga os passos abaixo:

1. Clone este repositório em sua máquina local.
2. Com o Docker instalado, execute o comando `docker-compose up`.

O servidor com o back-office estará disponível em [http://localhost:8000/admin](http://localhost:8000/admin)

## Acessos

Para acessar o back-office está sendo criado automaticamente um usuário inicial para testes no momento em que o contêiner sobe, os acessos são:

```bash
usuário: admin
senha: admin
```

## Métodos Disponíveis

### POST /analise-de-cliente

Este método recebe um JSON contendo todos os dados solicitados no formulário e encaminha para a API externa de análise de crédito através do Celery. 

### GET /analise-de-cliente

Este método retorna uma lista de campos para serem exibidos e preenchidos no front-end.

## Testes

Os testes unitários são realizados no momento em que o contêiner sobe, mas para serem realizados no momento de desenvolvimento, você pode:

1. No terminal rodar o comando `pytest`.
