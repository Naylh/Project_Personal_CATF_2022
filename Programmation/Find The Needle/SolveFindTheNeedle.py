#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author             : Naylh
# Python Version     : 3.*
    

#------------------------------------#
#                                    #
#              Import                #
#                                    #
#------------------------------------#


import time
    

#------------------------------------#
#                                    #
#          Global Variables          #
#                                    #
#------------------------------------#


MORSE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}


flagSize = 23 #17+6


#------------------------------------#
#                                    #
#             Functions              #
#                                    #
#------------------------------------#


def getLetterFromMorse(branch, leaf, needle):
    with open(f"branch_{branch}/leaf_{leaf}/needle_{needle}/needle") as f:
        n = f.read()
    #check if n is a value in MORSE_DICT if true return the key
    for key, value in MORSE_DICT.items():
        if n == value:
            return key
    return ""


def vigenere(cipher):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    cpt = 0
    for char in cipher:
        if char in alphabet:
            ans += alphabet[(alphabet.index(char)-alphabet.index("CATF"[cpt%4]))%len(alphabet)]
            cpt += 1
        else:
            ans += char
    return ans


#------------------------------------#
#                                    #
#               Main                 #
#                                    #
#------------------------------------#


if __name__ == '__main__':
    print("Starting...")
    start = time.time()

    for branch in range(1, 51):
        for leaf in range(1, 51):
            for needle in range(1, 51):
                if (branch, leaf, needle) != (1,1,1): #vous avez kiffé le rickroll ? :D
                    for offset in [1,2]:
                        if branch+flagSize*offset <= 50 and leaf+flagSize*offset <= 50 and needle+flagSize*offset <= 50:
                            cipher = ""
                            for i in range(flagSize):
                                cipher += getLetterFromMorse(branch+i*offset, leaf+i*offset, needle+i*offset)
                            flag = vigenere(cipher)
                            #print(flag)
                            if "CATF" in flag:
                                print(flag)

    print("The program took : ", time.time()-start)
    print("Done")          