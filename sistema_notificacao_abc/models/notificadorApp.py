from models.notificador import Notificador

class NotificadorApp(Notificador):

    def notificar(self, mensagem):
        print("[APP]")
        print(mensagem)