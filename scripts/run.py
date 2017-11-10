#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:35:21 2017

@author: HelenaSpiewak & DanEgan

Script that calls functios in xml_parser on a given input LRG.xml file

"""

from xml_parser import *
from sys import argv

script, xml_file = argv

root = load_file(xml_file)

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

