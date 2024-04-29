from value import Value


def main(a, b, c):
    # Implement the graph
    node_a = Value(a)
    node_b = Value(b)
    node_c = Value(c)
    # To maintain purity, only have 1 function per line
    node_e = node_a * node_b
    node_d = node_e + node_c
    print(node_d)
    print(node_d._prev)
    print(node_d._op)
    print(node_e)
    print(node_e._prev)
    print(node_e._op)


if __name__ == "__main__":
    main(2, -3, 10)
