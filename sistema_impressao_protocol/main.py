from models.boleto import Boleto
from models.etiqueta import Etiqueta
from models.relatorio_simples import RelatorioSimples
from services.processador import processar_impressao

boleto = Boleto("123456789",350.90)

etiqueta = Etiqueta("Carlos Silva","Rua das Flores, 120")

relatorio = RelatorioSimples("Relatório Financeiro")

processar_impressao(boleto)

print("-" * 40)

processar_impressao(etiqueta)

print("-" * 40)

processar_impressao(relatorio)