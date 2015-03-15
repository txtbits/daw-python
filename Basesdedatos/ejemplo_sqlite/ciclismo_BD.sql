CREATE TABLE ciclista (
	dorsal NUMBER NOT NULL,
	nombre VARCHAR2(30) NOT NULL,
	edad NUMBER,
	nomeq VARCHAR2(25) NOT NULL,
	PRIMARY KEY (dorsal)
);
CREATE TABLE equipo (
	nomeq VARCHAR2(25) NOT NULL,
	director VARCHAR2(30) ,
	PRIMARY KEY (nomeq)
);
CREATE TABLE etapa (
	netapa NUMBER NOT NULL,
	km NUMBER NOT NULL,
	salida VARCHAR2(35)  NOT NULL,
	llegada VARCHAR2(35)  NOT NULL,
	dorsal NUMBER
);
CREATE TABLE llevar (
	netapa NUMBER NOT NULL,
	codigo VARCHAR2(3)  NOT NULL,
	dorsal NUMBER NOT NULL
);
CREATE TABLE maillot (
	codigo VARCHAR2(3)  NOT NULL,
	tipo VARCHAR2(30)  NOT NULL,
	color VARCHAR2(20)  NOT NULL,
	premio LONG NOT NULL
);
CREATE TABLE puerto (
	nompuerto VARCHAR2(35)  NOT NULL,
	altura NUMBER NOT NULL,
	categoria VARCHAR2(1)  NOT NULL,
	pendiente NUMBER,
	netapa NUMBER NOT NULL,
	dorsal NUMBER
);

INSERT INTO equipo (nomeq, director) VALUES ('Amore Vita', 'Ricardo Padacci');
INSERT INTO equipo (nomeq, director) VALUES ('Artiach', 'Jos� Per�z');
INSERT INTO equipo (nomeq, director) VALUES ('Banesto', 'Miguel Echevarria');
INSERT INTO equipo (nomeq, director) VALUES ('Bresciali-Refin', 'Pietro Armani');
INSERT INTO equipo (nomeq, director) VALUES ('Carrera', 'Luigi Petroni');
INSERT INTO equipo (nomeq, director) VALUES ('Castorama', 'Jean Philip');
INSERT INTO equipo (nomeq, director) VALUES ('Euskadi', 'Pedro Txucaru');
INSERT INTO equipo (nomeq, director) VALUES ('Gatorade', 'Gian Luca Pacceli');
INSERT INTO equipo (nomeq, director) VALUES ('Gewiss', 'Moreno Argentin');
INSERT INTO equipo (nomeq, director) VALUES ('Jolly Club', 'Johan Richard');
INSERT INTO equipo (nomeq, director) VALUES ('Kelme', '�lvaro Pino');
INSERT INTO equipo (nomeq, director) VALUES ('Lotus Festina', 'Suarez Cuevas');
INSERT INTO equipo (nomeq, director) VALUES ('Mapei-Clas', 'Juan Fernandez');
INSERT INTO equipo (nomeq, director) VALUES ('Mercatone Uno', 'Ettore Romano');
INSERT INTO equipo (nomeq, director) VALUES ('Motorola', 'John Fidwell');
INSERT INTO equipo (nomeq, director) VALUES ('Navigare', 'Lonrenzo Sciacci');
INSERT INTO equipo (nomeq, director) VALUES ('ONCE', 'Manuel Sainz');
INSERT INTO equipo (nomeq, director) VALUES ('PDM', 'Piet Van Der Kruis');
INSERT INTO equipo (nomeq, director) VALUES ('Seguros Amaya', 'Minguez');
INSERT INTO equipo (nomeq, director) VALUES ('Telecom', 'Morgan Reikcard');
INSERT INTO equipo (nomeq, director) VALUES ('TVM', 'Steveens Henk');
INSERT INTO equipo (nomeq, director) VALUES ('Wordperfect', 'Bill Gates');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (1, 'Miguel Indur�in', 32, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (2, 'Pedro Delgado', 35, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (3, 'Alex Zulle', 27, 'ONCE');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (4, 'Tony Rominger', 30, 'Mapei-Clas');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (5, 'Gert-Jan Theunisse', 32, 'TVM');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (6, 'Adriano Baffi', 33, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (7, 'Massimiliano Lelli', 30, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (8, 'Jean Van Poppel', 33, 'Lotus Festina');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (9, 'Massimo Podenzana', 34, 'Navigare');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (10, 'Mario Cipollini', 28, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (11, 'Flavio Giupponi', 31, 'Bresciali-Refin');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (12, 'Alessio Di Basco', 31, 'Amore Vita');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (13, 'Lale Cubino', 28, 'Seguros Amaya');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (14, 'Roberto Pagnin', 33, 'Navigare');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (15, 'Jesper Skibby', 31, 'TVM');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (16, 'Dimitri Konishev', 29, 'Jolly Club');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (17, 'Bruno Leali', 37, 'Bresciali-Refin');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (18, 'Robert Millar', 37, 'TVM');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (19, 'Julian Gorospe', 34, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (20, 'Alfonso Guti�rrez', 29, 'Artiach');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (21, 'Erwin Nijboer', 31, 'Artiach');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (22, 'Giorgio Furlan', 32, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (23, 'Lance Armstrong', 27, 'Motorola');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (24, 'Claudio Chiappucci', 29, 'Carrera');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (25, 'Gianni Bugno', 32, 'Gatorade');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (26, 'Mikel Zarrabeitia', 27, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (27, 'Laurent Jalabert', 28, 'ONCE');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (28, 'Jesus Montoya', 33, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (29, 'Angel Edo', 28, 'Kelme');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (30, 'Melchor Mauri', 28, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (31, 'Vicente Aparicio', 30, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (32, 'Laurent Dufaux', 28, 'ONCE');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (33, 'Stefano della Santa', 29, 'Mapei-Clas');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (34, 'Angel Yesid Camargo', 30, 'Kelme');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (35, 'Erik Dekker', 28, 'Wordperfect');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (36, 'Gian Matteo Fagnini', 32, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (37, 'Scott Sunderland', 29, 'TVM');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (38, 'Javier Palacin', 25, 'Euskadi');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (39, 'Rudy Verdonck', 30, 'Lotus Festina');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (40, 'Viatceslav Ekimov', 32, 'Wordperfect');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (41, 'Rolf Aldag', 25, 'Telecom');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (42, 'Davide Cassani', 29, 'TVM');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (43, 'Francesco Casagrande', 28, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (44, 'Luca Gelfi', 27, 'Gatorade');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (45, 'Alberto Elli', 26, 'Artiach');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (46, 'Agustin Sagasti', 24, 'Euskadi');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (47, 'Laurent Pillon', 32, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (48, 'Marco Saligari', 29, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (49, 'Eugeni Berzin', 23, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (50, 'Fernando Escartin', 27, 'Mapei-Clas');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (51, 'Udo Bolts', 30, 'Telecom');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (52, 'Vladislav Bobrik', 26, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (53, 'Michele Bartoli', 28, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (54, 'Steffen Wesemann', 30, 'Telecom');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (55, 'Nicola Minali', 28, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (56, 'Andrew Hampsten', 29, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (57, 'Stefano Zanini', 28, 'Navigare');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (58, 'Gerd Audehm', 34, 'Telecom');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (59, 'Mariano Picolli', 28, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (60, 'Giovanni Lombardi', 28, 'Bresciali-Refin');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (61, 'Walte Castignola', 26, 'Navigare');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (62, 'Raul Alcala', 30, 'Motorola');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (63, 'Alvaro Mejia', 32, 'Motorola');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (64, 'Giuseppe Petito', 28, 'Mercatone Uno');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (65, 'Pascal Lino', 29, 'Amore Vita');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (66, 'Enrico Zaina', 24, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (67, 'Armand de las Cuevas', 28, 'Castorama');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (68, 'Angel Citracca', 28, 'Navigare');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (69, 'Eddy Seigneur', 27, 'Castorama');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (70, 'Sandro Heulot', 29, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (71, 'Prudencio Indur�in', 27, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (72, 'Stefano Colage', 28, 'Bresciali-Refin');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (73, 'Laurent Fignon', 35, 'Gatorade');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (74, 'Claudio Chioccioli', 36, 'Amore Vita');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (75, 'Juan Romero', 32, 'Seguros Amaya');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (76, 'Marco Giovannetti', 34, 'Gatorade');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (77, 'Javier Mauleon', 33, 'Mapei-Clas');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (78, 'Antonio Esparza', 35, 'Kelme');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (79, 'Johan Bruyneel', 33, 'ONCE');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (80, 'Federico Echave', 37, 'Mapei-Clas');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (81, 'Piotr Ugrumov', 33, 'Gewiss');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (82, 'Edgar Corredor', 30, 'Kelme');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (83, 'Hernan Buenahora', 32, 'Kelme');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (84, 'Jon Unzaga', 31, 'Mapei-Clas');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (85, 'Dimitri Abdoujaparov', 30, 'Carrera');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (86, 'Juan Martinez Oliver', 32, 'Kelme');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (87, 'Fernando Mota', 32, 'Artiach');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (88, 'Angel Camarillo', 28, 'Mapei-Clas');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (89, 'Stefan Roche', 36, 'Carrera');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (90, 'Ivan Ivanov', 27, 'Artiach');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (91, 'Nestor Mora', 28, 'Kelme');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (92, 'Federico Garcia', 27, 'Artiach');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (93, 'Bo Hamburger', 29, 'TVM');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (94, 'Marino Alonso', 30, 'Banesto');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (95, 'Manuel Guijarro', 31, 'Lotus Festina');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (96, 'Tom Cordes', 29, 'Wordperfect');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (97, 'Casimiro Moreda', 28, 'ONCE');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (98, 'Eleuterio Anguita', 25, 'Artiach');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (99, 'Per Pedersen', 29, 'Seguros Amaya');
INSERT INTO ciclista (dorsal, nombre, edad, nomeq) VALUES (100, 'William Palacios', 30, 'Jolly Club');
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (1, 9, 'Valladolid', 'Valladolid', 1);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (2, 180, 'Valladolid', 'Salamanca', 36);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (3, 240, 'Salamanca', 'Caceres', 12);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (4, 230, 'Almendralejo', 'C�rdoba', 83);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (5, 170, 'C�rdoba', 'Granada', 27);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (6, 150, 'Granada', 'Sierra Nevada', 52);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (7, 250, 'Baza', 'Alicante', 22);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (8, 40, 'Benidorm', 'Benidorm', 1);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (9, 150, 'Benidorm', 'Valencia', 35);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (10, 200, 'Igualada', 'Andorra', 2);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (11, 195, 'Andorra', 'Estaci�n de Cerler', 65);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (12, 220, 'Benasque', 'Zaragoza', 12);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (13, 200, 'Zaragoza', 'Pamplona', 93);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (14, 172, 'Pamplona', 'Alto de la Cruz de la Demanda', 86);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (15, 207, 'Santo Domingo de la Calzada', 'Santander', 10);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (16, 160, 'Santander', 'Lagos de Covadonga', 5);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (17, 140, 'Cangas de Onis', 'Alto del Naranco', 4);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (18, 195, '�vila', '�vila', 8);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (19, 190, '�vila', 'Destilerias Dyc', 2);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (20, 52, 'Segovia', 'Destilerias Dyc', 2);
INSERT INTO etapa (netapa, km, salida, llegada, dorsal) VALUES (21, 170, 'Destilerias Dyc', 'Madrid', 27);
INSERT INTO maillot (codigo, tipo, color, premio) VALUES ('MGE', 'General', 'Amarillo', 8000000);
INSERT INTO maillot (codigo, tipo, color, premio) VALUES ('MMO', 'Monta�a', 'Blanco y Rojo', 2000000);
INSERT INTO maillot (codigo, tipo, color, premio) VALUES ('MMS', 'Mas Sufrido', 'Estrellitas moradas', 2000000);
INSERT INTO maillot (codigo, tipo, color, premio) VALUES ('MMV', 'Metas volantes', 'Rojo', 2000000);
INSERT INTO maillot (codigo, tipo, color, premio) VALUES ('MRE', 'Regularidad', 'Verde', 2000000);
INSERT INTO maillot (codigo, tipo, color, premio) VALUES ('MSE', 'Sprints especiales', 'Rosa', 2000000);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (1, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (1, 'MMO', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (1, 'MMS', 67);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (1, 'MMV', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (1, 'MRE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (1, 'MSE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (2, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (2, 'MMO', 25);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (2, 'MMS', 69);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (2, 'MMV', 16);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (2, 'MRE', 27);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (2, 'MSE', 8);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (3, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (3, 'MMO', 25);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (3, 'MMS', 67);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (3, 'MMV', 16);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (3, 'MRE', 27);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (3, 'MSE', 12);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (4, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (4, 'MMO', 24);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (4, 'MMS', 69);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (4, 'MMV', 17);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (4, 'MRE', 27);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (4, 'MSE', 8);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (5, 'MGE', 2);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (5, 'MMO', 25);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (5, 'MMV', 16);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (5, 'MRE', 27);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (5, 'MSE', 12);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (6, 'MGE', 2);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (6, 'MMO', 26);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (6, 'MMV', 16);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (6, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (6, 'MSE', 12);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (7, 'MGE', 2);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (7, 'MMO', 26);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (7, 'MMV', 33);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (7, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (7, 'MSE', 99);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (8, 'MGE', 4);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (8, 'MMO', 26);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (8, 'MMV', 33);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (8, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (8, 'MSE', 99);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (9, 'MGE', 26);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (9, 'MMO', 26);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (9, 'MMV', 48);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (9, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (9, 'MSE', 99);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (10, 'MGE', 26);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (10, 'MMO', 30);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (10, 'MMV', 48);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (10, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (10, 'MSE', 99);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (11, 'MGE', 3);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (11, 'MMO', 30);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (11, 'MMV', 48);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (11, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (11, 'MSE', 99);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (12, 'MGE', 3);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (12, 'MMO', 30);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (12, 'MMV', 48);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (12, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (12, 'MSE', 99);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (13, 'MGE', 30);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (13, 'MMO', 30);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (13, 'MMV', 48);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (13, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (13, 'MSE', 99);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (14, 'MGE', 30);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (14, 'MMO', 28);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (14, 'MMV', 42);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (14, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (14, 'MSE', 22);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (15, 'MGE', 30);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (15, 'MMO', 28);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (15, 'MMV', 42);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (15, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (15, 'MSE', 22);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (16, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (16, 'MMO', 28);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (16, 'MMV', 42);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (16, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (16, 'MSE', 22);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (17, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (17, 'MMO', 28);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (17, 'MMV', 42);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (17, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (17, 'MSE', 22);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (18, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (18, 'MMO', 26);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (18, 'MMV', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (18, 'MRE', 27);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (18, 'MSE', 10);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (19, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (19, 'MMO', 28);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (19, 'MMV', 42);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (19, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (19, 'MSE', 22);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (20, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (20, 'MMO', 28);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (20, 'MMV', 42);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (20, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (20, 'MSE', 22);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (21, 'MGE', 1);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (21, 'MMO', 2);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (21, 'MMV', 42);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (21, 'MRE', 20);
INSERT INTO llevar (netapa, codigo, dorsal) VALUES (21, 'MSE', 22);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Alto del Naranco', 565, '1', 6.9, 10, 30);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Arcalis', 2230, 'E', 6.5, 10, 4);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Cerler-Circo de Ampriu', 2500, 'E', 5.87, 11, 9);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Coll de la Comella', 1362, '1', 8.07, 10, 2);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Coll de Ordino', 1980, 'E', 5.3, 10, 7);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Cruz de la Demanda', 1850, 'E', 7, 11, 20);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Lagos de Covadonga', 1134, 'E', 6.86, 16, 42);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Navacerrada', 1860, '1', 7.5, 19, 2);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Puerto de Alisas', 672, '1', 5.8, 15, 1);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Puerto de la Morcuera', 1760, '2', 6.5, 19, 2);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Puerto de Mijares', 1525, '1', 4.9, 18, 24);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Puerto de Navalmoral', 1521, '2', 4.3, 18, 2);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Puerto de Pedro Bernardo', 1250, '1', 4.2, 18, 25);
INSERT INTO puerto (nompuerto, altura, categoria, pendiente, netapa, dorsal) VALUES ('Sierra Nevada', 2500, 'E', 6, 2, 26);