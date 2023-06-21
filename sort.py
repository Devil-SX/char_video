from PIL import Image, ImageFont, ImageDraw
import numpy as np

font_file = "/home/shuchengdu/.local/share/fonts/sarasa-term-sc-nerd-regular.ttf"


def pixel_rate(char: str) -> float:
    """
    返回一个字符串的像素占比
    """
    # 字体大小和字符
    font_size = 30
    img_size = (int(font_size * 1.5), int(font_size * 1.5))
    center = (int(font_size * 1.5 / 2), int(font_size * 1.5 / 2))

    # 创建字体对象
    font = ImageFont.truetype(font_file, font_size)

    img = Image.new("1", img_size, 1)
    draw = ImageDraw.Draw(img)
    draw.text(center, char, font=font, fill=0, anchor="mm")

    # 计算图片的平均数
    pixels = 1 - np.array(img).astype(dtype=int)
    avg = np.mean(pixels)

    return avg


def sort(string: str) -> tuple[str, np.array]:
    """
    读取一个字符串，按照像素占比的大小排序返回
    value : 归一化数组
    """
    list_sorted = sorted(string, key=pixel_rate)
    value = np.array(np.frompyfunc(pixel_rate, 1, 1)(list_sorted))
    value = value / np.max(value)
    string_sorted = "".join(list_sorted)

    return string_sorted, value


if __name__ == "__main__":
    string = "我爱你中国"
    string_sorted, value = sort(string)
    print(string_sorted)
    print(value)
