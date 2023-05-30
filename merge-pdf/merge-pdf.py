import argparse
import os
from PyPDF2 import PdfMerger
from datetime import datetime


def find_pdfs_in_path(path):
    list_dir = os.listdir(path)
    list_dir = [f.lower() for f in list_dir]
    s = sorted(list_dir)
    filtered = []
    # find PDF files and add them to array
    for item in s:
        if item.endswith('.pdf'):
            filtered.append(item)
    if not filtered:
        print("No items found")
        exit()
    return filtered


def merge_pdfs(pdfs, path):
    today = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    merger = PdfMerger(False)
    for pdf in pdfs:
        merger.append(path + '/' + pdf, import_outline=False)
    merger.write(path + "/" + today + "_result.pdf")
    merger.close()


def prepare_args():
    parser = argparse.ArgumentParser(description='Merge multiple PDFs into one PDF file in a given directory')
    parser.add_argument('-p', '--path', help='Full path to the directory containing the PDF files', required=True)
    return parser.parse_args()


def main():
    args = prepare_args()
    path = args.path
    pdfs = find_pdfs_in_path(path)
    merge_pdfs(pdfs, path)


if __name__ == "__main__":
    main()
