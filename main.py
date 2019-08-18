"""
author: Johan Khanye
Date: 17 August 2019
"""

import re
import string as str_mod
from constants import (
    STATUS_OK,
    STATUS_ERROR,
    IS_PALINDROME,
    IS_NOT_PALINDROME
)

def main(possible_palindrome):
    """ Check if included string is palindrome. """
    try:
        if palindrome(possible_palindrome):
            return {STATUS_OK: IS_PALINDROME}
        else:
            return {STATUS_OK: IS_NOT_PALINDROME}


    except Exception as e:
        raise ValueError

def palindrome(string):
    """ identify if string is palindrome or not.
    """
    reverse = ""
    for i in range(len(string)):
        reverse += string[-(i+1)]

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


    poem = """
        Entering the lonely house with my wife
    I saw him for the first time
    Peering furtively from behind a bush --
    Blackness that moved,
    A shape amid the shadows,
    A momentary glimpse of gleaming eyes
    Revealed in the ragged moon.
    A closer look (he seemed to turn) might have
    Put him to flight forever --
    I dared not
    (For reasons that I failed to understand),
    Though I knew I should act at once.

    I puzzled over it, hiding alone,
    Watching the woman as she neared the gate.
    He came, and I saw him crouching
    Night after night.
    Night after night
    He came, and I saw him crouching,
    Watching the woman as she neared the gate.

    I puzzled over it, hiding alone --
    Though I knew I should act at once,
    For reasons that I failed to understand
    I dared not
    Put him to flight forever.

    A closer look (he seemed to turn) might have
    Revealed in the ragged moon.
    A momentary glimpse of gleaming eyes
    A shape amid the shadows,
    Blackness that moved.

    Peering furtively from behind a bush,
    I saw him for the first time,
    Entering the lonely house with my wife.
    """
    print("Poem: ", main(poem))
