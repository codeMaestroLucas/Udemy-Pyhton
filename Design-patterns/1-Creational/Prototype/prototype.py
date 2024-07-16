from copy import deepcopy

class Prototype:
    """Class used to clone itself.
    """
    def clone(self):
        return deepcopy(self)