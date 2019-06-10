from pessoa import pessoa
from salario import salario


class funcionario(pessoa):
    sal = salario()

    def __init__(self):
        self.matricula = 0
        self.setor = ''
        self.cargo = ''
        self.nivel = 0

    def cadastrarFuncionario(self, nome, rg, cpf, anoNas, mesnasc, diaNas, sexo, matricula, setor, cargo, nivel):
        super().cadastrarPessoa(nome, rg, cpf, anoNas, mesnasc, diaNas, sexo)
        self.matricula = matricula
        self.setor = setor
        self.cargo = cargo
        self.nivel = nivel
        self.sal.calcularSalario(cargo, nivel)

    def listarfuncionario(self):
        super().exibir()
        print('\n Funcionário \n')
        print(f'Matricula: {self.matricula}')
        print(f'Setor: {self.setor}')
        print(f'Cargo: {self.cargo}')
        print(f'Nivel: {self.nivel}')
