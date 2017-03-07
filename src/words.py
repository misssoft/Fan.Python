#! /usr/bin/env python
"""Retrieve and print words from URL.
Usage:
    python words.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL
    Args
        url: The URL of a UTF-8 text document.
    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(story_words):
    """Print a list of items
        Args
            story_words: Words of a story etc
        """
    for word in story_words:
        print(word)


def main(url):
    """Fetch the words and print them out
        Args
            url: url for the txt file
        Returns:
            A list of strings containing the words from the document.
        """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename