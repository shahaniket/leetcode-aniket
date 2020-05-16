#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:03:21 2020

Question: https://leetcode.com/problems/jewels-and-stones/
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and
S are letters. Letters are case sensitive, so "a" is considered a
different type of stone from "A".

@author: anikts
"""

def numJewelsInStones(J, S):
    jewel_dict = {}
    for j in J:
        jewel_dict[j]=True
    jewel_count = 0
    for s in S:
        if s in jewel_dict:
            jewel_count+=1
    return jewel_count

J = "aA"
S = "aAAbbbb"
numJewelsInStones(J,S)