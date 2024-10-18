# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes derivadas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura),
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmentros e retorno iguais
# SO"L"IDO
# Princípio da substituição de liskov
# Objetos de uma superclase devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload) 🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

 

class Notificacao(ABC):

    def __init__(self, mensagem):
        self.msg = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):

    def __init__(self, mensagem):
        super().__init__(mensagem)

    def enviar(self) -> bool: 
        print('Email: enviando -', self.msg)
        return True


class NotificacaoSMS(Notificacao):

    def __init__(self, mensagem):
        super().__init__(mensagem)

    def enviar(self) -> bool: 
        print('SMS: enviando -', self.msg)
        return False

###############################################################################

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada: 
        print('Notificação enviada')
    else:
        print('Notificação  NÃO enviada')



notificacao_email = NotificacaoEmail('Notificação E-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Notificação SMS')
notificar(notificacao_sms)
