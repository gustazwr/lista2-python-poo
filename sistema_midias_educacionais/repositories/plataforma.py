from models.midia import Midia
class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.lista_midias = []

    def adicionar_midia(self, midia):
        self.lista_midias.append(midia)
    
    def listar_midias(self):
        print(f"| Midias da Plataforma: {self.nome}|\n")
        for midia in self.lista_midias:
            midia.mostrar_info()
            print("-" * 30)
    
    def reproduzir_todas(self):
        print("\nReproduzindo todas as midias:\n")
        for midia in self.lista_midias:
            midia.reproduzir()