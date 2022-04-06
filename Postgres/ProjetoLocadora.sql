CREATE DATABASE ProjetoLocadora;

CREATE TABLE atores(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100)
);
CREATE TABLE generos(
    id SERIAL PRIMARY KEY,
    genero VARCHAR(100)
);
CREATE TABLE filmes(
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(50),
    valor MONEY NOT NULL,
    id_genero INT REFERENCES generos(id) NOT NULL
);
CREATE TABLE dvds(
    id SERIAL PRIMARY KEY,
    quantidade INT NOT NULL,
    id_filme INT REFERENCES filmes(id) NOT NULL
);

CREATE TABLE atores_filmes(
    id SERIAL PRIMARY KEY,
    id_filme INT REFERENCES filmes(id) NOT NULL,
    id_ator INT REFERENCES atores(id) NOT NULL,
    personagem VARCHAR(100)
);
CREATE TABLE clientes(
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    telefone CHAR(12) NOT NULL,
    endereco VARCHAR(100) NOT NULL
);
CREATE TABLE emprestimos(
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    id_cliente INT REFERENCES clientes(id) NOT NULL
);
CREATE TABLE filmes_emprestimo(
    id SERIAL PRIMARY KEY,
    id_filme INT REFERENCES filmes(id),
    id_emprestimo INT REFERENCES emprestimos(id) NOT NULL
);
CREATE TABLE devolucoes(
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    id_emprestimo INT REFERENCES emprestimos(id) NOT NULL
);
CREATE TABLE filmes_devolucao(
    id SERIAL PRIMARY KEY,
    id_devolucao INT REFERENCES devolucoes(id) NOT NULL,
    id_filme_emprestimo INT REFERENCES filmes_emprestimo(id) NOT NULL
);
