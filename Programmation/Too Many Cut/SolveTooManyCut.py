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
    #create an empty image with the size of 1000x1000
    img_final = Image.new('RGB', (1000, 1000))
    #for each file in the directory
    for file in os.listdir("split"):
        #open the image
        img = Image.open("split/"+file)
        #put it in the final image
        img_final.paste(img, (int(file.split("-")[1]), int(file.split("-")[3].split(".")[0])))
    #save the final image
    img_final.save("QRCode_test.png")
    print("Done")
                
