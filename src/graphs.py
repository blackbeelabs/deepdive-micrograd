import math


class Node:
    def __init__(self, data, children=(), label="", op=""):
        self.data = data
        self.label = label
        self._prev = set(children)
        self._op = op
        self._grad = 0.0

    def __repr__(self):
        return f"Node(data={self.data})"

    def __add__(self, other):
        # Instantiate a Value object when passing in a primitive datatype
        other = other if isinstance(other, Node) else Node(other)
        out = Node(self.data + other.data, children=(self, other), op="+")
        return out

    def __mul__(self, other):
        # Instantiate a Value object when passing in a primitive datatype
        other = other if isinstance(other, Node) else Node(other)
        out = Node(self.data * other.data, children=(self, other), op="*")
        return out

    def exp(self):
        # Instantiate a Value object when passing in a primitive datatype
        out = Node(math.exp(self.data), children=(self,), op="exp")
        return out

    def __pow__(self, other):
        # Instantiate a Value object when passing in a primitive datatype
        other = other if isinstance(other, Node) else Node(other)
        out = Node(self.data**other.data, children=(self,), op="**")
        return out

    def __radd__(self, other):
        """
        Allow __add__ to work with the expression 2 + Value(1) with a primitive datatype first
        """
        return self + other

    def __sub__(self, other):  # self - other
        return self + (-other)

    def __rsub__(self, other):  # other - self
        return other + (-self)

    def __rmul__(self, other):
        """
        Allow __mul__ to work with the expression 2 * Value(1) with a primitive datatype first
        """
        return self * other

    def __truediv__(self, other):  # self / other
        return self * other**-1

    def __rtruediv__(self, other):  # other / self
        return other * self**-1

    def __neg__(self):  # -self
        return self * -1
