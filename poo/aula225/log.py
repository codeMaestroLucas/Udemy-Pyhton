from pathlib import Path

class Log:
    # Abstract class
    def _log(self, msg: str):
        raise NotImplementedError("Implement the method log.")
    
    def log_error(self, msg: str):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg: str):
        return self._log(f'Sucess: {msg}')
        
        
class LogPrintMixin(Log):
    def _log(self, msg: str):
        print(f'{msg}  >>> ({self.__class__.__name__})')
        

class LogFileMixin(Log):
    PATH_LOG: str = Path(__file__).parent / 'log.txt'

    def _log(self, msg: str):
        with open(self.PATH_LOG, '+a', encoding='utf8') as file:
            file.write(f'{msg}  >>> ({self.__class__.__name__})\n')