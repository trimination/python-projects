from PIL import Image
import os
import argparse


def calc_dimensions(t, w, h):
    ratio = t / w if w > h else t / h
    return w * ratio, h * ratio


def half_size(w, h):
    return w / 2, h / 2


def double_size(w, h):
    return w * 2, h * 2


def parse_dimensions(d):
    s_split = d.split('x')
    if len(s_split) == 2:
        return s_split[0], s_split[1]
    else:
        if len(s_split) == 1:
            if not s_split[0].isdigit():
                raise Exception('Invalid dimension value was provided.')
            else:
                return s_split[0], None


def find_and_resize_images(path, ext, mode, *argv):
    print('find and resize images in: ' + path + ' with extension: ' + ext + ' using mode: ' + mode)
    for f in os.listdir(path):
        if f.lower().endswith(ext):
            fp = path + '/' + f
            filename_no_ext = os.path.splitext(f)[0]
            nfp = path + "/" + filename_no_ext.replace(" ", "_") + '_' + mode + ext
            im = Image.open(fp)
            w, h = im.size
            # resize, auto_scale_width, auto_scale_height, fixed
            if mode == 'resize':
                if argv[0] == 'h':
                    nw, nh = half_size(w, h)
                elif argv[0] == 'd':
                    nw, nh = double_size(w, h)
            if mode == 'fixed':
                nw, nh = argv[0], argv[1]
            if mode == 'auto_scale':
                nw, nh = calc_dimensions(argv[0], w, h)

            im = im.resize((int(nw), int(nh)), Image.LANCZOS)
            if ext.lower() == 'jpg' or ext.lower() == 'jpeg':
                im.save(nfp, optimize=True, quality=95, subsampling=0)
            else:
                im.save(nfp, optimize=True, quality=95)


def prepare_args():
    parser = argparse.ArgumentParser(
        description='Resize all the images of a given filetype in a given path. ' +
                    'This is not a lossless process for JPEG images.')
    parser.add_argument('-p', '--path', help='The absolute filepath to the image directory', required=True)
    parser.add_argument('-e', '--ext', help='The image extension to search for', choices=['png', 'jpeg', 'jpg'])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--mode',
                       help='The resize action you want. h: reduce the dimensions by 50%%. d: ' +
                            'increase the dimensions by 50%%. Use this option OR -d, but not both.',
                       choices=['h', 'd'])
    group.add_argument('-d', '--dimensions',
                       help='The dimensions you want the image to be. You may provide: widthxheight (e.g. 1920x1080),' +
                            ' width or height (e.g. 100 or 100). Providing one value will reduce the other value in aspect. ' +
                            'Use this option OR -t, but not both.')

    return parser.parse_args()


def main():
    args = prepare_args()
    path = args.path
    ext = args.ext if args.ext[0] == '.' else '.' + args.ext
    mode = 'resize' if args.mode is not None else 'specific'
    dx, dy = None, None
    if mode == 'specific':
        dx, dy = parse_dimensions(args.dimensions)
        if not dx.isdigit():
            raise Exception('Invalid dimension value was provided.')
        if dy is None:
            mode = 'auto_scale'
        elif dy.isdigit():
            mode = 'fixed'
        else:
            raise Exception('Invalid dimension value was provided.')

    if mode == 'resize':
        find_and_resize_images(path, ext, mode, args.mode)
    elif mode == 'fixed':
        find_and_resize_images(path, ext, mode, int(dx), int(dy))
    else:  # auto_scale
        find_and_resize_images(path, ext, mode, int(dx))


if __name__ == "__main__":
    main()
