from pessoa import pessoa
from matricula import matricula


class aluno(pessoa):
    m = matricula()

    def __int__(self):
        self.codigo = 0
        self.desconto = 0.0
        self.interesse = ''

    def cadastrarAluno(self, codigo, desconto):
        self.nome = input('Nome:')
        self.rg = input('RG: ')
        self.cpf = input('Cpf: ')
        self.ano = int(input('Ano do Nascimento: '))
        self.mes = int(input('Mes do Nascimento: '))
        self.dia = int(input('Dia do Nasc.:'))
        self.sexo = input('Gênero: ')
        self.codigo = codigo
        self.interesse = input('Interesse em qual curso:')
        self.m.cadMatricula(desconto)
        self.desconto = desconto
        super().cadastrarPessoa(self.nome, self.rg, self.cpf, self.ano, self.mes, self.dia, self.sexo)

    def exibirAluno(self):
        print('\n Aluno \n')
        super().exibir()
        self.m.exibirMatricula()
        print(f'Código: {self.codigo}')
        print(f'Interresse: {self.interesse}')
        print(f'Desconto: {self.desconto}')
