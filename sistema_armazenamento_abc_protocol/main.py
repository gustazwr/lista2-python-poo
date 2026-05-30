from models.armazenadorArquivo import ArmazenadorArquivo
from models.armazenadorBanco import ArmazenadorBanco
from models.armazenador_nuvem import ArmazenadorNuvem

from services.funcoes import (executar_salvamento_formal,executar_salvamento_flexivel)

arquivo = ArmazenadorArquivo()
banco = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

print("\n=== Salvamento Formal ===\n")

executar_salvamento_formal(arquivo,"dados.txt")

executar_salvamento_formal(banco,"clientes")

print("\n=== Salvamento Flexível ===\n")

executar_salvamento_flexivel(arquivo,"arquivo_flexivel.txt")

executar_salvamento_flexivel(banco,"usuarios")

executar_salvamento_flexivel(nuvem,"backup.zip")