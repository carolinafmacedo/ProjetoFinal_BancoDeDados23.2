from functions.create_database import create_database

create_database(
    database_name = 'streaming.db'
)

from functions.create_table import create_table

# tabela de clientes

create_table(
    database_name = 'streaming.db',
    table_name = 'dados_Cliente',
    columns ='id_Cliente INTEGER PRIMARY KEY, nome_Cliente VARCHAR (50), sobrenome_Cliente VARCHAR (50), email_Cliente VARCHAR (50), celular_Cliente VARCHAR (50), id_Endereco INTEGER, senha_Cliente VARCHAR (50), data_Criacao DATE, id_Assinatura INTEGER, FOREIGN KEY (id_Endereco) REFERENCES endereco(id_Endereco), FOREIGN KEY (id_Assinatura) REFERENCES assinatura(id_Assinatura)'
)

from functions.insert_rows import insert_many_rows

insert_many_rows(
'streaming.db', 'dados_Cliente', 'id_Cliente, nome_Cliente, sobrenome_Cliente, email_Cliente, celular_Cliente, id_Endereco, senha_Cliente, data_Criacao, id_Assinatura',
[   (1, "João", "Silva", "joao.silva@email.com", "123456789", 1, "senha123", "2023-01-01", 1), 
    (2, "Maria", "Santos", "maria.santos@email.com", "987654321", 2, "senha456", "2023-01-02", 2),
    (3, "Carlos", "Ribeiro", "carlos.ribeiro@email.com", "555666777", 3, "senha789", "2023-01-03", 3),
    (4, "Ana", "Oliveira", "ana.oliveira@email.com", "999000111", 4, "senhaabc", "2023-01-04", 4),
    (5, "Lucas", "Pereira", "lucas.pereira@email.com", "444333222", 5, "senhaxyz", "2023-01-05", 5),
    (6, "Julia", "Costa", "julia.costa@email.com", "111222333", 6, "senhajkl", "2023-01-06", 6),
    (7, "Roberto", "Almeida", "roberto.almeida@email.com", "999888777", 7, "senha456", "2023-01-07", 7),
    (8, "Fernanda", "Machado", "fernanda.machado@email.com", "555444333", 8, "senha789", "2023-01-08", 8),
    (9, "Pedro", "Rocha", "pedro.rocha@email.com", "222333444", 9, "senha123", "2023-01-09", 9),
    (10, "Larissa", "Ferreira", "larissa.ferreira@email.com", "777888999", 10, "senhaabc", "2023-01-10", 10),
    (11, "Ricardo", "Nunes", "ricardo.nunes@email.com", "333222111", 11, "senha789", "2023-01-11", 11),
    (12, "Camila", "Santana", "camila.santana@email.com", "888777666", 12, "senha123", "2023-01-12", 12),
    (13, "Gustavo", "Lima", "gustavo.lima@email.com", "444555666", 13, "senhaabc", "2023-01-13", 13),
    (14, "Aline", "Fernandes", "aline.fernandes@email.com", "999000111", 14, "senha789", "2023-01-14", 14),
    (15, "Marcelo", "Ramos", "marcelo.ramos@email.com", "111222333", 15, "senha123", "2023-01-15", 15),
    (16, "Patricia", "Mendes", "patricia.mendes@email.com", "666555444", 16, "senhaabc", "2023-01-16", 16),
    (17, "Eduardo", "Oliveira", "eduardo.oliveira@email.com", "222333444", 17, "senha789", "2023-01-17", 17),
    (18, "Raquel", "Pereira", "raquel.pereira@email.com", "777888999", 18, "senha123", "2023-01-18", 18),
    (19, "Vinicius", "Santos", "vinicius.santos@email.com", "333222111", 19, "senhaabc", "2023-01-19", 19),
    (20, "Isabela", "Lima", "isabela.lima@email.com", "888777666", 20, "senha789", "2023-01-20", 20)]
 )

# tabela de endereços

create_table(
    database_name = 'streaming.db',
    table_name = 'endereco',
    columns ='id_Endereco INTEGER PRIMARY KEY, CEP_Endereco VARCHAR (50), Cidade_Endereco VARCHAR (50), Bairro_Endereco VARCHAR (50), Rua_Endereco VARCHAR (50), Numero_residencia VARCHAR (50)'
)

insert_many_rows(
'streaming.db', 'endereco', 'id_Endereco, CEP_Endereco, Cidade_Endereco, Bairro_Endereco, Rua_Endereco, Numero_residencia',
[   (1, '12345-678', 'São Paulo', 'Centro', 'Rua A', '123'),
    (2, '54321-876', 'Rio de Janeiro', 'Copacabana', 'Avenida B', '456'),
    (3, '98765-432', 'Belo Horizonte', 'Savassi', 'Rua C', '789'),
    (4, '23456-789', 'Porto Alegre', 'Moinhos de Vento', 'Avenida D', '101'),
    (5, '87654-321', 'Brasília', 'Asa Sul', 'Rua E', '202'),
    (6, '34567-890', 'Salvador', 'Barra', 'Avenida F', '303'),
    (7, '87654-321', 'Fortaleza', 'Meireles', 'Rua G', '404'),
    (8, '23456-789', 'Recife', 'Boa Viagem', 'Avenida H', '505'),
    (9, '98765-432', 'Curitiba', 'Batel', 'Rua I', '606'),
    (10, '54321-876', 'Manaus', 'Adrianópolis', 'Avenida J', '707'),
    (11, '12345-678', 'Vitória', 'Praia do Canto', 'Rua K', '808'),
    (12, '87654-321', 'Natal', 'Ponta Negra', 'Avenida L', '909'),
    (13, '23456-789', 'Florianópolis', 'Centro', 'Rua M', '1010'),
    (14, '98765-432', 'Goiania', 'Setor Bueno', 'Avenida N', '1111'),
    (15, '54321-876', 'Maceió', 'Pajuçara', 'Rua O', '1212'),
    (16, '12345-678', 'João Pessoa', 'Tambaú', 'Avenida P', '1313'),
    (17, '87654-321', 'Campo Grande', 'Centro', 'Rua Q', '1414'),
    (18, '23456-789', 'Cuiabá', 'Araés', 'Avenida R', '1515'),
    (19, '98765-432', 'Teresina', 'Centro', 'Rua S', '1616'),
    (20, '54321-876', 'São Luís', 'Cohama', 'Avenida T', '1717')]
 )

 # tabela de pagamento

create_table(
    database_name = 'streaming.db',
    table_name = 'pagamento',
    columns ='id_Pagamento INTEGER PRIMARY KEY, id_Cliente INTEGER, forma_Pagamento VARCHAR (50)'
)

insert_many_rows(
'streaming.db', 'pagamento', 'id_Pagamento, id_Cliente, forma_Pagamento',
[   (1, 1, 'Cartão de Crédito'),
    (2, 2, 'Boleto Bancário'),
    (3, 3, 'Transferência Bancária'),
    (4, 4, 'Cartão de Débito'),
    (5, 5, 'Pix'),
    (6, 6, 'Cartão de Crédito'),
    (7, 7, 'Boleto Bancário'),
    (8, 8, 'Transferência Bancária'),
    (9, 9, 'Cartão de Débito'),
    (10, 10, 'Pix'),
    (11, 11, 'Cartão de Crédito'),
    (12, 12, 'Boleto Bancário'),
    (13, 13, 'Transferência Bancária'),
    (14, 14, 'Cartão de Débito'),
    (15, 15, 'Pix'),
    (16, 16, 'Cartão de Crédito'),
    (17, 17, 'Boleto Bancário'),
    (18, 18, 'Transferência Bancária'),
    (19, 19, 'Cartão de Débito'),
    (20, 20, 'Pix')]
 )

# tabela de assinatura

create_table(
    database_name = 'streaming.db',
    table_name = 'assinatura',
    columns ='id_Assinatura INTEGER PRIMARY KEY, id_Cliente INTEGER, id_Pagamento INTEGER, tipo_Assinatura VARCHAR (50), FOREIGN KEY (id_Pagamento) REFERENCES pagamento(id_Pagamento)'
)

insert_many_rows(
'streaming.db', 'assinatura', 'id_Assinatura, id_Cliente, id_Pagamento, tipo_Assinatura',
[   (1, 1, 1, 'Básica'),
    (2, 2, 2, 'Premium'),
    (3, 3, 3, 'Premium Plus'),
    (4, 4, 4, 'Básica'),
    (5, 5, 5, 'Premium'),
    (6, 6, 6, 'Premium Plus'),
    (7, 7, 7, 'Básica'),
    (8, 8, 8, 'Premium'),
    (9, 9, 9, 'Premium Plus'),
    (10, 10, 10, 'Básica'),
    (11, 11, 11, 'Premium'),
    (12, 12, 12, 'Premium Plus'),
    (13, 13, 13, 'Básica'),
    (14, 14, 14, 'Premium'),
    (15, 15, 15, 'Premium Plus'),
    (16, 16, 16, 'Básica'),
    (17, 17, 17, 'Premium'),
    (18, 18, 18, 'Premium Plus'),
    (19, 19, 19, 'Básica'),
    (20, 20, 20, 'Premium')]
 )
