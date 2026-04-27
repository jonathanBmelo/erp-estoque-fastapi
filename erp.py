from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import psycopg
 
app = FastAPI(title="ERP Estoque API")
 
def get_conn():
    return psycopg.connect("host=localhost dbname=produtos_informatica user=postgres password=admin")
 
class Produto(BaseModel):
    nome: str
    quantidade: int
    valor: float
 
class ProdutoAtualizar(BaseModel):
    nome: Optional[str] = None
    quantidade: Optional[int] = None
    valor: Optional[float] = None
 
@app.get("/produtos")
def listar_produtos(nome: Optional[str] = None):
    conn = get_conn()
    cursor = conn.cursor()
    if nome:
        cursor.execute(
            "SELECT id, nome, quantidade, valor FROM estoque WHERE nome ILIKE %s ORDER BY id",
            (f"%{nome}%",)
        )
    else:
        cursor.execute("SELECT id, nome, quantidade, valor FROM estoque ORDER BY id")
    produtos = cursor.fetchall()
    conn.close()
    return [{"id": p[0], "nome": p[1], "quantidade": p[2], "valor": float(p[3])} for p in produtos]
 
@app.get("/produtos/{id}")
def buscar_produto(id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, quantidade, valor FROM estoque WHERE id = %s", (id,))
    p = cursor.fetchone()
    conn.close()
    if not p:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return {"id": p[0], "nome": p[1], "quantidade": p[2], "valor": float(p[3])}
 
@app.post("/produtos", status_code=201)
def criar_produto(produto: Produto):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO estoque (nome, quantidade, valor) VALUES (%s, %s, %s) RETURNING id",
        (produto.nome, produto.quantidade, produto.valor)
    )
    id_novo = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return {"id": id_novo, "nome": produto.nome, "quantidade": produto.quantidade, "valor": produto.valor}
 
@app.put("/produtos/{id}")
def atualizar_produto(id: int, produto: ProdutoAtualizar):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, quantidade, valor FROM estoque WHERE id = %s", (id,))
    p = cursor.fetchone()
    if not p:
        conn.close()
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    nome = produto.nome if produto.nome is not None else p[1]
    quantidade = produto.quantidade if produto.quantidade is not None else p[2]
    valor = produto.valor if produto.valor is not None else float(p[3])
    cursor.execute(
        "UPDATE estoque SET nome = %s, quantidade = %s, valor = %s WHERE id = %s",
        (nome, quantidade, valor, id)
    )
    conn.commit()
    conn.close()
    return {"id": id, "nome": nome, "quantidade": quantidade, "valor": valor}
 
@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM estoque WHERE id = %s", (id,))
    p = cursor.fetchone()
    if not p:
        conn.close()
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    cursor.execute("DELETE FROM estoque WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return {"mensagem": f"'{p[0]}' removido com sucesso!"}
