
-- ============================================
-- Remover tabelas existentes (se houver)
-- ============================================
DROP TABLE IF EXISTS supplier CASCADE;
DROP TABLE IF EXISTS type_product CASCADE;
DROP TABLE IF EXISTS company CASCADE;

-- ============================================
-- Criação das Tabelas
-- ============================================

-- Tabela Company
CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('ATIVO', 'INATIVO', 'SUSPENSO'))
);

-- Tabela Type Product
CREATE TABLE type_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cod VARCHAR(50) UNIQUE NOT NULL,
    company_id INTEGER NOT NULL,
    CONSTRAINT fk_type_product_company FOREIGN KEY (company_id) REFERENCES company(id) ON DELETE CASCADE
);

-- Tabela Supplier
CREATE TABLE supplier (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('ATIVO', 'INATIVO', 'SUSPENSO')),
    company_id INTEGER NOT NULL,
    CONSTRAINT fk_supplier_company FOREIGN KEY (company_id) REFERENCES company(id) ON DELETE CASCADE
);

-- ============================================
-- Inserção de Dados - Companies (30 registros)
-- ============================================

INSERT INTO company (name, cnpj, status) VALUES
('Tech Solutions Ltda', '12.345.678/0001-90', 'ATIVO'),
('Comercial Brasil S.A', '23.456.789/0001-01', 'ATIVO'),
('Distribuidora Norte', '34.567.890/0001-12', 'ATIVO'),
('Alimentos Frescos Ltda', '45.678.901/0001-23', 'ATIVO'),
('Eletrônicos Online', '56.789.012/0001-34', 'ATIVO'),
('Moda & Estilo', '67.890.123/0001-45', 'INATIVO'),
('Construção Total', '78.901.234/0001-56', 'ATIVO'),
('Auto Peças Master', '89.012.345/0001-67', 'ATIVO'),
('Farmácia Saúde', '90.123.456/0001-78', 'ATIVO'),
('Livraria Cultural', '01.234.567/0001-89', 'ATIVO'),
('Supermercado Bom Preço', '11.345.678/0001-90', 'ATIVO'),
('Indústria Metal Forte', '22.456.789/0001-01', 'ATIVO'),
('Cosméticos Bella', '33.567.890/0001-12', 'ATIVO'),
('Pet Shop Amigo Fiel', '44.678.901/0001-23', 'ATIVO'),
('Ferramentas Pro', '55.789.012/0001-34', 'ATIVO'),
('Bebidas Premium', '66.890.123/0001-45', 'ATIVO'),
('Móveis Decoração', '77.901.234/0001-56', 'ATIVO'),
('Informática Express', '88.012.345/0001-67', 'SUSPENSO'),
('Papelaria Office', '99.123.456/0001-78', 'ATIVO'),
('Esportes Total', '10.234.567/0001-89', 'ATIVO'),
('Brinquedos Alegria', '21.345.678/0001-90', 'ATIVO'),
('Jardim & Casa', '32.456.789/0001-01', 'ATIVO'),
('Calçados Fashion', '43.567.890/0001-12', 'ATIVO'),
('Laticínios São José', '54.678.901/0001-23', 'ATIVO'),
('Padaria Pão Quente', '65.789.012/0001-34', 'ATIVO'),
('Açougue Boi Gordo', '76.890.123/0001-45', 'ATIVO'),
('Floricultura Jardim', '87.901.234/0001-56', 'INATIVO'),
('Joalheria Diamante', '98.012.345/0001-67', 'ATIVO'),
('Ótica Visão Clara', '09.123.456/0001-78', 'ATIVO'),
('Lavanderia Clean', '19.234.567/0001-89', 'ATIVO');

-- ============================================
-- Inserção de Dados - Type Product (50 registros)
-- ============================================

INSERT INTO type_product (name, cod, company_id) VALUES
('Notebook', 'NB-001', 1),
('Desktop', 'DK-002', 1),
('Monitor', 'MN-003', 1),
('Arroz', 'AR-001', 4),
('Feijão', 'FJ-002', 4),
('Macarrão', 'MC-003', 4),
('Smartphone', 'SP-001', 5),
('Tablet', 'TB-002', 5),
('Fone de Ouvido', 'FN-003', 5),
('Camiseta', 'CM-001', 6),
('Calça Jeans', 'CJ-002', 6),
('Cimento', 'CM-001', 7),
('Tijolo', 'TJ-002', 7),
('Tinta', 'TN-003', 7),
('Filtro de Óleo', 'FO-001', 8),
('Pastilha de Freio', 'PF-002', 8),
('Paracetamol', 'PC-001', 9),
('Dipirona', 'DP-002', 9),
('Livro Ficção', 'LF-001', 10),
('Livro Técnico', 'LT-002', 10),
('Café', 'CF-001', 11),
('Açúcar', 'AC-002', 11),
('Leite', 'LT-003', 11),
('Parafuso', 'PR-001', 12),
('Chapa de Aço', 'CA-002', 12),
('Shampoo', 'SH-001', 13),
('Condicionador', 'CD-002', 13),
('Ração Cães', 'RC-001', 14),
('Ração Gatos', 'RG-002', 14),
('Furadeira', 'FR-001', 15),
('Martelo', 'MT-002', 15),
('Cerveja', 'CV-001', 16),
('Refrigerante', 'RF-002', 16),
('Sofá', 'SF-001', 17),
('Mesa', 'MS-002', 17),
('Impressora', 'IM-001', 18),
('Teclado', 'TC-002', 18),
('Caderno', 'CD-001', 19),
('Caneta', 'CN-002', 19),
('Bola de Futebol', 'BF-001', 20),
('Raquete de Tênis', 'RT-002', 20),
('Boneca', 'BN-001', 21),
('Carrinho', 'CR-002', 21),
('Vaso', 'VS-001', 22),
('Cortador de Grama', 'CG-002', 22),
('Tênis Esportivo', 'TE-001', 23),
('Sandália', 'SD-002', 23),
('Queijo', 'QJ-001', 24),
('Iogurte', 'IG-002', 24),
('Pão Francês', 'PF-001', 25);

-- ============================================
-- Inserção de Dados - Suppliers (45 registros)
-- ============================================

INSERT INTO supplier (name, cnpj, status, company_id) VALUES
('Fornecedor Tech Alpha', '10.111.222/0001-33', 'ATIVO', 1),
('Distribuidora Digital', '20.222.333/0001-44', 'ATIVO', 1),
('Atacado Brasil', '30.333.444/0001-55', 'ATIVO', 2),
('Grãos & Cereais', '40.444.555/0001-66', 'ATIVO', 4),
('Agro Distribuidor', '50.555.666/0001-77', 'ATIVO', 4),
('Importadora Eletrônicos', '60.666.777/0001-88', 'ATIVO', 5),
('Tech Import', '70.777.888/0001-99', 'ATIVO', 5),
('Confecções Modernos', '80.888.999/0001-00', 'INATIVO', 6),
('Materiais Construção Sul', '90.999.000/0001-11', 'ATIVO', 7),
('Cimento Forte', '11.000.111/0001-22', 'ATIVO', 7),
('Auto Parts Distribuidora', '22.111.222/0001-33', 'ATIVO', 8),
('Peças Originais', '33.222.333/0001-44', 'ATIVO', 8),
('Farmacêutica Nacional', '44.333.444/0001-55', 'ATIVO', 9),
('Medicamentos Genéricos', '55.444.555/0001-66', 'ATIVO', 9),
('Editora Livros Brasil', '66.555.666/0001-77', 'ATIVO', 10),
('Distribuidora Cultural', '77.666.777/0001-88', 'ATIVO', 10),
('Atacadista Alimentos', '88.777.888/0001-99', 'ATIVO', 11),
('Central de Abastecimento', '99.888.999/0001-00', 'ATIVO', 11),
('Siderúrgica Nacional', '10.999.000/0001-11', 'ATIVO', 12),
('Beleza & Cia', '21.000.111/0001-22', 'ATIVO', 13),
('Cosméticos Importados', '32.111.222/0001-33', 'ATIVO', 13),
('Pet Food Distribuidora', '43.222.333/0001-44', 'ATIVO', 14),
('Ferragens Industriais', '54.333.444/0001-55', 'ATIVO', 15),
('Ferramentas Profissionais', '65.444.555/0001-66', 'ATIVO', 15),
('Bebidas Brasil', '76.555.666/0001-77', 'ATIVO', 16),
('Indústria de Móveis', '87.666.777/0001-88', 'ATIVO', 17),
('Madeireira Central', '98.777.888/0001-99', 'ATIVO', 17),
('Distribuidor Tech', '09.888.999/0001-00', 'SUSPENSO', 18),
('Papéis & Escritório', '11.999.000/0001-11', 'ATIVO', 19),
('Artigos Esportivos Nacional', '22.000.111/0001-22', 'ATIVO', 20),
('Sports Import', '33.111.222/0001-33', 'ATIVO', 20),
('Brinquedos & Jogos', '44.222.333/0001-44', 'ATIVO', 21),
('Distribuidora Toy', '55.333.444/0001-55', 'ATIVO', 21),
('Plantas & Jardins', '66.444.555/0001-66', 'ATIVO', 22),
('Couros & Calçados', '77.555.666/0001-77', 'ATIVO', 23),
('Fábrica de Sapatos', '88.666.777/0001-88', 'ATIVO', 23),
('Laticínios Regional', '99.777.888/0001-99', 'ATIVO', 24),
('Cooperativa de Leite', '10.888.999/0001-00', 'ATIVO', 24),
('Moinho de Trigo', '21.999.000/0001-11', 'ATIVO', 25),
('Distribuidora de Pães', '32.000.111/0001-22', 'ATIVO', 25),
('Frigorífico São Paulo', '43.111.222/0001-33', 'ATIVO', 26),
('Carnes & Cia', '54.222.333/0001-44', 'ATIVO', 26),
('Flores & Plantas', '65.333.444/0001-55', 'INATIVO', 27),
('Joias & Pedras Preciosas', '76.444.555/0001-66', 'ATIVO', 28),
('Lentes & Armações', '87.555.666/0001-77', 'ATIVO', 29);

-- ============================================
-- Verificação dos Dados Inseridos
-- ============================================

SELECT 'Total de Companies:' AS info, COUNT(*) AS total FROM company;
SELECT 'Total de Type Products:' AS info, COUNT(*) AS total FROM type_product;
SELECT 'Total de Suppliers:' AS info, COUNT(*) AS total FROM supplier;

-- ============================================
-- Consultas de Exemplo
-- ============================================

-- Companies ativas
SELECT * FROM company WHERE status = 'ATIVO';

-- Tipos de produtos por company
SELECT c.name AS company_name, tp.name AS product_type, tp.cod
FROM type_product tp
JOIN company c ON tp.company_id = c.id
ORDER BY c.name, tp.name;

-- Suppliers por company
SELECT c.name AS company_name, s.name AS supplier_name, s.cnpj, s.status
FROM supplier s
JOIN company c ON s.company_id = c.id
ORDER BY c.name, s.name;

-- ============================================
-- FIM DO SCRIPT
-- ============================================
