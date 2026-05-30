from models.midia import Midia
class Texto_Narrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma
    def reproduzir(self):
        print(f"| Reproduzindo Texto Narrado:{self.titulo} | Duração:{self.duracao} minutos | Idioma: {self.idioma} |")





