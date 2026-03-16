from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/projeto1"

engine = create_engine(DATABASE_URL)

app = FastAPI(title="API Usuários - Versão Corrigida")


@app.get("/status")
def status():
    try:
        conn = engine.connect()
        conn.execute(text("SELECT 1"))
        conn.close()
        return {"status": "ok", "banco": "conectado"}
    except Exception as e:
        return {"status": "erro", "detalhe": str(e)}


@app.get("/users")
def get_users():
    try:
        conn = engine.connect()
        result = conn.execute(text("SELECT * FROM users.users"))
        rows = [dict(row._mapping) for row in result]
        conn.close()
        return rows
    except Exception as e:
        return {"ERRO_REAL": str(e)}


@app.post("/users")
def criar_usuario(name: str, email: str, password_hash: str):
    try:
        conn = engine.connect()
        conn.execute(
            text("""
                INSERT INTO users.users 
                (name, email, password_hash, is_active, created_at, updated_at)
                VALUES (:name, :email, :password_hash, true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """),
            {"name": name, "email": email, "password_hash": password_hash}
        )
        conn.commit()
        conn.close()
        return {"mensagem": "criado com sucesso"}
    except Exception as e:
        return {"ERRO_REAL": str(e)}


print("✅ main.py carregado - usando apenas 'users'")