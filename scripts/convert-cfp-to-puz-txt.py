#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
usage:
cat puzzle.cfp | python convert-cfp-to-puz-txt.py > newpuzzle.puz.txt
'''

import sys
import xml.etree.ElementTree as ET
import re
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('xml_filename', help='.xml file to convert')
    args = parser.parse_args()

    #print args.xml_filename

    dom = ET.parse(args.xml_filename)
    root = dom.getroot()
    # for child in root:
    #     print (child.tag, child.attrib)
    print ("<ACROSS PUZZLE V2>")
    print ("<TITLE>")
    print ("    " + root.find('TITLE').text)
    print ("<AUTHOR>")
    print ("    " + root.find('AUTHOR').text)
    print ("<COPYRIGHT>")
    print ("    " + root.find('COPYRIGHT').text)
    print ("<SIZE>")
    print ("    " + root.find('GRID').attrib.get('width') + 'x' + root.find('GRID').attrib.get('width'))
    print ("<GRID>")
    #print (re.sub('^', '    ', root.find('GRID').text.rstrip().lstrip(), count=0))
    print ('    ' + '    '.join(root.find('GRID').text.rstrip().lstrip().splitlines(True)))
    print ("<ACROSS>")
    for word in root.iter('WORD'):
        if word.attrib.get('dir') == 'ACROSS':
            print "    " + word.text
    print ("<DOWN>")
    for word in root.iter('WORD'):
        if word.attrib.get('dir') == 'DOWN':
            print "    " + word.text
    
    #for word in root.iter('WORD'):
        #print (word.tag, word.attrib, word.text)
    # print (ET.tostring(dom))
    # xslt = ET.parse(args.xsl_filename)
    # transform = ET.XSLT(xslt)
    # newdom = transform(dom)
    # print(ET.tostring(newdom, pretty_print=True))

# def read_in():
#     lines = sys.stdin.readlines()
#     for i in range(len(lines)):
#         lines[i] = lines[i].replace('\n','')
#     #print lines
#     return lines

# def main():
#     vowels = "aeiouAEIOU"
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# #    s = read_in()
#     lines = sys.stdin.readlines()
#     s = ''
#     consec = 4
#     duplicate = 3
#     maxlen = 4

#     for j in range(len(lines)):
#         s = lines[j].replace('\n','')
#         # s = s[:s.index(";") + 0]

# #        print([x for x in s.split() if any(len(set(x[i:i+2]).intersection(consonants))==  3 for i in range(len(x))) ])

# #        print(s if any(len(set(s[i:i+2]).intersection(consonants))==  3 for i in range(len(s))))

#         for x in s.split():
#                 #            print x
# #            if len(x) <= maxlen and len(set(x).difference(consonants)) <= maxlen - consec:
# #                s = ''
# #            else:
#             for i in range(len(x)):
#                 #                print i
#                 #                print set(x[i:i+consec]).intersection(consonants)
                
#                 #                if len(set(x[i:i+consec]).intersection(consonants))==  consec:
#                 if len(set(x[i:i+consec]).difference(consonants))==  0:
#                     s = ''
#                     #                    print 'conso!'
                    
#                     if x[i:i+duplicate].count(x[i]) == duplicate:
#                         s = ''

#         print s

# #            print three.join()

# #            if any(len(set(s[i: i + 3]).intersection(consonants))) == 3:
# #            print s

if __name__ == '__main__':
    main()

# print([x for x in s.split() if any(len(set(x[i:i+2]).intersection(vowels))==  2 for i in range(len(x))) ])

