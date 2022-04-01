USE projetomysql; 

CREATE TABLE fabricantes (id INT PRIMARY KEY, fabricante VARCHAR(45)) ENGINE = InnoDB;
CREATE TABLE medicos (id INT PRIMARY KEY, nome VARCHAR(100), crm VARCHAR(45)) ENGINE = InnoDB;
CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  endereco VARCHAR(200),
  telefone VARCHAR(20),
  cep VARCHAR(15),
  localidade VARCHAR(45),
  cpf VARCHAR(15)
) ENGINE = InnoDB;

CREATE TABLE compras (
  id INT,
  datas DATE,
  INDEX fk_compras (id_cliente ASC),
        FOREIGN KEY (id_cliente) 
            REFERENCES clientes (id)
            ON DELETE CASCADE
) ENGINE = InnoDB;