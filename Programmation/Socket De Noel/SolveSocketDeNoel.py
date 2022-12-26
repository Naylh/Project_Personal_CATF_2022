#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author             : Naylh
# Python Version     : 3.*
    

#------------------------------------#
#                                    #
#              Import                #
#                                    #
#------------------------------------#


import socket
    

#------------------------------------#
#                                    #
#             Variables              #
#                                    #
#------------------------------------#


HOST = "127.0.0.1"
PORT = 9898


#------------------------------------#
#                                    #
#               Main                 #
#                                    #
#------------------------------------#


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        message_recu=s.recv(2048).decode()
        print(message_recu)
        
        recu=message_recu.split("service")
        #print(recu)
        
        #print("La liste reçue est : {}".format(recu[1]))

        #get only the index where there is a '€'
        index=[]
        for i in range(0,len(recu[1])):
            if recu[1][i]=='€':
                index.append(i)

        #get the price of each present
        price=[]
        for i in range(0,len(index)):
            price.append(recu[1][index[i]-2:index[i]])
        #print("Les prix sont : {}".format(price))

        total=0
        for i in price:
            total+=int(i)
        #print("Le total est : {}".format(total))
        
        s.send(str(total).encode())

        flag=s.recv(1024).decode()
        print("Le flag est : {}".format(flag))

        print ("Close")
        #s.close()
    





