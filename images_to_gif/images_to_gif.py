import getopt
import glob
import sys
from os import path
from PIL import Image

# filepaths
fp_in = "/path/to/image_*.png"
fp_out = "/path/to/image.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
def generate_gif(indir, outfile, filetype, duration, loop):
    fp_in = indir + '/*.' + filetype
    fp_out = outfile
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
    img.save(fp=fp_out, format='GIF', append_images=imgs, save_all=True, duration=duration, loop=loop)

def print_usage():
    print('USAGE: img2gif')
    print('-------------------')
    print('test.py -i <inputdir> -o <outputfile> -t <filetypes> -d <duration ms> -l <loop 0 or 1>')
    print('test.py -i /imgdir -o /img/dir -t png -d 200 -l 1')
    print('-------------------')

def main(argv):

    if not len(argv) > 6 and not len(argv) == 2:
        print('argv len: ', len(argv))
        print_usage()
        exit()

    inputdir = ''
    outputfile = ''
    filetype = ''
    duration = 0
    loop = 0

    try:
        opts, args = getopt.getopt(argv, "hi:o:t:d:l:", ["idir=", "ofile=", "filetype=", "duration=", "loop="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit()
        elif opt in ("-i", "--idir"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-t", "--filetype"):
            filetype = arg
        elif opt in ("-d", "--duration"):
            duration = int(arg)
        elif opt in ("-l", "--loop"):
            loop = int(arg)

    print('Input file is ', inputdir)
    print('Output file is ', outputfile)
    print('Filetype is ', filetype)
    print('Duration is ', duration)
    print('Loop is ', loop)

    if not path.exists(inputdir):
        print(inputdir + " does not exist")
        exit(2)

    generate_gif(inputdir, outputfile, filetype, duration, loop)

if __name__ == "__main__":
    main(sys.argv[1:])
