"""
author: Johan Khanye
Date: 17 August 2019
"""

import re
import string as str_mod
from constants import (
    STATUS_PASS,
    STATUS_FAIL,
    IS_PALINDROME,
    IS_NOT_PALINDROME
)

def main(possible_palindrome):
    """ Check if included string is palindrome. """
    try:
        if palindrome(possible_palindrome):
            return {STATUS_PASS: IS_PALINDROME}
        else:
            return {STATUS_FAIL: IS_NOT_PALINDROME}


    except Exception as e:
        raise ValueError

def palindrome(string):
    """ identify if string is palindrome or not.
    """
    # whole text.
    reverse = string[::-1]

    # letters.
    if map(reverse.lower())==map(string.lower()):
        return True
    elif follow_words(string).lower()==map(string.lower()):
        return True
    else:
        return False

def map(sample):
    """This function will remove all puncuation marks and space """
    punctuation_marks = str_mod.punctuation+'""--\n'
    translator = str.maketrans(punctuation_marks, len(punctuation_marks)*' ')
    clean_string = sample.translate(translator).replace(" ","")

    return clean_string

def compare(sample):
    # if follow_words(sample)==
    pass

def follow_words(sample):
    """Follow the words, not the letters"""
    split = []
    reverse = ""

    for x in sample.split(" "):
        split.append(map(x))

    for i in range(len(split)):
        reverse+=split.pop()
    return reverse

if __name__ == '__main__':
    string = "A nut for a jar of tuna"
    print("Simple Example: ", main(string))

    geese = 'Do geese see God?'
    print("geese:", main(geese))

    panama="A man, a plan, a canal: Panama."
    print("panama: ",main(panama))

    long_eg='Are we not pure? "No, sir!" Panama\'s moody Noriega brags. "It is garbage!" Irony dooms a man-a prisoner up to new era'
    print("Long Example: ", main(long_eg))

    follow = "King, are you glad you are king?"
    print("Follow the words: ", main(follow))

    santas_naughty_list = """Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny,
     Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne,
     Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned."""
    print("naughty_list: ", main(santas_naughty_list))

    banana_boy = "Yo, banana boy!"
    print("Banana Boy: ", main(banana_boy))

    hitman = "Murder for a jar of red rum."
    print("Hitman for hire: ", main(hitman))
