from PlayLA.Vector import Vector

if __name__ == '__main__':
    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print("{}|{}".format(vec[0], vec[1]))

    vec1 = Vector([2, 5])
    print(vec + vec1)
    print(vec - vec1)
    print(vec * 3)
    print(3 * vec)
    print(+vec)
    print(-vec)