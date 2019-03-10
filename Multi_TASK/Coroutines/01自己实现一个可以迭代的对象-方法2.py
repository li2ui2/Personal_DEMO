from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


def main():
    classmate = Classmate()
    classmate.add("张灿")
    classmate.add("里斯")
    classmate.add("王五")
    # print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))
    # classmate_iterator = iter(classmate)
    # print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))
    for name in classmate:
        print(name)


if __name__ == "__main__":
    main()
