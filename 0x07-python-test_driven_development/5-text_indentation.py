#!/usr/bin/python3
"""
This module prints text with 2 newlines after
character - . ? :
"""


def text_indentation(text):
    """
    function to print text and 2 newlines
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError('text must be a string')
    string = "".join([a if a not in ".?:" else a + "\n\n" for a in text])
    print("\n".join([x.strip() for x in string.split("\n")]), end="")
