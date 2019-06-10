from funcionarios import funcionario
from alunos import aluno
from coordenador import coordenador
from coodAdm import coordenadorAdm
from professor import professor

def exibir():
    selecao = int(input('(1) Exibir Aluno'
                    '(2) Exibir Professor'
                    '(3) Exibir Funcionário'
                    '(4) Exibir Professor Coordenador'
                    '(5) Exibir Coordenador Adm'))
    if selecao == 1:
