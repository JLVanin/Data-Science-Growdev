
insert into instrutor values
	(001, 'Jose', '000', '1990-01-01','M', 1254, 99991111),
	(002, 'Luiz', '111', '1991-02-02', 'D', 2415, 88882222),
	(003, 'Joao', '222', '1992-03-03', 'D', 23658, 99991122),
	(004, 'Amanda','333', '1993-04-04', 'B', 4758, 44415632),
	(005, 'Barbara','444', '1993-04-04', 'B', 7758, 99994444);

insert into atividade values
	(1, 'ginastica'),
	(2, 'danca'),
	(3, 'artes_marciais'),
	(4, 'musculacao');
	
insert into turma values
	(01, '07:00', 50, '2022-02-01', '2022-05-01', 1, 004),
	(02, '08:00', 50, '2022-02-01', '2022-05-01', 2, 003),
	(03, '05:00', 50, '2022-02-01', '2022-05-01', 3, 001),
	(04, '06:00', 50, '2022-02-01', '2022-05-01', 4, 002),
	(05, '07:00', 50, '2022-02-01', '2022-05-01', 4, 005);

insert into aluno values 
	 (001,'Emilia', 'Rua A', '999999999', '1998-01-26', '1.65', 55, '1998-01-26', null, 01),
	 (002,'Tha�s', 'Rua B', '999999999','1997-01-26', '1.70', 70, '2021-01-26', null, 02),
	 (003,'Terezinha', 'Rua C', '999999999','1997-01-26', '1.74', 75, '2021-01-26', null, 03),
	 (004,'Maidi', 'Rua D', '999999999','1997-01-26', '1.80', 80, '2021-01-26', null, 04),
	 (005,'Lorena', 'Rua E', '999999999','1997-01-26', '1.59', 60, '2021-01-26', null, 05);	 
	
insert into matricula values
	(01, 001, 01),
	(02, 002, 02),
	(03, 003, 03),
	(04, 004, 04),
	(05, 005, 05);

insert into registro_presenca values
	(01, '2022-02-03', true),
	(02, '2022-02-03', false),
	(03, '2022-02-03', false),
	(04, '2022-02-03', true),
	(05, '2022-02-03', true);