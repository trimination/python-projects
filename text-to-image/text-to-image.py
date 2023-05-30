from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import argparse


def text_to_image(args):
    text = args.text
    text_size = args.s if args.s is not None else 20
    color = args.color if args.color is not None else "#FFFFFF"
    hex_color = color.lstrip('#')
    save = args.save
    ext = args.ext
    filename = args.filename
    font = ImageFont.truetype("./Roboto-Regular.ttf", int(text_size))
    r, g, b = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    x0, y0, x1, y1 = font.getbbox(text)
    w = x1 + 2
    h = y1 + 5
    img = Image.new('RGBA', (w, h))
    d = ImageDraw.Draw(img)
    d.fontmode = "L"
    d.font = font
    d.text((1, 1), text, fill=(r, g, b))
    if save:
        img.save('./' + filename + ext)
    else:
        img.show()


def prepare_args():
    parser = argparse.ArgumentParser(description="Draw a text string onto an image")
    parser.add_argument('-t', '--text', help='The text to draw, use quotes', required=True)
    parser.add_argument('--save', help="Whether to save or just show the image", required=True,
                        action=argparse.BooleanOptionalAction)
    parser.add_argument('-s', help='The text size', required=False)
    parser.add_argument('-c', '--color', help='The hexadecimal color of the text', required=False)
    parser.add_argument('-f', '--filename', help='The filename used to save the image', required=True)
    parser.add_argument('-e', '--ext', help='The image file extension (png or jpg)', required=True,
                        choices=['.png', '.jpg'])
    return parser.parse_args()


def main():
    args = prepare_args()
    text_to_image(args)


if __name__ == "__main__":
    main()
