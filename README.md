# 🖥️ ERP Estoque de Eletrônicos

API REST para gerenciamento de estoque de eletrônicos, desenvolvida com FastAPI, PostgreSQL e Python.

## 🚀 Tecnologias

- **Python** — linguagem base
- **FastAPI** — framework para criação da API
- **PostgreSQL** — banco de dados
- **Pydantic** — validação de dados
- **psycopg** — conexão Python com PostgreSQL

## 📦 Funcionalidades

- ✅ Listar todos os produtos
- ✅ Buscar produto por ID
- ✅ Filtrar produtos por nome
- ✅ Cadastrar novo produto
- ✅ Atualizar produto (parcial ou completo)
- ✅ Deletar produto

## 🔗 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /produtos | Lista todos os produtos |
| GET | /produtos/{id} | Busca produto por ID |
| GET | /produtos?nome=x | Filtra por nome |
| POST | /produtos | Cadastra novo produto |
| PUT | /produtos/{id} | Atualiza produto |
| DELETE | /produtos/{id} | Remove produto |

## 🗄️ Estrutura do Banco

```sql
CREATE TABLE estoque (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    valor NUMERIC(10,2) NOT NULL
);
```

## ▶️ Como rodar

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/erp-estoque-fastapi.git
```

2. Instale as dependências
```bash
pip install fastapi psycopg uvicorn
```

3. Configure o banco no arquivo `erp.py`

4. Rode a API
```bash
python -m uvicorn erp:app --reload
```

5. Acesse a documentação automática
