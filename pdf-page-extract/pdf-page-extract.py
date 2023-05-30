import os
import PyPDF2
import argparse


def extract(filename, s, e):
    base_name = os.path.basename(filename)
    dir_name = os.path.dirname(filename)
    pdf_reader = PyPDF2.PdfReader(filename)
    for page in range(len(pdf_reader.pages) - 1):
        pdf_writer = PyPDF2.PdfWriter()
        start = s - 1
        end = e
        try:
            while start < end:
                pdf_writer.add_page(pdf_reader.pages[start])
                start += 1
            output_filename = dir_name + '/' + os.path.splitext(base_name)[0] + '_pages_' + str(s) + '-' + str(
                e) + '.pdf'
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
        except IndexError:
            print('Invalid page number: ' + str(start) + ' in PDF file: ' + base_name + ' (' + str(len(
                pdf_reader.pages)) + ' pages)')
            exit(-1)


def prepare_args():
    parser = argparse.ArgumentParser(description='Extract pages from PDF')
    parser.add_argument('-f', '--filename', help='Full PDF path', required=True)
    parser.add_argument('-s', '--start', help='Start Page', type=int, required=True)
    parser.add_argument('-e', '--end', help='End Page', type=int, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = prepare_args()
    extract(args.filename, args.start, args.end)
