"""
ANSI standard console
"""


class Console:
    def __init__(self) -> None:
        pass

    def clear(self):
        print("\x1b[2J")

    # def up(self, n: int):
    #     while n > 9:
    #         print("\x1b[9A")
    #         n = n - 9
    #     print(f"\x1b[{n}A")

    # def left(self, n: int):
    #     while n > 9:
    #         print("\x1b[9C")
    #         n = n - 9
    #     print(f"\x1b[{n}C")

    def save_pos(self):
        print("\x1b[s")

    def recover_pos(self):
        print("\x1b[r")

    def reset_pos(self):
        print("\x1b[1;1H")

    def set_color(self, r, g, b):
        print(f"\x1b[38;2;{r};{g};{b}m")

    def print_2D_array(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(arr[i][j], end=" ")
            print()
