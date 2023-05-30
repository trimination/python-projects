# Python Projects

Here is a collection of short python scripts I've written either for the sake of it or necessity:

- [heic-converter](#heic-converter)
- [img-to-ico](#img-to-ico)
- [merge-pdf](#merge-pdf)
- [pdf-page-extract](#pdf-page-extract)
- [resize-images](#resize-images)
- [temperature-converter](#temperature-converter)
- [text-to-image](#text-to-image)

## heic-converter

_iPhone images save as HEIC and although you can export them to another format, it's a slow process when you have a
whole
directory full of them. So, `heic-converter.py` will convert every image in the directory to either JPG or PNG depending
on the parameters you pass it._

**Usage:**

```
usage: heic-converter.py [-h] -p PATH -e {jpg,png,jpeg}

Convert HEIC to JPG or PNG images

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Full path to the directory containing the files
  -e {jpg,png,jpeg}, --ext {jpg,png,jpeg}
                        Target filetype

```

> **Example**:
> <br/>
> `heic-converter.py -p '/absolute/path/to/directory' -e jpg`
>- Will convert every HEIC or HEIF image in the path to JPG.

---

## img-to-ico

_Occasionally I require an ICO file, so here's a python script to make one from either a JPEG or PNG image._

**Usage:**

```
usage: img-to-ico.py [-h] -f FILE [-n NAME]

Convert an image to an ICO file

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The file to convert
  -n NAME, --name NAME  The name to use when saving the file
```

> **Example**:
> <br/>
> `img-to-ico.py -f '/absolute/path/to/file'`
> - Will convert the image at the path to an ICO file.

**Accepted Image formats:** _JPG, JPEG, PNG_

---

## merge-pdf

_Merge all PDF files in a given directory into a single PDF file_

**Usage:**

```
usage: merge-pdf.py [-h] -p PATH

Merge multiple PDFs into one PDF file in a given directory

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Full path to the directory containing the PDF files

```

> **Example**:
> <br/>
> `merge-pdf.py -p '/absolute/path/to/directory'`
> - Merge all PDF files in given directory into a single PDF file.

---

## pdf-page-extract

_Extract a range of pages from a PDF file_

**Usage:**

```
usage: pdf-page-extract.py [-h] -f FILENAME -s START -e END

Extract pages from PDF

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Full PDF path
  -s START, --start START
                        Start Page
  -e END, --end END     End Page
```

> **Example**:
> <br/>
> `pdf-page-extract.py -f '/absolute/path/to/file' -s 3 -e 10`
> - Extract pages 3 through 10 to a new PDF file.
>
>`pdf-page-extract.py -f '/absolute/path/to/file' -s 2 -e 2`
> - Extract page 2 to a new PDF file.

---

## resize-images

**Usage:**

```
usage: resize-images.py [-h] -p PATH [-e {png,jpeg,jpg}] (-m {h,d} | -d DIMENSIONS)

Resize all the images of a given filetype in a given path. This is not a lossless process for JPEG images.

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  The absolute filepath to the image directory
  -e {png,jpeg,jpg}, --ext {png,jpeg,jpg}
                        The image extension to search for
  -m {h,d}, --mode {h,d}
                        The resize action you want. h: reduce the dimensions by 50%. d: increase the dimensions by 50%. Use this option OR -d, but not both.
  -d DIMENSIONS, --dimensions DIMENSIONS
                        The dimensions you want the image to be. You may provide: widthxheight (e.g. 1920x1080), width or height (e.g. 100 or 100). Providing one
                        value will reduce the other value in aspect. Use this option OR -t, but not both.
```

> **Example**:
> <br/>
> `resize-images.py -p '/absolute/path/to/directory' -m h -e jpg`
> - Resize all JPG images in directory to 50% width, 50% height.
>
>`resize-images.py -p '/absolute/path/to/directory' -m d -e jpg`
> - Resize all JPG images in directory to 200% width, 200% height.
>
>`resize-images.py -p '/absolute/path/to/directory' -d 1920x1080 -e png `
> - Resize all PNG images in the directory to 1920x1080
>
>`resize-images.py -p '/absolute/path/to/directory' -d 500 -e png`
> - Resize all PNG images in the directory with auto_scale, the largest dimension of an image will be set to 500 (the
    value of -d) and the other dimension will be scaled up or down proportionally.

## temperature-converter

_These convenience scripts convert between Celsius (c2f) and Fahrenheit (f2c)._

**Usage:**

```
**************************************************

c2f Celsius to Fahrenheit Conversion
Usage: c2f <temperature>

**************************************************
```

```
**************************************************

f2c Fahrenheit to Celsius Conversion
Usage: f2c <temperature>

**************************************************
```

I personally run these scripts from a dedicated `scripts` directory on my system that is
included in the system PATH, so a shebang is included at the top to point to python. You can also
just run them like any other python script:

`python c2f.py 0` = 32

`python f2c.py 32` = 0

---

## text-to-image

_Takes a string of text and draws it on an image_

text-to-image uses Google's `Roboto` font which is subject to the
[Apache License, Version 2.0, January 2004](http://www.apache.org/licenses/). A copy of this license is included within
the `text-to-image` directory. 

**Usage:**

```
usage: text-to-image.py [-h] -t TEXT --save | --no-save [-s S] [-c COLOR] -f FILENAME -e {.png,.jpg}

Draw a text string onto an image

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  The text to draw, use quotes
  --save, --no-save     Whether to save or just show the image
  -s S                  The text size
  -c COLOR, --color COLOR
                        The hexadecimal color of the text
  -f FILENAME, --filename FILENAME
                        The filename used to save the image
  -e {.png,.jpg}, --ext {.png,.jpg}
                        The image file extension (png or jpg)
```
> **Example**:
> <br/>
> `text-to-image.py  -t "Hello, World\!" --save -s 100 -f "example" -e .png -c "#ff0000"`
> - Will produce the example.png image within the `text-to-image` directory.

### Author
 -Trimination.

### License 
[Apache License, Version 2.0, January 2004](http://www.apache.org/licenses/)