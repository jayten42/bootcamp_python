from vector import Vector
if __name__ == '__main__':
    v1 = Vector([0.0, 1.0])
    v2 = Vector(2)
    v3 = Vector((0, 2))
    v4 = Vector(range(2))
    print(v1.__dict__)
    print(v2.__dict__)
    print(v3.__dict__)
    print(v4.__dict__)
    print(([1.1, 1.1] - v1).__dict__)
    print((v1 - [1.1, 1.1]).__dict__)
    v5 = Vector([1])
    print((3 / v5).__dict__)
    print((v1 * 5).__dict__)
    print((5 * v1).__dict__)
    print((Vector([1, 2, 3]) * Vector([3, 2, 1])).__dict__)
    print(v1)