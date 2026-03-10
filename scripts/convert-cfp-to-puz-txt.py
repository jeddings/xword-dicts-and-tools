#!/usr/bin/env python3
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
    print("<ACROSS>")
    for word in root.iter('WORD'):
        if word.attrib.get('dir') == 'ACROSS':
            print("    " + word.text)
    print("<DOWN>")
    for word in root.iter('WORD'):
        if word.attrib.get('dir') == 'DOWN':
            print("    " + word.text)
    
    #for word in root.iter('WORD'):
        #print (word.tag, word.attrib, word.text)
    # print (ET.tostring(dom))
    # xslt = ET.parse(args.xsl_filename)
    # transform = ET.XSLT(xslt)
    # newdom = transform(dom)
    # print(ET.tostring(newdom, pretty_print=True))


if __name__ == '__main__':
    main()
