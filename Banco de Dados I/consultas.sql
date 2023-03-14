-- Consultas

-- Dados de cada aluno matriculado na academia e as modalidades em que estao matriculados:

select
	a.nome,
	a.endereco,
	a.telefone,
	t.tipo_atividade 
from
	aluno a
join matricula m on
	m.id_matricula = a.id_aluno
join turma t on
	t.id_turma = m.id_matricula 

--Dados de cada instrutor da academia, e os horarios de suas turmas:
	
select
	i.nome,
	i.cpf,
	i.data_nascimento,
	ti.numero,
	t.id_turma,
	t.horario_aula
from
	instrutor i
join tel_instrutor ti on
	ti.id_tel = i.id_instrutor
join turma t on
	t.id_turma = i.id_instrutor 
	
--Horario de aula de um aluno especifico:
	
select
	a.nome,
	t.id_turma,
	t.horario_aula
from
	aluno a
join turma t on
	t.id_turma = a.id_aluno
where
	a.nome = 'Emilia'
	
--Faltas de um aluno especifico com base nas turmas em que esta matriculado:
	
select
	a.nome,
	m.id_turma,
	count(rp.presente) n_faltas
from
	registro_presenca rp
join matricula m on
	m.id_matricula = rp.id_matricula
join aluno a on
	a.id_aluno = m.id_matricula
where
	m.id_turma = 2
	and rp.presente = false
	and a.nome = 'Thais'
group by
	a.nome,
	m.id_turma
