CREATE DATABASE projeto;

USE projeto;

CREATE TABLE cargos(
pkCargo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
responsabilidades TEXT
);

CREATE TABLE setores(
pkSetor INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
descricao TEXT
);

CREATE TABLE tecnologias(
pkTecnologia INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
tipo VARCHAR(80) NOT NULL,
funcao VARCHAR(80) NOT NULL
);

CREATE TABLE enderecos(
pkEndereco INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
rua VARCHAR(150) NOT NULL,
CEP INT(8) NOT NULL UNIQUE KEY,
numero INT NOT NULL,
cidade VARCHAR(150) NOT NULL,
UF CHAR(2) NOT NULL,
bloco VARCHAR(50)
);

CREATE TABLE Pessoas(
pkPessoa INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
email VARCHAR(150) NOT NULL UNIQUE KEY,
CPF VARCHAR(11) NOT NULL,
fkEndereco INT NOT NULL,
FOREIGN KEY (fkEndereco) REFERENCES enderecos(pkEndereco)
);

CREATE TABLE feedbacks(
pkFeedback INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
nota INT NOT NULL CHECK (nota <= 10 AND nota >= 0),
descricao TEXT,
fkPessoa INT NOT NULL,
FOREIGN KEY (fkPessoa) REFERENCES pessoas(pkPessoa)
);

CREATE TABLE funcionario(
pkFuncionario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
fkPessoa INT NOT NULL,
fkCargo INT NOT NULL,
fkSetor INT NOT NULL,
FOREIGN KEY (fkPessoa) REFERENCES pessoas(pkPessoa),
FOREIGN KEY (fkCargo) REFERENCES cargos(pkCargo),
FOREIGN KEY (fkSetor) REFERENCES setores(pkSetor)
);

CREATE TABLE equipeResonsaveis(
pkEquipeResonsavel INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
fkResponsavel INT NOT NULL,
nomeEquipe VARCHAR(100) NOT NULL,
FOREIGN KEY (fkResponsavel) REFERENCES pessoas(pkPessoa)
);

CREATE TABLE equipeFuncionario(
pkEquipeFuncionario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
fkEquipeResonsaveis INT NOT NULL,
FOREIGN KEY (fkEquipeResonsaveis) REFERENCES equipeResonsaveis(pkEquipeResonsavel)
);

CREATE TABLE servico(
pkServico INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
custoEstimado DOUBLE NOT NULL,
prazoDeConclusao DATE NOT NULL,
servicoPrestado TEXT,
fkEquipeResonsaveis INT NOT NULL,
fkFeedback INT NOT NULL,
FOREIGN KEY (fkFeedback) REFERENCES feedbacks(pkFeedback),
FOREIGN KEY (fkFeedback) REFERENCES feedbacks(pkFeedback)
);

CREATE TABLE empresas(
pkEmpresa INT NOT NULL PRIMARY KEY,
nome VARCHAR(150) NOT NULL,
CNPJ VARCHAR(14) NOT NULL,
fkPessoaRepresentante INT NOT NULL,
fkEndereco INT NOT NULL,
FOREIGN KEY (fkEndereco) REFERENCES enderecos(pkEndereco),
FOREIGN KEY (fkPessoaRepresentante) REFERENCES pessoas(pkPessoa)
);

CREATE TABLE produtos(
pkProduto INT NOT NULL PRIMARY KEY,
nome VARCHAR(150) NOT NULL,
serial VARCHAR(150),
descricao TEXT
);

CREATE TABLE Clientes(
pkCliente INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
representante INT NOT NULL,
tipoDeEmpresa enum ("pessoaFisica", "pessoaJuridica"),
FOREIGN KEY (representante) REFERENCES pessoas(pkPessoa)
);

CREATE TABLE fornecedores(
pkFornecedor INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
fkEmpresa INT NOT NULL,
FOREIGN KEY (fkEmpresa) REFERENCES empresas(pkEmpresa)
);

CREATE TABLE compras(
pkCompra INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
quantidade INT NOT NULL,
precoUnitario DECIMAL(10,2) NOT NULL,
fkProduto INT NOT NULL,
fkFornecedor INT NOT NULL,
FOREIGN KEY (fkProduto) REFERENCES produtos(pkProduto),
FOREIGN KEY (fkFornecedor) REFERENCES fornecedores(pkFornecedor)
);