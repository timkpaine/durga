
class Record(object):
    _ins = []

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, create_pair(k, v))

    def __json__(self):
        return ''

    def __hash__(self):
        pass

    def __repr__(self):
        return self.__json__()


def create_pair(key, val):
    def get(self):
        if self._updated:
            pass
        return getattr(self, '__' + str(key))

    def set(self, val):
        setattr(self, '__' + str(key), val)
    return property(get, set)


def input(meth):
    def foo(self, *args, **kwargs):
        pass
    foo.__name__ = meth.__name__
    return foo


def output(meth):
    def foo(self, *args, **kwargs):
        pass
    foo.__name__ = meth.__name__
    return foo


def inout(meth):
    def foo(self, *args, **kwargs):
        pass
    foo.__name__ = meth.__name__
    return foo
