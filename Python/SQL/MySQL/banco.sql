CREATE DATABASE pmysql;

CREATE TABLE produtos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    preco DECIMAL(8,2) NOT NULL,
    estoque INT NOT NULL
);

UPDATE produtos SET nome = '{nome}', preco = {preco}, estoque = {estoque} WHERE id = 2)