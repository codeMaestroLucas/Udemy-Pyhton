# Exception

class MyError(Exception): ...
    
class AnotherError(Exception): ...


def raise_error(error: Exception):
    exception_ = error('a', 'b', 'c')
    raise exception_


try:
    raise_error(MyError)
    raise_error(AnotherError)
    
except (MyError, AnotherError) as error:
    print(error.__class__.__name__)
    print(error)
    print("Something done to the error log.\n")
    print('*' *40)
    print()
    raise_error(MyError)