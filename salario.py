from calculo_salario import calculo_inss


class salario:
    salarioBruto = 0.0
    salarioLiquido = 0.0
    inss = 0.0
    irrf = 0.0
    planoSaude = 125.00

    def calcularSalario(self, cargo, nivel):
        if cargo == 'professor' and nivel == 'I':
            self.salarioBruto = 6500.00
            self.irrf = (self.salarioBruto - 869.36) * 27.5 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return float(self.salarioLiquido)
        elif cargo == 'professor' and nivel == 'II':
            self.salarioBruto = 8234.50
            self.irrf = (self.salarioBruto - 869.36) * 27.5 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return float(self.salarioLiquido)
        elif cargo == 'professor' and nivel == 'III':
            self.salarioBruto = 12568.43
            self.irrf = (self.salarioBruto - 869.36) * 27.5 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return float(self.salarioLiquido)
        elif cargo == 'tecnico' and nivel == 'A':
            self.salarioBruto = 1520.25
            self.irrf = (self.salarioBruto - 142.82) * 7.5 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return self.salarioLiquido
        elif cargo == 'tecnico' and nivel == 'B':
            self.salarioBruto = 2362.67
            self.irrf = (self.salarioBruto - 142.82) * 7.5 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return self.salarioLiquido
        elif cargo == 'tecnico' and nivel == 'C':
            self.salarioBruto = 2988.92
            self.irrf = (self.salarioBruto - 354.80) * 15 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return self.salarioLiquido
        elif cargo == 'tecnico' and nivel == 'D':
            self.salarioBruto = 3572.77
            self.irrf = (self.salarioBruto - 354.80) * 15 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return self.salarioLiquido
        elif cargo == 'tecnico' and nivel == 'E':
            self.salarioBruto = 4878.67
            self.irrf = (self.salarioBruto - 869.36) * 27.5 / 100
            self.inss = calculo_inss(self.salarioBruto)
            total = self.irrf + self.inss + self.planoSaude
            self.salarioLiquido = self.salarioBruto - total
            return float(self.salarioLiquido)
