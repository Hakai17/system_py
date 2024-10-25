
# Task Management API

Esta é uma API para gerenciamento de tarefas, construída com NestJS e TypeORM. Ela permite a criação, leitura, atualização e exclusão de tarefas, além de autenticação de usuários usando JWT.

## Tecnologias Usadas

- **NestJS**: Framework Node.js para construção de aplicações server-side.
- **TypeORM**: ORM para TypeScript e JavaScript que se conecta ao banco de dados.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional.
- **Passport**: Middleware de autenticação para Node.js.
- **JWT**: Para autenticação baseada em tokens.

## Pré-requisitos

Antes de começar, verifique se você tem o seguinte instalado:

- [Node.js](https://nodejs.org/) (v18 ou superior)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Nest CLI](https://docs.nestjs.com/cli/overview) (opcional)

## Configuração do Ambiente

1. Clone este repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd task-management-api
   ```

2. Instale as dependências:

   ```bash
   npm install
   ```

3. Crie um arquivo `.env` na raiz do projeto e configure as variáveis de ambiente:

   ```plaintext
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   DATABASE_USERNAME=seu_usuario
   DATABASE_PASSWORD=sua_senha
   DATABASE_NAME=nome_do_banco
   JWT_SECRET=suachavesecreta
   ```

4. Crie o banco de dados PostgreSQL e execute as migrações (se necessário):

   ```bash
   npx typeorm migration:run
   ```

## Executando a API

Para rodar a API, use o seguinte comando:

```bash
npm run start:dev
```

A API estará disponível em `http://localhost:3000`.

## Endpoints

### Usuários

- **POST /users/register**: Registra um novo usuário.
- **POST /auth/login**: Realiza login e retorna um token JWT.

### Tarefas

- **GET /tasks**: Retorna todas as tarefas.
- **GET /tasks/:id**: Retorna uma tarefa específica.
- **POST /tasks**: Cria uma nova tarefa.
- **PUT /tasks/:id**: Atualiza o status de uma tarefa específica.
- **DELETE /tasks/:id**: Remove uma tarefa específica.

## Testando a API

Você pode testar a API usando o [Postman](https://www.postman.com/) ou outra ferramenta similar. 

### Exemplo de Requisições

1. **Registrar Usuário**:
   - Método: POST
   - URL: `http://localhost:3000/users/register`
   - Body (JSON):
     ```json
     {
       "username": "exemplo",
       "password": "senha123"
     }
     ```

2. **Login**:
   - Método: POST
   - URL: `http://localhost:3000/auth/login`
   - Body (JSON):
     ```json
     {
       "username": "exemplo",
       "password": "senha123"
     }
     ```

3. **Criar Tarefa**:
   - Método: POST
   - URL: `http://localhost:3000/tasks`
   - Header: `Authorization: Bearer <TOKEN_JWT>`
   - Body (JSON):
     ```json
     {
       "title": "Nova Tarefa",
       "description": "Descrição da tarefa"
     }
     ```

## Link da Coleção do Postman

[Coleção do Postman](<LINK_PARA_COLECAO_DO_POSTMAN>)
