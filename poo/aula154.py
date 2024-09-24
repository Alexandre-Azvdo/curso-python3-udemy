# metrod vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    # method - self, método de instância
    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password

    # @classmethod - cls, método de classe
    @classmethod
    def create_with_auth(cls, user, password):
        connetion = cls()
        connetion.user = user
        connetion.password = password
        return connetion
    
    # @staticmethod - método estático (❌self, ❌cls)
    @staticmethod
    def log(msg):
        print('LOG -', msg)


#c1 = Connection()
#c1.set_user('Luiz')
#c1.set_password('12345')

c1 = Connection.create_with_auth('Alexandre', '12345')

print(Connection.log('Essa é a mensagem!'))
print(c1.user)
print(c1.password)
