import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app

# ---------------------------
# FIXTURE: cliente de teste
# ---------------------------
@pytest.fixture
def client():
    return TestClient(app)

# ---------------------------
# FIXTURE: mock do banco
# ---------------------------
@pytest.fixture
def mock_conn():
    with patch("main.engine.connect") as mock_connect:
        conn = MagicMock()
        mock_connect.return_value = conn
        yield conn

# ---------------------------
# TESTES /status
# ---------------------------
def test_status_ok(client, mock_conn):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["banco"] == "conectado"
    mock_conn.execute.assert_called_once()
    mock_conn.close.assert_called_once()

def test_status_error(client):
    with patch("main.engine.connect", side_effect=Exception("erro banco")):
        response = client.get("/status")
        data = response.json()
        assert data["status"] == "erro"
        assert "erro banco" in data["detalhe"]

# ---------------------------
# TESTES /users GET
# ---------------------------
def test_get_users(client, mock_conn):
    fake_row = MagicMock()
    fake_row._mapping = {"id": 1, "name": "Joao", "email": "joao@email.com"}
    mock_conn.execute.return_value = [fake_row]

    response = client.get("/users")
    data = response.json()
    assert data[0]["name"] == "Joao"
    assert data[0]["email"] == "joao@email.com"
    mock_conn.close.assert_called_once()

def test_get_users_error(client):
    with patch("main.engine.connect", side_effect=Exception("falha banco")):
        response = client.get("/users")
        data = response.json()
        assert "ERRO_REAL" in data
        assert "falha banco" in data["ERRO_REAL"]

# ---------------------------
# TESTES POST /users
# ---------------------------
def test_create_user(client, mock_conn):
    response = client.post(
        "/users",
        params={"name": "Maria", "email": "maria@email.com", "password_hash": "123"}
    )
    data = response.json()
    assert data["mensagem"] == "criado com sucesso"
    mock_conn.execute.assert_called_once()
    mock_conn.commit.assert_called_once()
    mock_conn.close.assert_called_once()

def test_create_user_error(client):
    with patch("main.engine.connect", side_effect=Exception("erro insert")):
        response = client.post(
            "/users",
            params={"name": "Maria", "email": "maria@email.com", "password_hash": "123"}
        )
        data = response.json()
        assert "ERRO_REAL" in data
        assert "erro insert" in data["ERRO_REAL"]