from PIL import Image
import argparse


def img_to_ico(source_file, target_file, sizes=None):
    if sizes is None:
        sizes = [16, 32, 48]
    icon_sizes = [(x, x) for x in sizes]
    Image.open(source_file).save(target_file, icon_sizes=icon_sizes)


def prepare_args():
    parser = argparse.ArgumentParser(description='Convert an image to an ICO file')
    parser.add_argument('-f', '--file', help='The file to convert', required=True)
    parser.add_argument('-n', '--name', help='The name to use when saving the file', required=False)
    return parser.parse_args()


def main():
    args = prepare_args()
    if args.file[-3:].lower() in ['jpg', 'jpeg', 'png']:
        target = args.name if args.name is not None else args.file[:-4]
        target = target if target.endswith('.ico') else target + '.ico'
        img_to_ico(args.file, target)


if __name__ == "__main__":
    main()
