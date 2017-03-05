import sys


class Const:
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise TypeError, "unable to set attr of a const object"
        else:
            self.__dict__[key] = value

    def __getattr__(self, key):
        if self.__dict__.has_key(key):
            return self.__dict__[key]
        else:
            return None


sys.modules[__name__] = Const()
