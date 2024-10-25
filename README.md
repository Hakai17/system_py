
# Sistema Distribuído de Processamento de Arquivos

Este projeto é um sistema distribuído de processamento de arquivos usando FastAPI para a API, RabbitMQ para enfileiramento de mensagens e um consumidor que processa os arquivos enviados. Inclui lógica de retentativas, rastreamento de status e logs para maior confiabilidade.

## Funcionalidades

- API para upload de arquivos baseada em FastAPI
- RabbitMQ para processamento assíncrono de tarefas de arquivo
- SQLite para rastrear o status do processamento dos arquivos (pendente, processado, falhou)
- Mecanismo de retentativas para tarefas que falharem (até 3 tentativas)
- Logs para o processamento de tarefas

## Requisitos

- Python
- FastAPI
- RabbitMQ
- SQLite (configurado automaticamente)
- Docker (opcional para RabbitMQ)

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Hakai17/system_py.git
```

### 2. Configure o ambiente virtual e instale as dependências

Recomendamos o uso do `Poetry` para gerenciar as dependências:

```bash
# Instale o Poetry se ainda não estiver instalado
pip install poetry

# Instale as dependências do projeto
poetry install
```

### 3. Configure o RabbitMQ

Você pode usar o Docker para rodar o RabbitMQ, ou instalá-lo localmente. Caso utilize Docker:

```bash
docker run -d --name rabbitmq -p 5672:5672 rabbitmq
```

Certifique-se de que o RabbitMQ esteja rodando em `localhost:5672`.

### 4. Execute o servidor FastAPI

Ative o ambiente virtual e execute a aplicação FastAPI:

```bash
poetry shell
task run
```

A API estará disponível em `http://127.0.0.1:8000`.

### 5. Inicie o consumidor RabbitMQ

Em outra janela de terminal, execute o consumidor que processará os arquivos enviados:

```bash
python app/tasks.py
```

### 6. Envie arquivos através da API

Você pode enviar arquivos para serem processados pelo consumidor RabbitMQ através do endpoint `/upload/`. Use uma ferramenta como `curl` ou Postman:

```bash
curl -X POST "http://127.0.0.1:8000/upload/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@caminho_do_seu_arquivo"
```

O arquivo será enfileirado para processamento e seu status poderá ser verificado no banco de dados SQLite.

## Estrutura de Diretórios

```
.
├── app
│   ├── __init__.py
│   ├── main.py  # Ponto de entrada do FastAPI
│   ├── tasks.py  # Consumidor RabbitMQ e lógica de processamento
│   └── uploads/  # Diretório para armazenar os arquivos enviados
├── files.db  # Banco de dados SQLite para rastrear o status dos arquivos
├── Dockerfile  # Opcional para deploy com Docker
└── README.md  # Este arquivo
```

## Funcionalidades Adicionais

- Tratamento de erros e mecanismo de retentativas em caso de falha no processamento.
- O status do arquivo pode ser rastreado como `pendente`, `processado` ou `falhou`.
- Logs para resolução de problemas.

## Melhorias Futuras

- Implementar sistema de notificações (por exemplo, via e-mail) após o processamento ser concluído.
- Expandir suporte para diferentes tipos de arquivos ou tarefas.
- Melhorar o desempenho e escalabilidade com múltiplos consumidores.
