import numpy as np


def index_of_number(arr, num) -> int:
    """
    在一个正序排列的数组中查找一个数的位置
    :param arr: 正序排列的数组
    :param num: 要查找的数
    :return: num在数组中的位置
    """
    for i in range(len(arr)):
        if num <= arr[i]:
            return i
    return len(arr)
