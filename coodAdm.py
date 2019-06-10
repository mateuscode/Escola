from funcionarios import funcionario as fun
from salario import salario


class coordenadorAdm(fun):
    area = ''
    __plusSalario = 0.0
    st = salario()
    s = 0.0

    def cadastrarCoodAdm(self):
        self.area = input('Area: ')
        self.cargo = input('Cargo(professor ou tecnico: ')
        self.nivel = input('Nivel(A, B, C ,D ,E): ')
        self.nome = input('Nome:')
        self.rg = input('RG: ')
        self.cpf = input('Cpf: ')
        self.anonasc = int(input('Ano do Nascimento: '))
        self.mesnasc = int(input('Mes do Nascimento: '))
        self.dianasc = int(input('Dia do Nasc.:'))
        self.sexo = input('Gênero: ')
        self.matricula = int(input('Matricula: '))
        self.setor = input('Setor: ')
        super().cadastrarFuncionario(self.nome, self.rg, self.cpf, self.anonasc, self.mesnasc, self.dianasc, self.sexo, self.matricula,
                                     self.setor, self.cargo, self.nivel)
        sala = self.st.calcularSalario(self.cargo, self.nivel)
        self.s = sala

    def exibirCoodAdm(self):
        super().listarfuncionario()
        print('\n Coodenador Administrativo \n')
        print(f'Area: {self.area}')
        print(f'SalarioPlus: {self.s}')

    def calcPlusSalario(self):
        if self.nivel == 'A':
             acrescimo = 1520.25 * 0.135
             self.s = self.s + acrescimo
        elif self.nivel == 'B':
             acrescimo = 2362.67 * 0.135
             self.s = self.s + acrescimo
        elif self.nivel == 'C':
             acrescimo = 2988.92 * 0.135
             self.s = self.s + acrescimo
        elif self.nivel == 'D':
             acrescimo = 3572.77 * 0.135
             self.s = self.s + acrescimo
        elif self.nivel == 'E':
             acrescimo = 4878.67 * 0.135
             self.s = self.s + acrescimo
