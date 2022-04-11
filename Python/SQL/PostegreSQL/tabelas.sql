CREATE TABLE produtos(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(8,2) NOT NULL,
    estoque INT NOT NULL
);
SELECT * FROM produtos;
UPDATE produtos SET nome = 'Switch', preco=2100, estoque = 2 WHERE id = 1