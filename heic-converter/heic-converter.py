import os.path

from PIL import Image
from pillow_heif import register_heif_opener
from os import listdir
from os.path import isfile, join
import argparse

register_heif_opener()


def convert(files, filetype="png"):
    ext = ""
    f = ""
    if len(files) == 0:
        print("No files found at path")
        return

    if filetype.lower() == "png":
        ext = "png"
        f = "png"
    elif filetype.lower() == "jpg" or filetype.lower() == "jpeg":
        ext = "jpg"
        f = "jpeg"
    else:
        print("Unknown format provided")
        quit(0)

    i = 1
    total = len(files) - 1
    for file in files:
        if not file.endswith(('.heic', '.heif', '.HEIC', '.HEIF')):
            print('[{i}] Skipping: '.format(i=i) + file + " is not a HEIC or HEIF image")
            i += 1
            continue
        print("[{i}] Processing image {i} of {total}\n{file}".format(i=i, total=total, file=file))
        im = Image.open(file)
        tmp_path = file[:-4]
        im.save(tmp_path + ext, format=f, quality=100, subsampling=0)
        i += 1


def init(path, ext):
    filepaths = []
    for f in listdir(path):
        if isfile(join(path, f)):
            filepaths.append(join(path, f))
    convert(filepaths, ext)


def prepare_args():
    parser = argparse.ArgumentParser(description='Convert HEIC to JPG or PNG images')
    parser.add_argument('-p', '--path', help='Full path to the directory containing the files', required=True)
    parser.add_argument('-e', '--ext', help='Target filetype', required=True, choices=['jpg', 'png', 'jpeg'])
    return parser.parse_args()


def main():
    args = prepare_args()
    if not os.path.exists(args.path):
        raise Exception('Invalid directory provided')
    else:
        init(args.path, args.ext)


if __name__ == '__main__':
    main()
