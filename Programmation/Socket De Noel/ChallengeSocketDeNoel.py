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
import random
import time
from _thread import *
    

#------------------------------------#
#                                    #
#             Variables              #
#                                    #
#------------------------------------#


HOST = '0.0.0.0'
PORT = 9898
ThreadCount = 0

present_list = ['Bike', 'Car', 'Piano', 'Computer', 'Phone', 'Book', 'Toy', 'Clothes', 'Guitar', 'Drums', 'Saxophone', 'Flute', 'Violin', 'Bass', 'Keyboard', 'Watch', 'Shoes', 'Socks', 'Hat', 'Gloves', 'Scarf', 'Jacket', 'Trousers', 'Skirt', 'Dress', 'Shirt', 'Jeans', 'T-shirt', 'Pants', 'Jumper', 'Blouse', 'Coat', 'Sweater', 'Sweatshirt', 'Shorts', 'Underwear', 'Pyjamas', 'Swimsuit', 'Tie', 'Belt', 'Sunglasses', 'Glasses', 'Jewellery', 'Bag', 'Wallet', 'Backpack', 'Laptop', 'Tablet', 'Camera', 'Printer', 'Television', 'Radio', 'Headphones', 'Speakers', 'Games', 'DVDs', 'CDs', 'Cassette', 'Books', 'Magazines', 'Posters', 'Paintings', 'Pictures', 'Furniture', 'Garden furniture', 'Garden tools', 'Tools', 'Kitchen utensils', 'Kitchen appliances', 'Fork', 'Spoon', 'Knife', 'Plate', 'Bowl', 'Cup', 'Glass', 'Bottle', 'Saucer', 'Tin', 'Can', 'Jar', 'Biscuit', 'Chocolate', 'Candy', 'Cake', 'Butter', 'Oil', 'Salt', 'Pepper', 'Spice', 'Rice', 'Pasta', 'Bread', 'Burger', 'Hot dog', 'Ice cream', 'Tea', 'Coffee', 'Juice', 'Water', 'Soda', 'Beer', 'Wine', 'Whisky', 'Vodka', 'Rum', 'Gin', 'Liquor', 'Sweets', 'Gum', 'Chewing gum', 'Toothpaste', 'Toothbrush', 'Deodorant', 'Shampoo', 'Conditioner', 'Soap', 'Shower gel', 'Shaving cream', 'Razor', 'Shaving brush', 'Shaving soap', 'Shaving mug', 'Cologne', 'Perfume', 'Toilet paper', 'Tissues', 'Napkins', 'Towels', 'Toilet brush', 'Toilet cleaner', 'Toilet seat', 'Towel', 'Shower curtain', 'Shower head', 'Shower cap', 'Hairbrush', 'Comb', 'Hairdryer', 'Hair straightener', 'Hair curler', 'Hair gel', 'Hair spray', 'Hair wax', 'Hair conditioner', 'Hair mask', 'Hair dye', 'Hair shampoo']
    

#------------------------------------#
#                                    #
#             Functions              #
#                                    #
#------------------------------------#


chall_banner="""
[+]===================================================[+]
[+]            Challenge Socket De Noël               [+]
[+]                  by Mak'Hack                      [+]
[+]                  (c) Naylh                        [+]
[+]===================================================[+]

"""
    

chall_help="""
Welcome to the Socket De Noël Challenge !
Your family made you a list of things they wanted for Christmas,
you put everything together and wrote down the objects with their prices on slips of paper.
Because you don't have an expandable budget and in order not to make anyone jealous,
you put these pieces of paper in a hat and draw lots of different objects that you will have to buy.
As you are very strong in mental calculation you must give what you will cost this list in less than 2 s.
Good luck.

You are able to give only an integer or these commands :
    'help' : Displays this help message
    'monkey' : Displays a monkey
    'exit' : Quits the service

"""

chall_monkey=r"""
            _______________________
           / I'm here, now get     \
           \ back to the challenge /
            ----------------------- 
                                    \
                                     \    .="=.
                                        _/.-.-.\_      _
                                       ( ( o o ) )     ))
                                        |/  "  \|     //
                                         \'---'/    //
                                         /`"'"`\\   ((
                                        / /_,_\ \\   \\
                                        \_\\_'__/ \   ))
                                         /`  /`~\    //
                                        /   /    \  /
                                    ,--`,--'\/\    /
                                    '-- "--'  '--'
"""
    

def generate_random_dictionnary():
    random_list = {}
    for i in range(0, 15):
        random_list[random.choice(present_list)] = random.randint(1, 100)
    return random_list


def transform_dict_to_string(dict):
    string = ""
    for key, value in dict.items():
        string += key + " : " + str(value) + "€\n"
    string+='\n'
    return string


def check_addition(dict, result):
    total = 0
    for key, value in dict.items():
        total += value
    if total == result:
        return True
    return False


def multi_threaded_client(connection):
    start = time.time()
    generated_list = generate_random_dictionnary()
    connection.send((chall_banner+chall_help+transform_dict_to_string(generated_list)).encode())
    prompt_running = True
    while True:
        try:
            while prompt_running:
                data = connection.recv(2048).decode()
                if not data:
                    break
                end=time.time()
                if data == 'help\n':
                    connection.send(chall_help.encode())
                    prompt_running = False
                elif data == 'exit\n':
                    connection.send("Bye !".encode())
                    prompt_running = False
                elif data == 'monkey\n':
                    connection.send(chall_monkey.encode())
                    prompt_running = False
                elif data[:-1].isdigit():
                    if end-start > 2:
                        connection.send("Too late !".encode())
                        prompt_running = False
                    elif check_addition(generated_list,int(data)):
                        with open("flag.txt", "r") as flag_file:
                            flag = flag_file.read()
                        connection.send(("Good job ! Here is your flag : %s" % str(flag)).encode())
                        prompt_running = False
                    else :
                        connection.send("Wrong answer !\n".encode())
                else:
                    connection.send("Unknown command, type 'help' for help\n".encode())
        except EOFError as e:
            pass
        break
    connection.send("You has been disconnected".encode())
    connection.close()


#------------------------------------#
#                                    #
#               Main                 #
#                                    #
#------------------------------------#


ServerSideSocket = socket.socket()
try:
    ServerSideSocket.bind((HOST, PORT))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()