USE postgres;

CREATE TABLE tipos_produtos(
    id SERIAL PRIMARY KEY,
    descricao CHARACTER VARYING(50) NOT NULL
);

CREATE TABLE produtos(
    id SERIAL PRIMARY KEY,
    descricao CHARACTER VARYING(50) NOT NULL, 
    preco MONEY NOT NULL, 
    id_tipo_produto INT REFERENCES tipos_produtos(id) NOT NULL
);

CREATE TABLE pacientes(
    id SERIAL PRIMARY KEY,
    nome CHARACTER VARYING(50) NOT NULL,
    endereco CHARACTER VARYING(50) NOT NULL,
    bairro CHARACTER VARYING(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    estado CHAR(2) NOT NULL,
    CEP VARCHAR(9) NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE professor (
    idProfessor SERIAL PRIMARY KEY,
    nome CHARACTER VARYING(80) NOT NULL,
    telefone INT NOT NULL
);

CREATE TABLE turmas(
    idTurma SERIAL PRIMARY KEY,
    nome CHARACTER VARYING(80) NOT NULL,
    capacidade INT NOT NULL,
    idProfessor INT REFERENCES professor(idProfessor) NOT NULL
);

INSERT INTO tipos_produtos (descricao) VALUES ('Computadores');
INSERT INTO tipos_produtos (descricao) VALUES ('Impressora');
INSERT INTO tipos_produtos (descricao) VALUES ('Diversos');

INSERT INTO produtos (descricao, preco, id_tipo_produto) VALUES ('Notebook DELL 1544', 2345.7, 1);
INSERT INTO produtos (descricao, preco, id_tipo_produto) VALUES ('Impressora Jato de Tinta', 2345.7, 2);
INSERT INTO produtos (descricao, preco, id_tipo_produto) VALUES ('Mouse Sem Fio', 2345.7, 3);

INSERT INTO professor (nome,telefone) VALUES ('José', 11);
INSERT INTO professor (nome,telefone) VALUES ('Ronaldo', 11);
INSERT INTO turmas (nome, capacidade, idprofessor) VALUES ('Turma A', 25, 1);
INSERT INTO turmas (nome, capacidade, idprofessor) VALUES ('Turma B', 25, 2);

INSERT INTO pacientes (nome, endereco, bairro, cidade, estado, cep, data_nascimento) VALUES ('José', 'Rua Martim 1234', 'Pitaia', 'João Góis', 'SP', '02482147', '2001-06-09');
UPDATE produtos set descricao = 'Xbox', preco = 2400.50 WHERE id_tipo_produto = 3 AND descricao = 'Mouse Sem Fio';

SELECT * FROM produtos WHERE descricao LIKE 'Imp%';
DELETE FROM produtos WHERE descricao = 'Notebook DELL 1544'

ALTER TABLE produtos ADD quantidade INT;  

# CREATE USER estagiario WITH PASSWORD '12345'
# GRANT USAGE, SELECT ON SQUENCE empresas_id_seq TO estagiario
# REVOKE ALL ON empreasas to estagiario

# BEGIN TRANSACTION
# COMMIT


# SELECT * FROM tabela ORDER BY coluna DESC LIMIT 3
