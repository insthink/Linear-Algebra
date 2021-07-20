from ._global import EPSILON
import math


class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """
        返回dim维度的零向量
        :param dim:
        :return:
        """
        return cls([0] * dim)

    def norm(self):
        """
        向量取模
        :return:
        """
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        """
        归一化为单位向量
        :return:
        """
        if self.norm() < EPSILON:
            raise ZeroDivisionError("norm is zero, cannot normalize")
        return 1 / self.norm() * Vector(self._values)

    def __add__(self, other):
        assert len(self) == len(other), "Error in adding. Length of vector must be the same"
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), "Error in subtracting. Length of vector must be the same"
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """
        左乘： vector * k
        :param k:
        :return:
        """
        return Vector([k * e for e in self._values])

    def __rmul__(self, k):
        """
        右乘： k * vector
        :param k:
        :return:
        """
        return Vector([k * e for e in self._values])

    def __truediv__(self, k):
        """
        truediv是数量除法，区别于地板除, vector / k
        :param k:
        :return:
        """
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__()

    def __getitem__(self, index):
        """
        取出向量的中的第index个元素
        :param index:
        :return:
        """
        return self._values[index]

    def __len__(self):
        """
        返回向量的长度
        :return:
        """
        return len(self._values)

    def __repr__(self):
        """
        供系统调用：对象展示成什么
        :return:
        """
        return "Vector({})".format(self._values)

    def __str__(self):
        """
        供用户调用：print
        :return:
        """
        return "({})".format(", ".join(str(e) for e in self._values))
