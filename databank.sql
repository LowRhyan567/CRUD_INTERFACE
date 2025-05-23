create database if not exists Loja_Jogos;
use Loja_Jogos;

create table if not exists tb_categoria(
    cat_id int auto_increment primary key,
    nome_cat varchar(255),
    desc_cat text
);

create table if not exists tb_fornecedor(
    forn_id int auto_increment primary key,
    forn_nome varchar(255),
    forn_num varchar(255),
    forn_cnpj varchar(255),
    forn_email varchar(255),
    forn_end varchar(255)
);

create table if not exists tb_produtos(
    pro_id int auto_increment primary key,
    pro_nome varchar(255),
    prod_desc text,
    prod_preco decimal(10,2),
    qntd_estoque int,
    forn_id int,
    cat_id int,
    foreign key (forn_id) references tb_fornecedor(forn_id) on delete cascade,
    foreign key (cat_id) references tb_categoria(cat_id) on delete cascade
);

INSERT INTO tb_categoria (nome_cat, desc_cat) VALUES
('Ação', 'Jogos de ação e aventura'),
('RPG', 'Jogos de RPG e fantasia'),
('Esportes', 'Jogos de esportes e simulação');


INSERT INTO tb_fornecedor (forn_nome, forn_num, forn_cnpj, forn_email, forn_end) VALUES
('Fornecedor A', '11999999999', '12345678000100', 'fornecedorA@email.com', 'Rua A, 123'),
('Fornecedor B', '21988888888', '98765432000100', 'fornecedorB@email.com', 'Rua B, 456');
