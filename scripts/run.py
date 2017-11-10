#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:35:21 2017

@author: HelenaSpiewak & DanEgan

Script that calls functions in xml_parser on a given input LRG.xml file to return
coding region sequence of each transcript, transcript comments, build coordinates
and build differences.

Usage: python LRG_parser.py <path_to_LRG_file>
Options:
    --h display help information.

Example:
Input: python LRG_parser.py ../data/LRG_public_xml_files/LRG_13.xml
Output to console:
*** XML Parser for Locus Reference Genomic (LRG) files ***

~~~~~~~~~~~~~~~~~~~~
~~ TRANSCRIPT DATA ~~
The xml file ../data/LRG_public_xml_files/LRG_13.xml has the following transcripts:
['t1, 't2']
The coding region for 't1' is:
ATGTTCAGCT.....TCGACGTTGGCCCTGTCTGCTTCCTGTAA

Comments for transcript 't1':
None

~~~~~~~~~~~~~~~~~~~~

~~ BUILD DIFFERENCE DATA ~~

In build 'GRCh38.p7'
Locus maps to coordinates: start '50182096' and end '50206639'.

~~~~~~~~~~~~~~~~~~~~
In build 'GRCh37.p13'
Locus maps to coordinates: start '48259457' and end '48284000'.

~~~~~~~~~~~~~~~~~~~~
Differences:
Type	Ref_coord	Orig_base	LRG_base	LRG_coord
'mismatch'	'48265495'	'A'	'G'	'18506'

~~~~~~~~~~~~~~~~~~~~
"""

from xml_parser import *
from sys import argv

# assign arguments
script, xml_file, flag = argv
## look up optional arguments in python
root = load_file(xml_file)
if flag == "--h" or not xml_file:
    print("""LRG_parser takes a given input LRG.xml file to return
    coding region sequence of each transcript, transcript comments, build coordinates
    and build differences.

    Usage: python LRG_parser.py <path_to_LRG_file>
    Options:
        --h display help information.

    Example:
    Input: python LRG_parser.py ../data/LRG_public_xml_files/LRG_13.xml
    Output to console:
    *** XML Parser for Locus Reference Genomic (LRG) files ***

    ~~~~~~~~~~~~~~~~~~~~
    ~~ TRANSCRIPT DATA ~~
    The xml file ../data/LRG_public_xml_files/LRG_13.xml has the following transcripts:
    ['t1, 't2']
    The coding region for 't1' is:
    ATGTTCAGCT.....TCGACGTTGGCCCTGTCTGCTTCCTGTAA

    Comments for transcript 't1':
    None

    ~~~~~~~~~~~~~~~~~~~~

    ~~ BUILD DIFFERENCE DATA ~~

    In build 'GRCh38.p7'
    Locus maps to coordinates: start '50182096' and end '50206639'.

    ~~~~~~~~~~~~~~~~~~~~
    In build 'GRCh37.p13'
    Locus maps to coordinates: start '48259457' and end '48284000'.

    ~~~~~~~~~~~~~~~~~~~~
    Differences:
    Type	Ref_coord	Orig_base	LRG_base	LRG_coord
    'mismatch'	'48265495'	'A'	'G'	'18506'

    ~~~~~~~~~~~~~~~~~~~~
    """)
    sys.exit()
else:
# test file
#xml_file = '/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml'
    # store file for loading
    root = load_file(xml_file)

    # check that file is an lrg file
    if root.tag == "lrg":
        print("""*** XML Parser for Locus Reference Genomic (LRG) files ***\n\nUsage: python xml_parser.py path_to_LRG_file/LRG.xml\n
              """)
        print("~" * 20)
        ## Print name and number of transcripts
        print("\n~~ TRANSCRIPT DATA ~~\n")
        print('The xml file ' + str(xml_file) + ' has the following transcripts:')

        num_of_t = transcripts(root)
        print(num_of_t)
        print("\n")
        # for each transcript print coding region and comments
        for i in num_of_t:
            print("The coding region for %r is:" % i)
            print(coding_region(root,i))
            print("\n")
            print("Comments for transcript %r:" %i)
            print(transcript_comment(root,i))
            print("\n")
            print("~" * 20)

        # Display build difference info
        print("\n~~ BUILD DIFFERENCE DATA ~~\n")
        build_info = build_coord(root)

        for i in build_info:
            # display build coordinates
            print("In build %r" % (i))
            print("Locus maps to coordinates: start %r and end % r. \n" % (build_info[i]['other_start'], build_info[i]['other_end']))
            print("~" * 20)
            diffs = build_diff(root,i)
            if diffs:
                for i in diffs:
                    print("Differences:")
                    # display differences written in xml file
                    print("Type\tRef_coord\tOrig_base\tLRG_base\tLRG_coord")
                    print("%r\t%r\t%r\t%r\t%r\n" % (i.attrib["type"], i.attrib["other_start"], i.attrib["other_sequence"], i.attrib["lrg_sequence"], i.attrib["lrg_start"]))
        print("~" * 20)
    else:
        print("File is not an LRG file. Exiting....")

    #ex_coord = exons_coord(root, i)
    #        print(ex_coord)
    #        x = {}
    #        ex_list = exons_labels(root, i)
    #
    #
    #        for k in exons_labels(root, i):
    #            ex_label.append(k.attrib["label"])
    #
    #
    #            print(exon_label, ex_coord["coord_system"], ex_coord["start"], ex_coord["end"])
    #
    #            exon_coord_system = n.attrib["coord_system"]
    #            exon_start = n.attrib["start"]
    #            exon_end = n.attrib["end"]
    #            print(exon_coord, exon_start, exon_end)
