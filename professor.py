from dadosProf import BancoDeDados
from funcionarios import funcionario
from curso import curso


class professor(funcionario):
    data = BancoDeDados(f'Professores.txt')
    formacao = ''
    disciplina = ''
    nivel = ''
    cr = curso()
    num = 0.0

    def cadastrarProfessor(self, nivel):
        self.nome = input('Nome:')
        self.rg = input('RG: ')
        self.cpf = input('Cpf: ')
        self.anonasc = int(input('Ano do Nascimento: '))
        self.mesnasc = int(input('Mes do Nascimento: '))
        self.dianasc = int(input('Dia do Nasc.:'))
        self.sexo = input('Gênero: ')
        self.matricula = int(input('Matricula: '))
        self.setor = input('Setor: ')
        self.cargo = 'professor'
        self.nivel = nivel
        self.formacao = input('Formação: ')
        self.disciplina = input('Disciplina: ')
        super().cadastrarFuncionario(self.nome, self.rg, self.cpf, self.anonasc, self.mesnasc, self.dianasc, self.sexo, self.matricula, self.setor, self.cargo, self.nivel)
        profe = [f'Matricula//{self.matricula}, {self.nome}, {self.rg}, {self.cpf}'
                 f'DATA de Nascimento: {self.dianasc}/{self.mesnasc}/{self.anonasc}'
                 f'Gênero: {self.sexo}'
                 f'funcionario(nivel){self.nivel}, Cargo: {self.cargo}Setor: {self.setor}, Formação: {self.formacao}'
                 f' Disciplina: {self.disciplina} || \n']
        self.profe = profe
        self.data.atualizar(self.profe)
        numMin = self.cr.calcNumMinAluno(nivel)
        self.num = numMin

    def exibirProfessor(self):
        super().listarfuncionario()
        print('\n Professor \n')
        print(f'Formação: {self.formacao}')
        print(f'Nivel: {self.nivel}')
        print(f'Disciplina: {self.disciplina}')
        print(f'Número Minimo de alunos para a matéria do professor: {self.num}')
        print('\n Arquivo do Professor')
        print(self.data.listar())




#pro1 = professor()
#pro1.cadastrarProfessor()
#pro1.exibirProfessor()
#print(pro1.sal.salarioBruto)
#print(pro1.sal.salarioLiquido)