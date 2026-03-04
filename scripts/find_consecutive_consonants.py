#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
usage:
cat about.txt | python soinput.py
'''

import sys
import argparse

def read_in():
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    #print lines
    return lines

def main():
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#    s = read_in()
    lines = sys.stdin.readlines()
    s = ''
    consec = 4
    duplicate = 3
    maxlen = 4

    for j in range(len(lines)):
        s = lines[j].replace('\n','')
        # s = s[:s.index(";") + 0]

#        print([x for x in s.split() if any(len(set(x[i:i+2]).intersection(consonants))==  3 for i in range(len(x))) ])

#        print(s if any(len(set(s[i:i+2]).intersection(consonants))==  3 for i in range(len(s))))

        for x in s.split():
                #            print x
#            if len(x) <= maxlen and len(set(x).difference(consonants)) <= maxlen - consec:
#                s = ''
#            else:
            for i in range(len(x)):
                #                print i
                #                print set(x[i:i+consec]).intersection(consonants)
                
                #                if len(set(x[i:i+consec]).intersection(consonants))==  consec:
                if len(set(x[i:i+consec]).difference(consonants))==  0:
                    s = ''
                    #                    print 'conso!'
                    
                    if x[i:i+duplicate].count(x[i]) == duplicate:
                        s = ''

        print s

#            print three.join()

#            if any(len(set(s[i: i + 3]).intersection(consonants))) == 3:
#            print s

if __name__ == '__main__':
    main()

# print([x for x in s.split() if any(len(set(x[i:i+2]).intersection(vowels))==  2 for i in range(len(x))) ])

