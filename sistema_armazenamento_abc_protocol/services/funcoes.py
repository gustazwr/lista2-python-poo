from models.armazenador import Armazenador
from models.salvavel import Salvavel


def executar_salvamento_formal(armazenador: Armazenador,dado):
    armazenador.salvar(dado)

def executar_salvamento_flexivel(objeto: Salvavel,dado):
    objeto.salvar(dado)