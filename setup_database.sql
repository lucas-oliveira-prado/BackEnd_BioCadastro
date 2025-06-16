use biocadastro;

CREATE TABLE animal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    sexo INT,
    raca INT,
    data_nascimento DATETIME,
    status INT
);

CREATE TABLE vacinacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    nome VARCHAR(100),
    data DATETIME,
    FOREIGN KEY (animal_id) REFERENCES animal(id)
);

CREATE TABLE pesagem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_animal INT,
    peso FLOAT(8,2),
    data DATETIME,
    FOREIGN KEY (id_animal) REFERENCES animal(id)
);

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PUC@123';
FLUSH PRIVILEGES;

INSERT INTO animal (nome, sexo, raca, data_nascimento, status) 
VALUES 
('Boi Bravo', 1, 2, '2020-05-15 00:00:00', 1),
('Vaca Mimosa', 2, 3, '2019-08-22 00:00:00', 1),
('Cavalo Preto', 1, 4, '2018-03-10 00:00:00', 1),
('Porca Rosa', 2, 5, '2021-11-30 00:00:00', 1); 