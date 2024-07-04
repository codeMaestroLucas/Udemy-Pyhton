# Polimorphism - changing the behaivior of the methods, classes...

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, msg: str):
        self._msg = msg
        
    @abstractmethod
    def send_msg(self, msg: str) -> bool: ...
    
class Sms(Notification):
    def send_msg(self) -> bool:
        print(f"Sending SMS >>> {self._msg}")
        return True
    
class Email(Notification):
    def send_msg(self) -> bool:
        print(f"Sending Email >>> {self._msg}")
        return True
        
def notificate(notification: Notification):
    sended = notification.send_msg()
    
    if sended:
        print("Message sended")
    else:
        print("Message not sended")
        

sms = Sms('testing SMS')
email = Email('testing Email')

notificate(sms)
notificate(email)