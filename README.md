<h1 align="center">
Char Camera 字符摄像头
</h1>

<p align="center">
让摄像头输出在你的控制台！
</p>

用自定义的字符在控制台绘制酷酷的字符视频！

<img src="./byx_dsc.png"  width="500px">

# Features

使用 [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) 完成屏幕光标移动

用移动光标而不是清屏的方式刷新以避免闪屏

    ANSI escape code 还支持颜色显示，还能用控制台播放视频，但这样做失去了绘制字符的意义

# Get Started

环境 `Ubuntu 22.04`

(1) 安装 `opencv` 和 `numpy` 库

```shell
pip install -r ./requirements.txt
```

(2) 设置自己的字符字典文件

比如默认的字符文件 [default.txt](./dic/default.txt) 内容是：

```
一二三四五六七八九杜书丞爱上了白映溪
```

那么就会用这18个字作为基本元素组成字符画

*由于中英文字宽不一样，最好使用全英文/全中文字符*

将自己的字符文件保存，后续要作为参数路径输入

(3) 修改 `sort.py` 文件中 `font_file` 变量的路径保持和控制台字体路径一致。该字体文件将用来评估字符打印后的像素密度

(4) 运行程序

```shell
python ./main.py -f [your_dic_file_path]
```

- `-f` 字典文件路径， 缺省则使用`/dic/default.txt`

