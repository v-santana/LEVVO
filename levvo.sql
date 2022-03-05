CREATE TABLE IF NOT EXISTS tb_cliente (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR(100) NOT NULL,
    email       VARCHAR(50) NOT NULL,
    senha       VARCHAR(50) NOT NULL,
    telefone    VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_entregador(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    nome        VARCHAR(100) NOT NULL,
    email       VARCHAR(50) NOT NULL,
    senha       VARCHAR(50) NOT NULL,
    telefone    VARCHAR(20) NOT NULL,
    placa       VARCHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_entrega(
    id                      INT AUTO_INCREMENT PRIMARY KEY,
    descricao               VARCHAR(200) NOT NULL,
    id_endereco_coleta      INT NOT NULL,
    id_endereco_final       INT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_endereco(
    id              INT AUTO_INCREMENT PRIMARY KEY,
    rua             VARCHAR(200) NOT NULL,
    numero          INT NOT NULL,
    complemento     VARCHAR(200),
    CEP             VARCHAR(10),
    id_bairro       INT
)

select * from tb_cliente;
SELECT * FROM tb_entregador;