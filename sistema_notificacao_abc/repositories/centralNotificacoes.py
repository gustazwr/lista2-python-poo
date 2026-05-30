from models.notificador import Notificador

class CentralNotificacoes:
    def __init__(self):
        self.lista_notificadores = []
    
    def adicionar_notificador(self, notificar):
        self.lista_notificadores.append(notificar)

    def enviar_todos(self, mensagem):
        for notificador in self.lista_notificadores:
            notificador.notificar(mensagem)