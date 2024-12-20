#!/usr/bin/python python3.12
"""
author: Sebastian Fath
"""
from pprint import pprint
import pandas as pd
import pypdf
import argparse
import re
import spacy


# generate_text_from_pdf requires path_to_file for input_file, path_to_file or None for output_file. If output is None, will print to stdout, for lib use: if not called as "__main__", will not write to stdout
def generate_text_from_pdf(input_file, output_file=None):
    pdf_file = pypdf.PdfReader(input_file)
    text = ""
    for page in pdf_file.pages:
        text += page.extract_text()
    if output_file is None and __name__ == "__main__":
        print(text)
    else:
        with open(output_file, "w") as f:
            f.write(text)
    # return final text for library use
    return text

# remove_line_spillover requires path_to_file for input_file, path_to_file or None for output_file. If output is None, will print to stdout, for lib use: if not called as "__main__", will not write to stdout
def remove_line_spillover(input_file, output_file=None):
    text = ""
    clean_text = ""
    with open(input_file, "r") as ifile:
        text = ifile.read()

    # remove spillover
    for word in text.split(" "):
        if "-\n" in word:
            word = word.replace("-\n", "")
        clean_text += f"{word} "

    # save cleaned text to file or stdout
    if output_file is None:
        if __name__ == "__main__":
            print(text)
        else:
            return text
    else:
        with open(output_file, "w") as ofile:
            ofile.write(clean_text)
    # return final text for library use
    return clean_text

# count_words requires string for input_string, path_to_file or None for output_file. If output is None, will print to stdout, for lib use: if not called as "__main__", will not write to stdout
def count_words(input_string, output_file=None):
    wordcounts = {}
    # use regex to create a list of all words; regex is used because it automatically strips punctuation; \w+ = return word characters (a-z, A-Z, 0-9) until no longer possible
    words = re.findall(r"\w+", input_string)

    # iterate over words, add to dictionary and count
    for word in words:
        word = word.lower()
        if wordcounts.get(word) is None:
            wordcounts[word] = 1
        else:
            wordcounts[word] += 1

    # save wordcounts to file or stdout
    if output_file is None:
        if __name__ == "__main__":
            print(wordcounts)
        else:
            return wordcounts
    else:
        pd.DataFrame(wordcounts.items(), columns=["word", "count"]).to_csv(output_file, index=False)
    # return final text for library use
    return wordcounts

# load_nlp requires string for input_string, path_to_file or None for output_file. If output is None, will print to stdout, for lib use: if not called as "__main__", will not write to stdout
def load_nlp(input_string, lang="deu"):
    # determine which model to use based on language
    nlp_model = ""
    match lang:
        case "deu":
            # requires running python -m spacy download de_core_news_lg
            nlp_model = "de_core_news_lg"
        case "eng":
            # requires running python -m spacy download en_core_web_lg
            nlp_model = "en_core_web_lg"
        case _:
            Exception(f"ERROR | Language {lang} not yet implemnted in generator.nlp_data()")
    # init spacy nlp
    nlp = spacy.load(nlp_model)
    # read string and return
    return nlp(input_string)



# Entrypoint
if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-t", "--task", help="specify which task to run", required=True)
    argparser.add_argument("-i", "--input", help="string to specify input parameters")
    argparser.add_argument("-o", "--output", help="string to specify output parameters")

    args = argparser.parse_args()

    match args.task:
        # fn generate_text requires path_to_file for input_file, path_to_file or None for output_file. If output is None, will print to stdout
        case c if c in ["generate-text-from-pdf", "pdf-to-txt", "gen-txt", "0"]:
            generate_text_from_pdf(input_file=args.input, output_file=args.output)
        # fn remove_line_spillover requires path_to_file for input_file, path_to_file or None for output_file. If output is None, will print to stdout
        case c if c in ["remove-spillover", "rm-spillover", "clean-step1", "1"]:
            remove_line_spillover(input_file=args.input, output_file=args.output)
        # fn count_words requires string for input_string, path_to_file or None for output_file. If output is None, will print to stdout
        case c if c in ["create-wordcount", "count-words-in-file", "2"]:
            with open(args.input, "r") as f:
                count_words(input_string=f.read(), output_file=args.output)
        # fn load_nlp requires ...
        case c if c in ["nlp", "load_nlp", "3"]:
            with open(args.input, "r") as f:
                pprint(load_nlp(input_string=f.read()))
        case _:
            print(f"Invalid task specified: {args.task}")

