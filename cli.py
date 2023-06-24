"""
cli接口
"""
import argparse
from camera import CharCamera

# Get FilePath
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", default="./dic/default.txt", help="file path")
args = parser.parse_args()
file_path = args.file


# Load DicFile
with open(file_path, "r") as f:
    dic_string = f.read()


# Start Camera
camera = CharCamera(dic_string)
camera.start()
