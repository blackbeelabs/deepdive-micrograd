class Value:
    def __init__(self, data, children=(), label="", op=""):
        self.data = data
        self.label = label
        self._prev = set(children)
        self._op = op
        self._grad = 0.0

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data, children=(self, other), op="+")
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, children=(self, other), op="*")
        return out
