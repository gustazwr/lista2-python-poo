from models.notificador import Notificador

class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print("[SMS]")
        print(mensagem)