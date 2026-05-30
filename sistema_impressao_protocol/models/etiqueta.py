class Etiqueta:
    def __init__(self, destinatario, endereco):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self):
        print(f"Etiqueta | Destinatário: {self.destinatario}")
        print(f"Endereço: {self.endereco}")
        