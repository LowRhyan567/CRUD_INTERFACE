create database Loja_jogos;
use Loja_jogos;

create table tb_categoria(
cat_id int auto_increment primary key,
cat_nome varchar(255),
cat_desc text
);

create table tb_fornecedor(
forn_id int auto_increment primary key,
forn_nome varchar(255),
forn_num varchar(255),
forn_cnpj varchar(255),
forn_email varchar(255),
forn_ende varchar(255)
);

create table tb_produto(
prod_id int auto_increment primary key,
prod_nome varchar(255),
prod_desc varchar(255),
prod_preco decimal(10,2),
quant_estoque int,
categoria_id int,
fornecedor_id int,
foreign key (categoria_id) references tb_categoria(cat_id),
foreign key (fornecedor_id) references tb_fornecedor(forn_id)
);

insert into tb_categoria (cat_id, cat_nome, cat_desc) values
('1','sobrevivencia','Jogos que focam na dificuldade da gameplay, buscando o realismo em situações complicadas');

use Loja_jogos;

insert into tb_fornecedor (forn_id, forn_nome, forn_num, forn_cnpj, forn_email, forn_ende) values
('1','Games Gen','11 95432 9877','58.170.589/0001-77','gamesgens@gmail.com','Rua das Palmeiras Imperiais, 789, Jardim das Flores, Campinas, SP, 13088-030');

insert into tb_fornecedor (forn_id, forn_nome, forn_num, forn_cnpj, forn_email, forn_ende) values
('2','Tech Solutions','11 98765 4321','12.345.678/0001-90','contact@techsolutions.com.br','Avenida das Nações Unidas, 1000, Brooklin, São Paulo, SP, 04578-000'),
('3','Food Express','19 91234 5678','98.765.432/0001-12','pedidos@foodexpress.com','Rua Augusta, 500, Consolação, São Paulo, SP, 01305-000'),
('4','Creative Arts','21 95555 1212','23.456.789/0001-34','info@creativearts.art','Rua da Carioca, 10, Centro, Rio de Janeiro, RJ, 20020-060'),
('5','Global Imports','41 99988 7766','65.432.109/0001-56','sales@globalimports.net','Avenida Paraná, 300, Bacacheri, Curitiba, PR, 82510-000');

select * from tb_categoria;

insert into tb_categoria (cat_id, cat_nome, cat_desc) values
('2','aventura','Jogos focados na exploração de lugares desocnhecidos e cheios de emoção'),
('3','terror','Jogos que buscam assustar o jogador de diversas maneiras'),
('4','RPG',' Jogos que exploram diferentes epocas temporais e que buscam aproveitar o maximo da imersão'),
('5','corrida','Jogos que Buscam trazer as emoções das pistas para dentro de sua casa'),
('6','cartas','Jogos estrategicos que estimulam o pensamento rapido'),
('7','Luta','Jogos competitivos entre lutadores'),
('8','Plataforma','Jogos 2D'),
('9','FPS',' Jogos de tiro competitivos'),
('10','Coop','Jogos que necessitam da ajuda de mais pessoas para conseguir o preogresso dentro do jogo'),
('11','Simulador','Jogos que tentam trazer o grande parte do realismo de certa area da vida real');
use Loja_jogos;
insert into tb_produto (prod_id, prod_nome, prod_desc, prod_preco, quant_estoque, categoria_id, fornecedor_id) values
('1','The Last Of us','Jogo que faz com que vc enfrente um apocalipse de montrsos humanoides que foram infectados por um fungo','199.90','99','1','1');

insert into tb_produto (prod_id, prod_nome, prod_desc, prod_preco, quant_estoque, categoria_id, fornecedor_id) values
('2','DayZ','Jogo online de sobrevivência em mundo aberto pós-apocalíptico com foco em interação entre jogadores','149.90','25','1','3'),
('3','Rust','Sobreviva em um ambiente multiplayer hostil com crafting, construção de bases e combate','119.50','40','1','2'),
('4','ARK: Survival Evolved','Sobreviva em uma ilha repleta de dinossauros e outras criaturas pré-históricas','159.99','35','1','5'),
('5','7 Days to Die','Jogo de sobrevivência em mundo aberto com elementos de terror, crafting, construção e defesa de hordas de zumbis','99.00','55','1','4'),
('6','Green Hell','Simulador de sobrevivência na selva amazônica, com foco em realismo e desafios ambientais','109.90','20','1','1'),
('7','Valheim','Jogo de exploração e sobrevivência em um mundo inspirado na mitologia nórdica','89.99','65','1','2'),
('8','Conan Exiles','Jogo de sobrevivência em mundo aberto ambientado no universo de Conan, o Bárbaro','139.00','30','1','4'),
('9','No Man\'s Sky','Jogo de exploração espacial e sobrevivência com um universo processual infinito','179.90','40','1','3'),
('10','Stranded Deep','Sobreviva após um acidente de avião em ilhas isoladas no Oceano Pacífico','79.50','50','1','5'),
('11','Raft','Aventura de sobrevivência em um oceano perigoso a bordo de uma jangada em expansão','99.99','25','1','1');

select * from tb_fornecedor;

insert into tb_produto (prod_id, prod_nome, prod_desc, prod_preco, quant_estoque, categoria_id, fornecedor_id) values
('17','Resident Evil Village','Jogo de terror de sobrevivência com elementos de ação em uma vila misteriosa','249.90','30','2','3'),
('18','Outlast','Jogo de terror em primeira pessoa com foco em stealth e horror psicológico em um hospício','89.00','45','2','1'),
('19','Amnesia: The Dark Descent','Jogo de terror de sobrevivência em primeira pessoa com ênfase em quebra-cabeças e evitar encontros','69.50','50','2','4'),
('20','Dead by Daylight','Jogo de terror multiplayer assimétrico onde um assassino caça quatro sobreviventes','99.99','60','2','2'),
('21','Phasmophobia','Jogo de terror investigativo cooperativo onde jogadores caçam fantasmas','79.99','35','2','5'),
('22','Alien: Isolation','Jogo de terror de sobrevivência em primeira pessoa com um Alien implacável como principal ameaça','119.90','25','2','1'),
('23','The Evil Within 2','Jogo de terror de sobrevivência em terceira pessoa com elementos psicológicos e combate','139.50','40','2','5'),
('24','Little Nightmares II','Jogo de terror e plataforma com foco em atmosfera sombria e quebra-cabeças','79.00','55','2','3'),
('25','SOMA','Jogo de terror de ficção científica com foco em narrativa e dilemas existenciais','99.50','30','2','2'),
('26','Layers of Fear','Jogo de terror psicológico em primeira pessoa com foco em exploração e uma narrativa perturbadora','59.99','65','2','4'),
('27','The Witcher 3: Wild Hunt','RPG de mundo aberto aclamado pela crítica com uma história rica e escolhas impactantes','199.99','40','3','2'),
('28','Elden Ring','RPG de ação e fantasia em mundo aberto com exploração vasta e combate desafiador','279.90','30','3','5'),
('29','Baldur\'s Gate 3','RPG baseado em turnos com forte ênfase em narrativa, escolhas e consequências','249.50','35','3','1'),
('30','Divinity: Original Sin 2','RPG tático com combate baseado em turnos e um mundo rico em interações','179.00','45','3','3'),
('31','Final Fantasy VII Remake','RPG de ação que reimagina um clássico com gráficos modernos e história expandida','219.90','25','3','4'),
('32','Persona 5 Royal','RPG de turno com elementos de simulação social e uma história envolvente','229.90','38','3','1'),
('33','Disco Elysium','RPG narrativo com foco em diálogo, escolhas e um sistema de habilidades único','159.00','42','3','4'),
('34','Pathfinder: Wrath of the Righteous','RPG isométrico com combate tático e uma história épica','189.50','32','3','2'),
('35','Pillars of Eternity II: Deadfire','RPG isométrico com exploração marítima e um mundo rico em lore','169.99','36','3','5'),
('36','Monster Hunter: World','RPG de ação com foco em caça de monstros gigantes em um mundo vasto','199.50','28','3','3'),
('37','Gran Turismo 7','Simulador de corrida com foco em realismo e uma vasta seleção de carros e pistas','299.90','35','4','3'),
('38','Forza Horizon 5','Jogo de corrida arcade em mundo aberto com paisagens deslumbrantes do México','249.00','40','4','1'),
('39','Assetto Corsa Competizione','Simulador de corrida focado na GT World Challenge com carros e circuitos oficiais','199.50','28','4','5'),
('40','Need for Speed Unbound','Jogo de corrida arcade com estilo visual único e foco em corridas de rua e personalização','219.99','32','4','2'),
('41','F1 23','Jogo oficial da Fórmula 1 com todos os carros, pilotos e circuitos da temporada','269.00','25','4','4'),
('42','Project CARS 3','Jogo de corrida com uma grande variedade de carros e pistas, com foco em acessibilidade','149.90','45','4','5'),
('43','Dirt Rally 2.0','Simulador de rally off-road com pistas desafiadoras e carros icônicos','129.50','30','4','2'),
('44','WRC 10','Jogo oficial do Campeonato Mundial de Rally com todos os eventos e carros da temporada','169.99','38','4','1'),
('45','GRID Legends','Jogo de corrida com foco em narrativa e corridas emocionantes com diversos tipos de veículos','179.00','22','4','4'),
('46','Burnout Paradise Remastered','Jogo de corrida arcade em mundo aberto com foco em destruição e corridas de alta velocidade','99.90','50','4','3')