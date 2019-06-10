from professor import professor as pr
from salario import salario


class coordenador(pr):
    area = ''
    __plusSalario = 0.0
    st = salario()
    s = 0.0

    def cadastrarCood(self, nivel):
        self.area = input('Area: ')
        self.nivel = nivel
        super().cadastrarProfessor(nivel)
        sala = self.st.calcularSalario(self.cargo, self.nivel)
        self.s = sala

    def exibirCood(self):
        super().exibirProfessor()
        print('\n Coordenador \n')
        print(f'Area: {self.area}')
        print(f'SalarioPlus: {self.s}')

    def calcPlusSalario(self):
        if self.nivel == 'I':
             acrescimo = 6500 * 0.15
             self.s = self.s + acrescimo
        elif self.nivel == 'II':
             acrescimo = 8325.50 * 0.15
             self.s = self.s + acrescimo
        elif self.nivel == 'III':
             acrescimo = 12568.43 * 0.15
             self.s = self.s + acrescimo
