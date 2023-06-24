from time import sleep

import cv2
import numpy as np

from sort import sort
from Console import Console
from utils import index_of_number


class CharCamera:
    def __init__(self, dic_string) -> None:
        self.dic_string, self.dic_value = sort(dic_string)
        self.cam = cv2.VideoCapture(0)
        self.height = 30
        ret, temp = self.cam.read()
        self.width = int(temp.shape[1] / (temp.shape[0] / self.height))

        def quantize(x: int) -> int:
            return index_of_number(self.dic_value * 255, x)

        self.quantize_v = np.frompyfunc(quantize, 1, 1)

        def get_dic_char(index):
            return self.dic_string[index]

        self.get_dic_char_v = np.frompyfunc(get_dic_char, 1, 1)
        self.console = Console()
        self.console.clear()

    def main_loop(self):
        self.console.reset_pos()

        ret, frame = self.cam.read()

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 缩小图片
        img_resized = cv2.resize(img_gray, (self.width, self.height))

        # 翻转一下
        img_resized = cv2.flip(img_resized, 1)

        # 量化像素值
        img_quantized = self.quantize_v(img_resized).astype(np.uint8)

        # 生成二维数组
        arr = self.get_dic_char_v(img_quantized)

        self.console.print_2D_array(arr)

    def start(self, frame_rate):
        while True:
            sleep(1 / frame_rate)
            self.main_loop()
            if cv2.waitKey(1) == ord("q"):
                break

        self.cam.release()
        cv2.destroyAllWindows()
