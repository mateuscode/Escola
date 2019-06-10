from funcionarios import funcionario
from alunos import aluno
from coordenador import coordenador
from coodAdm import coordenadorAdm
from professor import professor
import sys


def menu():
    print('\n MENU \n')
    print('Cadastro e Exibir')
    selecaoI = int(input('(1) Aluno \n'
                        '(2) Professor \n'
                        '(3) Funcionario \n'
                        '(4) Professor coordenador \n'
                        '(5) Técnico Administrativo Coordenador \n'
                        '(7) Finalizar \n'))

    if selecaoI == 1:
        a = aluno()
        cod = input('Código do Aluno: ')
        desc = int(input('Desconto do curso: '))
        a.cadastrarAluno(cod, desc)

    elif selecaoI == 2:
        prof = professor()
        nivel = input('Nivel do Professor(I, II, III): ')
        prof.cadastrarProfessor(nivel)

    elif selecaoI == 3:
        func = funcionario()
        setor = input('Setor: ')
        cargo = input('Cargo(professor ou tecnico): ')
        nivel = input('Nivel(A, B, C, D, E): ')
        nome = input('Nome:')
        rg = input('RG: ')
        cpf = input('Cpf: ')
        anonasc = int(input('Ano do Nascimento: '))
        mesnasc = int(input('Mes do Nascimento: '))
        dianasc = int(input('Dia do Nasc.:'))
        sexo = input('Gênero: ')
        matricula = int(input('Matricula: '))
        func.cadastrarFuncionario(nome, rg, cpf, anonasc, mesnasc, dianasc, sexo, matricula, setor, cargo, nivel)

    elif selecaoI == 4:
        profCord = coordenador()
        nivelCord = input('Nivel do Professor Coordenador(I, II, III)')
        profCord.cadastrarCood(nivelCord)

    elif selecaoI == 5:
        tecadm = coordenadorAdm()
        tecadm.cadastrarCoodAdm()
    elif selecaoI == 7:
        sys.exit()

    selecao = int(input('(1) Exibir Aluno'
                        '(2) Exibir Professor'
                        '(3) Exibir Funcionário'
                        '(4) Exibir Professor Coordenador'
                        '(5) Exibir Coordenador Adm'
                        '(6) sair'))
    if selecao == 1:
        a.exibirAluno()
        menu()
    elif selecao == 2:
        prof.exibirProfessor()
        print(f'Salario Bruto: {prof.sal.salarioBruto}')
        print(f'Salario Líquido: {prof.sal.salarioLiquido}')
        menu()
    elif selecao == 3:
        func.listarfuncionario()
        print(f'Salario Bruto: {func.sal.salarioBruto}')
        print(f'Salario Líquido: {func.sal.salarioLiquido}')
        menu()
    elif selecao == 4:
        profCord.calcPlusSalario()
        profCord.exibirCood()
        print(f'Salario Bruto: {profCord.sal.salarioBruto}')
        print(f'Salario Líquido: {profCord.sal.salarioLiquido}')
        menu()

    elif selecao == 5:
        tecadm.calcPlusSalario()
        tecadm.exibirCoodAdm()
        print(f'Salario Bruto: {tecadm.sal.salarioBruto}')
        print(f'Salario Líquido: {tecadm.sal.salarioLiquido}')
        menu()

    else:
        sys.exit()


menu()