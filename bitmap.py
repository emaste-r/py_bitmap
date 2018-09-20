# coding=utf-8
"""
2018年09月20日 星期四
by ouyang
"""


class Bitmap(object):
    def __init__(self, number_count, init_array=True):
        self.size = number_count / 32 + 1
        self.number_count = number_count

        if init_array:
            self.array = [0] * self.size

        print "__init__: size=%s" % self.size

        a = number_count / (2 ** 3)  # byte 字节
        b = float(a) / (2 ** 10)  # Kb
        c = float(b) / (2 ** 10)  # Mb
        d = float(c) / (2 ** 10)  # Gb
        print "__init__: memory size=%s Byte, %.3fKb, %.3fMb, %.3fGb " % (a, b, c, d)

    @staticmethod
    def find_element_pos(number):
        return number / 32

    @staticmethod
    def find_bit_index(number):
        return number % 32

    def set(self, number):
        """
        99 => pos = 3, index = 3
        element = self.array[3], suppose now element is 8
        index = 3
        we need the 3th bit which in the 3th element set to 1...

        1、 element = 8 = 1000
        2、 1 << index = 1 << 3 = 0100
        3、 element | (1 << index)
            =
            1000 | 0100
            =
            1100

        :param number:
        :return:
        """
        print "set: %s" % number
        pos = self.find_element_pos(number)
        index = self.find_bit_index(number)

        self.array[pos] |= (1 << index)

    def clear(self, number):
        """
        99 => pos = 3, index = 3
        element = self.array[3], suppose now element is 5
        index = 3
        we need the 3th bit which in the 3th element set to 0...

        1、 element = 5 = 0101
        2、 ~(1 << index) = ~(1 << 3) = ~0100 = 1011
        3、 element & ~(1 << index)
            =
            0101 & 1011
            =
            0001

        :param number:
        :return:
        """
        print "clear: %s" % number
        pos = self.find_element_pos(number)
        index = self.find_bit_index(number)

        self.array[pos] &= (~(1 << index))

    def is_set(self, number):
        pos = self.find_element_pos(number)
        index = self.find_bit_index(number)

        if self.array[pos] & (1 << index) > 0:
            return True

        return False

    def print_bitmap(self):
        res = []
        for i in range(self.number_count):
            if self.is_set(i):
                res.append(i)
        print "print bitmap:", res


if __name__ == '__main__':

    bm = Bitmap(100)

    for i in [1, 3, 4, 5, 6, 78, 9, 90]:
        bm.set(i)

    bm.print_bitmap()

    bm.clear(5)

    bm.print_bitmap()

    big_bm = Bitmap(10 ** 9, init_array=False)
