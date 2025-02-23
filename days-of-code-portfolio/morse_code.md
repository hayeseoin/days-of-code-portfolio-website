---
title: Morse Code Converter
tags:
  - Scripting
  - '100 Days of Code'
author: Eoin Hayes
github: "https://github.com/hayeseoin/days-of-code-82"
---

# Morse Code Converter
This script takes in a string, and outputs morse code.

The alphabet is a dictionary of key value pairs, associating each character to the morse code signal. It prints out the phrase in morse code. Letters are folowed by a space, words followed by two spaces. If an incompatible character is entered, it represented with an 'e'.

---
    #!python
    alphabet = {'A':'.-','B':'-...','C':'-.-.','D':'-..',
                'E':'.','F':'..-.','G':'--.','H':'....',
                'I':'..','J':'.---','K':'-.-','L':'.-..',
                'M':'--','N':'-.','O':'---','P':'.--.',
                'Q':'--.-','R':'.-.','S':'...','T':'-',
                'U':'..-','V':'...-','W':'.--','X':'-..-',
                'Y':'-.--','Z':'--..', ' ':' ', '1':'.----',
                '2':'..---', '3':'...--', '4':'....', '5':'.....',
                '6':'-....','7':'--...', '8':'---..', '9':'----.',
                '0':'-----'
                }

    def main():
        # Read word, convert to upper case string
        word: str = input('Please enter the word: ')
        word = word = str(word).upper()

        # List for morse characters
        morse = []
        # Loop through string, print 'e' if character not in alphabet
        for letter in word:
            char = alphabet.get(letter)
            try:
                morse.append(char + ' ')
            except TypeError:
                morse.append('e' + ' ')

        # Join word and print
        morse_word = ''.join(morse)
        print(morse_word)


    if __name__ == "__main__":
        main()
