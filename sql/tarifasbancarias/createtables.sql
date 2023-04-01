CREATE SCHEMA IF NOT EXISTS tarifas;

CREATE TABLE IF NOT EXISTS tarifas.grupos (
    codigo VARCHAR,
    tipo VARCHAR,
    PRIMARY KEY (codigo)
);

CREATE TABLE IF NOT EXISTS tarifas.instituicoes (
    cnpj VARCHAR,
    nome VARCHAR,
    codigo VARCHAR
);

CREATE TABLE IF NOT EXISTS tarifas.tarifas (
    codigo_servico VARCHAR,
    servico VARCHAR,
    unidade VARCHAR,
    data_vigencia DATE,
    valor_maximo FLOAT,
    tipo_valor VARCHAR,
    periodicidade VARCHAR,
    cnpj VARCHAR
);

CREATE TABLE IF NOT EXISTS tarifas.tarifas_instituicoes(
    cnpj VARCHAR,
    nome VARCHAR,
    codigo VARCHAR,
    tipo VARCHAR,
    codigo_servico VARCHAR,
    servico VARCHAR,
    unidade VARCHAR,
    data_vigencia DATE,
    valor_maximo FLOAT,
    tipo_valor VARCHAR,
    periodicidade VARCHAR
);

CREATE TABLE IF NOT EXISTS tarifas.ouvidorias(
    cnpj VARCHAR,
    nome VARCHAR,
    ouvidor VARCHAR,
    website VARCHAR,
    telefone VARCHAR
);

CREATE TABLE IF NOT EXISTS tarifas.tarifas_ouvidorias(
    cnpj VARCHAR,
    nome VARCHAR,
    codigo VARCHAR,
    tipo VARCHAR,
    codigo_servico VARCHAR,
    servico VARCHAR,
    unidade VARCHAR,
    data_vigencia DATE,
    valor_maximo FLOAT,
    tipo_valor VARCHAR,
    periodicidade VARCHAR,
    ouvidor VARCHAR,
    website VARCHAR,
    telefone VARCHAR
);
