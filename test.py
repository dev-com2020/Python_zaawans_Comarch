import abc
import random
import doctest


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class Fake(Tombola):
    def pick(self):
        return 11


class BingoClass(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('metoda pick z pustego...')

    def __call__(self):
        self.pick()


class Blower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('metoda pick() z pustego BingoClass')
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboLista(list):

    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('POP z pustego TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


# Tombola.register(TomboList) - stara wersja!


# issubclass(TomboLista,Tombola)
# t = TomboLista(range(100))
# isinstance(t,Tombola)
# TomboLista.__mro__


TEST_FILE = 'tombola_test.rst'
TEST_MSG = '{0:16} {1.próba:2} testy, {1.niepowodzenie:2} nieudane - {2}'


def main(argv):
    verbose = '-v' in argv
    real_subclasses = Tombola.__subclasses__()
    virtual_subclasses = list(Tombola._abc_registry)

    for cls in real_subclasses + virtual_subclasses:
        test(cls, verbose)


def test(cls, verbose=False):
    res = doctest.testfile(
        TEST_FILE,
        globs={'KonkretnaTombola': cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'FAIL' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))


if __name__ == '__main__':
    import sys

    main(sys.argv)
