class Vector:
    def __init__(self, value):
        if isinstance(value, list) and all([isinstance(v, float) or isinstance(v, int) for v in value]):
            self.values = value
        elif isinstance(value, int):
            self.values = [float(i) for i in range(value)]
        elif isinstance(value, range):
            self.values = [float(i) for i in value]
        elif isinstance(value, tuple) and len(value) == 2 and value[1] > value[0]:
            self.values = [float(i) for i in range(*value)]
        try:
            self.size = len(self.values)
        except AttributeError:
            quit("invalid Inputs")

    def __add__(self, other):
        if isinstance(other, list) and all([isinstance(v, float) or isinstance(v, int) for v in other]):
            other = Vector(other)
        if not isinstance(other, Vector):
            quit("can't add. op1 and op2 must be Vector or list of float.")
        if isinstance(other, Vector) and other.size != self.size:
            quit("can't add. op1 and op2 must be same size.")

        values = [round(v1 + v2, 10) for v1, v2 in zip(self.values, other.values)]
        return Vector(values)

    def __radd__(self, other):
        return Vector.__add__(self, other)

    def __sub__(self, other):
        if isinstance(other, list) and all([isinstance(v, float) or isinstance(v, int) for v in other]):
            other = Vector(other)
        if not isinstance(other, Vector):
            quit("can't sub. op1 and op2 must be Vector or list of float.")
        if isinstance(other, Vector) and other.size != self.size:
            quit("can't sub. op1 and op2 must be same size.")

        values = [round(v1 - v2, 10) for v1, v2 in zip(self.values, other.values)]
        return Vector(values)

    def __rsub__(self, other):
        if isinstance(other, list) and all([isinstance(v, float) or isinstance(v, int) for v in other]):
            other = Vector(other)
        if not isinstance(other, Vector):
            quit("can't sub. op1 and op2 must be Vector or list of float.")
        if isinstance(other, Vector) and other.size != self.size:
            quit("can't sub. op1 and op2 must be same size.")
        return Vector.__sub__(other, self)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = [other]
        if isinstance(other, list) and all([isinstance(v, float) or isinstance(v, int) for v in other]):
            other = Vector(other)
        if not isinstance(other, Vector):
            quit("can't divide. op1 and op2 must be Scala.")
        if self.size != 1 or other.size != 1:
            quit("can't divide. op1 and op2 must be Scala.")
        value = [self.values[0] / other.values[0]]
        return Vector(value)

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = [other]
        if isinstance(other, list) and all([isinstance(v, float) or isinstance(v, int) for v in other]):
            other = Vector(other)
        if not isinstance(other, Vector):
            quit("can't divide. op1 and op2 must be Scala.")
        if self.size != 1 or other.size != 1:
            quit("can't divide. op1 and op2 must be Scala.")
        return Vector.__truediv__(other, self)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = [other]
        if isinstance(other, list) and all([isinstance(v, float) or isinstance(v, int) for v in other]):
            other = Vector(other)
        if not isinstance(other, Vector):
            quit("can.t mul. op1 and op2 must be Vector, float or int.")

        if other.size != self.size and other.size != 1:
            quit("can't mul. op1 and op2 must be same size. Or any op must be Scala")
        if other.size != 1:
            values = [sum([v1 * v2 for v1, v2 in zip(self.values, other.values)])]
        else:
            values = [v1 * other.values[0] for v1 in self.values]
        return Vector(values)

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = [other]
        if isinstance(other, list) and all([isinstance(v, float) or isinstance(v, int) for v in other]):
            other = Vector(other)
        if not isinstance(other, Vector):
            quit("can.t mul. op1 and op2 must be Vector, float or int.")
        return Vector.__mul__(self, other)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)
