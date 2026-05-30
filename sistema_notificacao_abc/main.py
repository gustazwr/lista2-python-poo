from models.notificadorEmail import NotificadorEmail
from models.notificadorSMS import NotificadorSMS
from models.notificadorApp import NotificadorApp
from repositories.centralNotificacoes import CentralNotificacoes

central = CentralNotificacoes()

email = NotificadorEmail()

sms = NotificadorSMS()

app = NotificadorApp()

central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

central.enviar_todos(
    "Sua atividade foi enviada com sucesso!"
)