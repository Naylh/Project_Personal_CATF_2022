#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author             : Naylh
# Python Version     : 3.*
    

#------------------------------------#
#                                    #
#              Import                #
#                                    #
#------------------------------------#


import os
import random
    

#------------------------------------#
#                                    #
#               Main                 #
#                                    #
#------------------------------------#


Morse_Alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
Morse_Alphabet_Without_T_F = [".-", "-...", "-.-.", "-..", ".", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
flag = [".", ".-", "--", "-.-", "{", "....-", "-.", "-----" ,"-", "-----", "-.--", "-...", "-----", "-", "-.-", "-.--", "-----", ".--", "...-", "....", "....-", "--", "}"]


if __name__ == '__main__':
    print("Starting...")
    print("Making the tree...")
    if not os.path.isdir("tree"):
        os.mkdir("tree")
    for i in range(1, 51):
        print("Making the branch "+str(i)+"...")
        os.mkdir("tree/branch_" + str(i))
        for j in range(1, 51):
            os.mkdir("tree/branch_" + str(i) + "/leaf_" + str(j))
            for k in range(1, 51):
                os.mkdir("tree/branch_" + str(i) + "/leaf_" + str(j) + "/needle_" + str(k))
                with open("tree/branch_" + str(i) + "/leaf_" + str(j) + "/needle_" + str(k) + "/needle", "w") as f:
                    f.write(Morse_Alphabet_Without_T_F[random.randint(0, len(Morse_Alphabet_Without_T_F)-1)])
    os.remove("tree/branch_1/leaf_1/needle_1/needle")
    with open("tree/branch_1/leaf_1/needle_1/Flag", "w") as f:
        f.write("You have been rick rolled")
    with open("tree/branch_4/leaf_18/needle_46/needle", "w") as f:
        f.write("CATF grep will be useless here")
    for i in range(len(flag)):
        os.remove("tree/branch_" + str(i+25) + "/leaf_" + str(i+26) + "/needle_" + str(i+27) + "/needle")
        with open("tree/branch_" + str(i+25) + "/leaf_" + str(i+26) + "/needle_" + str(i+27) + "/needle", "a") as f:
           f.write(flag[i])
    print("Done !")

#Char (CATF{4L0T0FW0RKF0RTH4T}) -> Vigenere(EAMK{4N0T0YB0TKY0WVH4M}) + key = CATF -> Morse (. .- -- -.- {....- -. ----- - ----- -.-- -... ----- - -.- -.-- ----- .-- ...- .... ....- --})