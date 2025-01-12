import string
import re

def string_preprocessing(text: str) -> str:
    text_clrd = text.lower()
    text_clrd = text_clrd.translate(str.maketrans('', '', string.punctuation))
    text_clrd = " ".join(text_clrd.split())
    return text_clrd

def count_words(text: str) -> int: #ho cambiato il tipo di ritorno (perchè dict?)
    wc = len(text.split())
    print("Il wordcount è: " + str(wc))
    return wc

def find_longest_word(text: str) -> str:
    text_lw = string_preprocessing(text)
    words = text_lw.split()
    if not words:
        return ""
    print("Longest word:" + max(words, key=len))
    return max(words, key=len)
    pass

def format_sentences(text: str) -> list:
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)([\s\n]|$)', text)
    formatted_sentences = [
        string_preprocessing(part).capitalize()
        for part in sentences
        if string_preprocessing(part)
    ]
    print(formatted_sentences)
    return formatted_sentences
    pass