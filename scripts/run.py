#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:35:21 2017

@author: HelenaSpiewak & DanEgan

Script that calls functions in xml_parser on a given input LRG.xml file to return
coding region sequence of each transcript, transcript comments, build coordinates
and build differences.

"""

from xml_parser import *
import argparse
import sys

# print help message when error method is triggered
# i.e. if script is run without arguments
# or an argument that does not exist
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('Error: %s\n' % message)
        self.print_help()
        sys.exit(2)
# help message to be displayed
parser=MyParser(description="""Program takes a LRG.xml file and returns coding region sequence of each transcript,
transcript comments, build coordinates and build differences.""", formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""Example of use:\n
Input: python run.py ../data/LRG_public_xml_files/LRG_13.xml
Output to console:

\t****** XML Parser for Locus Reference Genomic (LRG) files (v1) ******


** TRANSCRIPT DATA **

The LRG file ../data/LRG_public_xml_files/LRG_13.xml has the following 2 transcript(s):
t1, t2

The coding region for 't1' is:
ATGGGCTTCC.....TTCAAGCCTGA

Comments for transcript 't1':
None
--------------------

The coding region for 't2' is:
ATGGGCTTC.....AATGCCAACTAA

Comments for transcript 't2':
None
--------------------

** BUILD DIFFERENCE DATA **

In build 'GRCh37.p13'
Locus maps to coordinates: start '42576' and end '55193'.
Sequence differences for build 'GRCh37.p13':
Type	Ref_coord	Orig_base	LRG_base	LRG_coord
'mismatch'	'14991539'	'A'	'G'	'7294'

In build 'GRCh38.p7'
Locus maps to coordinates: start '14964669' and end '14977286'.
Sequence differences for build 'GRCh38.p7':
No sequence differences to report.

--------------------
""")

# assign arguments
parser.add_argument("file", help="File path of LRG file")
args = parser.parse_args()
xml_file = args.file

# test file
#xml_file = '/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml'
# store file for loading
root = load_file(xml_file)

# check that file is an lrg file
if root.tag == "lrg":
    # display welcome message
    print("""\n\t****** XML Parser for Locus Reference Genomic (LRG) files (v1) ******\n""")

    print("\n** TRANSCRIPT DATA **\n")
    # get transcript info
    num_of_t = transcripts(root)
    print('The LRG file ' + str(xml_file) + ' has the following %r transcript(s):' % len(num_of_t))
    # display transcript names
    print(', '.join(num_of_t))
    # for each transcript print coding region and comments
    for i in num_of_t:
        print("\nThe coding region for %r is:" % i)
        print(coding_region(root,i))
        print("\nComments for transcript %r:" %i)
        print(transcript_comment(root,i))
        print("-" * 20)

    print("\n** BUILD DIFFERENCE DATA **\n")
    # get build coordinates from xml file
    build_info = build_coord(root)
    for i in build_info:
        # display build coordinates for eacb build
        print("In build %r" % (i))
        print("Locus maps to coordinates: start %r and end % r." % (build_info[i]['other_start'], build_info[i]['other_end']))
        # for each build get the build difference info from xml file
        diffs = build_diff(root,i)
        # display build sequence difference for each build
        print("Sequence differences for build %r:" % i)
        if diffs:
            print("Type\tRef_coord\tOrig_base\tLRG_base\tLRG_coord")
            for i in diffs:
                print("%r\t%r\t%r\t%r\t%r\n" % (i.attrib["type"], i.attrib["other_start"], i.attrib["other_sequence"], i.attrib["lrg_sequence"], i.attrib["lrg_start"]))
        else:
            print("No sequence differences to report.\n")
    print("-" * 20)
else:
    print("File is not an LRG file. Exiting....")

## Legacy code attmpting to display exon information
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
