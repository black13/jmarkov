import unittest
import markovify
import sys, os
import operator

def main():
    with open(os.path.join(os.path.dirname(__file__), "pg23393.txt")) as f:
        text = f.read()
        model = markovify.Text(text)

    text_model = model
    sent = None
    for x in range(100):
        sent = text_model.make_short_sentence(45)
        if sent:
            print(sent)
'''
    for x in range(100):
        start_str = "noch"
        sent = text_model.make_sentence_with_start(start_str, strict=False)
        if sent:
            print(sent)
'''
if __name__ == "__main__":
    main()
