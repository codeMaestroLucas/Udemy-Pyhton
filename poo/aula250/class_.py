class Foo:
    """Class Documentation
    
    Used just to explain the documentation on the classes.
    """
    def __init__(self, foo) -> None:
        self._foo = foo
    
    @property
    def foo(self):
        return self._foo
    
    @foo.setter
    def foo(self, foo):
        self._foo = foo