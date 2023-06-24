import argparse
import cv2
import numpy as np
import os
from sort import sort
from time import sleep


# Get FilePath
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="./dic/default.txt", help="file path")
args = parser.parse_args()
file_path = args.file


# Load DicFile
with open(file_path, "r") as f:
    dic_string = f.read()

dic_string, dic_value = sort(dic_string)
print(dic_string)


def print2DArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()


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


def quantize(a: int) -> int:
    return index_of_number(dic_value * 255, a)


quantize_ = np.frompyfunc(quantize, 1, 1)


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 缩小图片
    width = 50
    height = int(img_gray.shape[0] / (img_gray.shape[1] / width))
    img_resized = cv2.resize(img_gray, (width, height))

    # 翻转一下
    img_resized = cv2.flip(img_resized, 1)

    # 量化像素值
    img_quantized = quantize_(img_resized).astype(np.uint8)

    # 生成二维数组
    arr = np.zeros((height, width), dtype=str)
    for i in range(height):
        for j in range(width):
            arr[i, j] = dic_string[img_quantized[i, j]]  # 在此处使用灰度图的值作为索引取对应位置的元素

    print2DArray(arr)
    sleep(0.1)

    if cv2.waitKey(1) == ord("q"):
        break

    os.system("clear")

cam.release()
cv2.destroyAllWindows()
