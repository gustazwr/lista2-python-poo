from sistema_Funcionarios_emopresa.funcionario import Funcionario

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.lista_de_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n---- Lista de Funcionarios: {self.nome} -----\n")
        for funcionario in self.lista_de_funcionarios:
            funcionario.mostrar_dados()
            print("-"*30)
    
    def folha_pagamento(self):
        print("\n---- Folha de Pagamento ----\n")
        for funcionario in self.lista_de_funcionarios:
           pagamento = funcionario.calcular_pagamento()
           

        

