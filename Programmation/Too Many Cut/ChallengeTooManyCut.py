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
from PIL import Image
    

#------------------------------------#
#                                    #
#               Main                 #
#                                    #
#------------------------------------#


if __name__ == '__main__':
    print("Starting...")
    #check if the directory exist
    if not os.path.isdir("split"):
        os.mkdir("split")
    #open the image
    img = Image.open("QRCode.png")
    #get the number of pixels 
    width, height = img.size
    print("Image size : {}x{}".format(width, height))
    #split the image in 1000 parts
    for i in range(0, width, 10):
        for j in range(0, height, 100):
            box = (i, j, i+10, j+100)
            #get the part of the image
            a = img.crop(box)
            #save the part of the image
            a.save("split/row-"+str(i)+"-column-"+str(j)+".png.png")
    print("Done")




