

class Solution:

    def __init__(self, input=None, output=None):
        self._input = input
        self._output = output

    @property
    def input(self):
        return self._input

    @property
    def output(self):
        return self._output

    def _read(self, f):
        raise NotImplementedError

    def _write(self, f, answer):
        raise NotImplementedError

    def solve(self, data):
        raise NotImplementedError

    def test(self):
        pass

    @classmethod
    def __all_subclasses__(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.__all_subclasses__()
            yield subclass

    @staticmethod
    def algorithm(name, input=None, output=None):
        cls = None
        for subcls in Solution.__all_subclasses__():
            if subcls.__name__ == name:
                cls = subcls
                break

        if cls is None:
            raise ValueError("Unknown task: '{}'".format(name))

        return cls(input=input, output=output)

    @staticmethod
    def go(name, input, output):
        alg = Solution.algorithm(name, input=input, output=output)

        with open(alg.input, 'r') as f:
            data = alg._read(f)
            answer = alg.solve(data)

        with open(alg.output, 'w') as f:
            alg._write(f, answer)

        return answer

    @staticmethod
    def test(name):
        alg = Solution.algorithm(name)
        alg.test()


class SimpleWriteSolution(Solution):

    def _write(self, f, answer):
        f.write(str(answer))


class ArrayWriteSolution(Solution):

    def _write(self, f, answer):
        f.write(' '.join([str(i) for i in answer]))
