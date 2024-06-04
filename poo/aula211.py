class Connection:
    def __init__(self, host: str = 'localhost'):
        # O "_" diz que o att deve ser usado somente dentro da classe.
        self._host = host
        self._user = None
        self._password = None

    @property # Faz um método se comportar como um atributo -> chamamento sem os parênteses
    def user(self):
        return self._user
        
    @user.setter
    def user(self, user:str):
        self._user = user
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password: str):
        self._password = password

if __name__ == "__main__":
    c1 = Connection()
    print(c1.__dict__)
    print(c1.user) # Método usado como um att
    c1.user = 'admin'
    c1.password = '12435'
    print(c1.__dict__)