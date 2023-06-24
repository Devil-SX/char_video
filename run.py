"""
cli接口
"""
import argparse
from camera import CharCamera

# Get FilePath
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="./dic/default.txt", help="file path")
parser.add_argument("--frame", default=10, type=int, help="max frame rate")
args = parser.parse_args()
file_path = args.file
frame_rate = args.frame


# Load DicFile
with open(file_path, "r") as f:
    dic_string = f.read()


# Start Camera
camera = CharCamera(dic_string)
camera.start(frame_rate)
