CREATE SCHEMA IF NOT EXISTS users;

CREATE TABLE IF NOT EXISTS users.users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    password_hash TEXT,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users.users (name, email, password_hash)
VALUES 
('Teste 1', 'teste1@email.com', '123'),
('Teste 2', 'teste2@email.com', '123'),
('Teste 3', 'teste3@email.com', '123'),
('Teste 4', 'teste4@email.com', '123'),
('Teste 5', 'teste5@email.com', '123'),
('corno', 'malins@email.com', '123'),
('ratazana', 'assassina1@email.com', '123');
