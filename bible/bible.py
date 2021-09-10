#!/usr/bin/env python

"""
Напишите функцию, которая находит n наиболее употребляемых слов из Библии.
Слова в возвращаемом списке идут по убыванию их частоты использования.
"""
from collections import Counter
from itertools import islice
from pathlib import Path

kjb_file = Path(__file__).parent.absolute() / 'king_james_bible.txt'
BIBLE = kjb_file.read_text()

TOP_WORDS_COINT = 10


def most_freq_bible_words(n: int) -> list:
    kjb_word_couner = Counter(BIBLE.lower().split())
    return [word for word, _ in kjb_word_couner.most_common(n)]


if __name__ == "__main__":
    print(*most_freq_bible_words(TOP_WORDS_COINT), sep='\n')
