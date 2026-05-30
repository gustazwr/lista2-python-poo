from sistema_Funcionarios_emopresa.funcionarioAssalariado import FuncionarioAssalariado
from sistema_Funcionarios_emopresa.funcionarioHorista import FuncionarioHorista
from sistema_Funcionarios_emopresa.funcionarioComissionado import FuncionarioComissionado
from sistema_Funcionarios_emopresa.empresa import Empresa

funcionario1 = FuncionarioAssalariado("Carlos Silva","111.111.111-11",5000)

funcionario2 = FuncionarioHorista("Ana Souza","222.222.222-22",160,35)

funcionario3 = FuncionarioComissionado("Marcos Lima","333.333.333-33",20000,0.10)


empresa = Empresa("Tech Solutions")

empresa.adicionar_funcionario(funcionario1)
empresa.adicionar_funcionario(funcionario2)
empresa.adicionar_funcionario(funcionario3)

empresa.listar_funcionarios()

empresa.folha_pagamento()