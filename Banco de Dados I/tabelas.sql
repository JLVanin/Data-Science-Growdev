
CREATE TABLE instrutor(
	id_instrutor int not null,
	nome varchar(50) not null,
	cpf varchar(11) not null unique,
	data_nascimento date not null,
	titulacao varchar(50),
	reg_profissional int,
	tel_instrutor int NOT NULL,
	constraint pk_instrutor primary key (id_instrutor)
);

CREATE TABLE atividade( 
	id_atividade int not null,
	nome varchar(50) not null,
	constraint pk_atividade primary key (id_atividade)
);


CREATE TABLE turma( 
	id_turma int not null,
	horario_aula time not null,
	duracao_aula float not null,
	data_inicial date not null,
	data_final date not null,
	id_atividade int not null,
	id_instrutor int not null,
	constraint pk_turma primary key (id_turma),
	constraint fk_atividade foreign key (id_atividade) references atividade(id_atividade),
	constraint fk_instrutor foreign key (id_instrutor) references instrutor(id_instrutor)
); 

CREATE TABLE aluno( 
	id_aluno int not null,
	nome varchar(50) not null,
	endereco varchar(50),
	telefone int not null,
	data_nascimento date not null,
	altura float not null,
	peso float not null,
 	ultima_avl_medica date,
 	observacoes varchar(100),
 	id_turma int not null,
 	constraint pk_aluno primary key (id_aluno)
); 

CREATE TABLE matricula( 
	id_matricula int not null,
	id_aluno int not null,
	id_turma int not null,
	constraint pk_matricula primary key (id_matricula),
	constraint fk_aluno foreign key (id_aluno) references aluno(id_aluno),
	constraint fk_turma foreign key (id_turma) references turma(id_turma)
); 

CREATE TABLE registro_presenca( 
	id_matricula int not null,
	data_presenca date not null,
	presente boolean not NULL,
	constraint fk_registro foreign key (id_matricula) references matricula(id_matricula)
);