#!/usr/bin/python python 3.13
"""
name: weihnachtsaufgabe
author: Sebastian Fath
"""

# imports for external libraries
import sys
import argparse
import io

from PIL import Image
import pytesseract
import pdf2image
from pypdf import PdfWriter


# main code for ocr of pdf-file
def main(inputfile, outputfile, outputtype, lang, resolution):
    # main code here
    print(
        f"INFO | OCR-ing {inputfile} to {outputfile} of type {outputtype} using language-argument {lang}"
    )

    # split input pdf into PIL Images using pdf2image
    # note this should be rewritten at some point to decrease memory-usage. For inspiration see the examples on pdf2image PyPI page
    images = pdf2image.convert_from_path(inputfile, dpi=resolution)
    print(f"INFO | found and converted {len(images)} pages!")

    # run ocr over images
    match outputtype:
        case "txt":
            with open(outputfile, mode="w", buffering=False) as output:
                for index, image in enumerate(images):
                    print(f"INFO | processing page {index + 1} out of {len(images)}")
                    output.write(pytesseract.image_to_string(image, lang=lang))

        case "pdf":
            # PDF creation (in Python?) is weird. For a decent implementation use pypdf to stitch together the multipage pdf instead of byte-wise file.write() as suggested by the pytesseract documentation
            merger = PdfWriter()
            for index, image in enumerate(images):
                print(f"INFO | processing page {index + 1} out of {len(images)}")
                # While pytesseract does result in bytes, pypdf requires an IoStream. Conversion is achieved using io.BytesIO()
                page = io.BytesIO()
                page.write(pytesseract.image_to_pdf_or_hocr(image, extension="pdf", lang=lang))
                merger.append(page)
            with open(outputfile, mode="w+b", buffering=False) as output:
                merger.write(output)
            merger.close()

        case "hocr":
            with open(outputfile, mode="w+b", buffering=False) as output:
                for index, image in enumerate(images):
                    print(f"INFO | processing page {index + 1} out of {len(images)}")
                    output.write(
                        pytesseract.image_to_pdf_or_hocr(
                            image, extension="hocr", lang=lang
                        )
                    )

        case "alto":
            with open(outputfile, mode="w", buffering=False) as output:
                for index, image in enumerate(images):
                    print(f"INFO | processing page {index + 1} out of {len(images)}")
                    output.write(pytesseract.image_to_alto_xml(image, lang=lang))

        case _:
            print(f"type {outputtype} not yet implemented")

    print("INFO | finished processing OCR")


# entrypoint
if __name__ == "__main__":
    # parse arguments using argparse
    parser = argparse.ArgumentParser(
        prog="weihnachtsaufgabe",
        description="ocr multi-page pdf files using tesseract",
        # epilog='?'
    )
    parser.add_argument("inputfile")
    parser.add_argument("outputfile")
    parser.add_argument("-t", "--type", type=str)
    parser.add_argument("-l", "--lang", default="eng", type=str)
    parser.add_argument("-r", "--resolution", default=600, type=int)
    args = parser.parse_args()

    # check arguments for validity

    # check type:
    if args.type not in ["pdf", "hocr", "alto", "txt"]:
        # check if type is specified at all, if not attempt to look at ending of  outputfile
        if args.type == "" or args.type == None:
            o = args.outputfile.split(".")[-1:][0]
            print(
                f"WARN | no input type specified, attempting to determine type from outputfile {args.outputfile}: {o}"
            )
            while o not in ["pdf", "hocr", "alto", "txt"]:
                o = input(
                    "No known filetype for output could be detected, please select a filetype from ['pdf', 'hocr', 'alto', 'txt']"
                )
            args.type = o
        # if type is neither unspecified nor valid exit with error
        else:
            sys.exit(
                f"the type {args.type} is invalid, please specify a type from ['pdf', 'hocr', 'alto', 'txt']"
            )
    # check wether language-data is installed
    for lang in args.lang.split("+"):
        if lang not in pytesseract.get_languages():
            sys.exit(
                f"language {lang} is not installed, please install or modify your string to select from your installed languages {pytesseract.get_languages()} '"
            )

    # call main function with supplied arguments
    main(args.inputfile, args.outputfile, args.type, args.lang, args.resolutions)
