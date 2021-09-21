#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def get_num_letters(text):
    nb_letters = 0
    for character in text:
        if character.isalnum():
            nb_letters += 1
    return nb_letters


def get_word_length_histogram(text):
    word_list = text.split()
    len_list = [0]*(len(word_list))
    for i, word in enumerate(word_list):
        len_list[i] = get_num_letters(word)
    len_list.sort()
    histo = [0]*(len_list[len(len_list)-1]+1)
    for nb in len_list:
        histo[nb] += 1
    return histo


def format_histogram(histogram:List):
    ROW_CHAR = "*"
    string = ""
    for i in range(1, len(histogram)):
        string += f"{i} "
        for j in range(histogram[i]):
            string += ROW_CHAR
        string += "\n"
    return string


def format_horizontal_histogram(histogram:List):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"
    histogram.remove(0)
    list_string=[]
    string =""
    for i in range(len(histogram)):
        string+=LINE_CHAR
    list_string.append(string)
    while any(histogram)!=0:
        string = ""
        for i in range(len(histogram)):
            if histogram[i]>0:
                string+=BLOCK_CHAR
                histogram[i]-=1
            else:
                string+=" "
        list_string.append(string)
    histo=""
    height=len(list_string)
    for i in range(height):
        histo+=f"{list_string.pop()}\n"
    return histo


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
