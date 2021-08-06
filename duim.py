#!/usr/bin/env python3

import subprocess, sys
import os
import argparse



'''
OPS435 Assignment 2 - Summer 2021
Program: duim.py 
Author: "Hamza Najmuddin"
The python code in this file (duim.py) is original work written by
"Hamza Najmuddin". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <two functions are done for milestone1>

Date: 27 July 2021
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2021")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")

    
    args = parser.parse_args()


def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    graph = percent/100
    graph = graph * total_chars
    graph = round(graph)
    bar=""
    space=""
    p = 0
    i = 0
    end = total_chars - graph
    
    while p != graph:
        bar = bar + "#"
        p = p + 1
    finish = "["+ bar
    
    while i != end:
        space = space + " "
        i = i + 1
    finish = finish + space + "]"    
    
    return finish

def call_du_sub(location):
    "use subprocess to call `du -d 1 + location`, rtrn raw list"

    p = subprocess.Popen(['du -d 1 ' + location], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    outputlist = list(stdout)
    return outputlist

def create_dir_dict(raw_dat):
    "get list from du_sub, return dict {'directory': 0} where 0 is size"
    keys = [i.split('\t')[1] for i in raw_dat]
    valueslist = [i.split('\t')[0] for i in raw_dat]
    valuesint = [int(i) for i in valueslist]
    outputDict = dict(zip(keys, valuesint))
    return outputDict


if __name__ == "__main__":
    #take input from user and get directory size
    sub = call_du_sub(sys.argv[1])
    dit = create_dir_dict(sub)
    total_size = dit[sys.argv[1]]
    total_size = total_size / 1000
    #print(dit)
    holder = []
    val = []
