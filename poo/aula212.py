class Connection:
    def __init__(self, host: str = 'localhost'):
        # O "_" diz que o att deve ser usado somente dentro da classe.
        self._host = host
        self._user = None
        self._password = None
        
    @classmethod
    def create_connection(cls, user: str, password: str):
        cls()
        cls._user = user
        cls._password = password
        return cls
    
    @staticmethod
    def to_sum(*args: int):
        return sum(args)
    
    @staticmethod
    def log_mensage(msg: str):
        return f'Loggin: {msg}'
    
if __name__ == "__main__":
    c2 = Connection.create_connection('admin', '12435')
    print(c2._user, c2._password)
    
    print(c2.log_mensage("Log mensage here!"))