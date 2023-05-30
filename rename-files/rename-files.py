import os
import argparse

path = "/Users/trim/www/dispatchZZ/images"
ext = ".jpg"


def rename(path, ext):
    count = 1
    for f in os.listdir(path):
        if f.lower().endswith(ext):
            fp = path + '/' + f
            nfp = path + "/" + "{:04d}".format(count) + ext
            os.rename(fp, nfp)
            count += 1


def prepare_args():
    parser = argparse.ArgumentParser(description='Rename all files in a directory numerically from 0001-9999')
    parser.add_argument('-p', '--path', help='Full path to the directory containing the files', required=True)
    parser.add_argument('-e', '--ext', help='File extension of files to rename', required=True)
    return parser.parse_args()


def main():
    args = prepare_args()
    if not os.path.exists(args.path):
        raise Exception('Invalid directory provided')
    else:
        args.ext = args.ext if args.ext[0] == '.' else '.'+args.ext
        rename(args.path, args.ext)


if __name__ == "__main__":
    main()
