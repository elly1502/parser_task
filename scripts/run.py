#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 09:35:21 2017

@author: HelenaSpiewak
"""

from xml_parser import *
from sys import argv

script, xml_file = argv

root = load_file(xml_file)

# Display to user
# test file
#xml_file = '/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml'
root = load_file(xml_file)

if root.tag == "lrg":
    print("""*** XML Parser for Locus Reference Genomic (LRG) files ***\n\nUsage: python xml_parser.py path_to_LRG_file/LRG.xml\n\n\n
          """)
    print("You have inputted "+ str(xml_file) + "\n")

    ## Print name and number of transcripts 
    print('The xml file ' + str(xml_file) + ' has the following transcripts:')
   
    num_of_t = transcripts(root)
    print(num_of_t)
    print("\n")
    
    for i in num_of_t:
        print("The coding region for %r is:" % i)
        print("\n")
        print(coding_region(root,i))
        print("\n")
        print(transcript_comment(root,i))
        print("\n")
        
    build_info = build_coord(root)
    
    for i in build_info:
        print("In build %r" % (i))
        print("Locus maps to coordinates: start %r and end % r. \n" % (build_info[i]['other_start'], build_info[i]['other_end']))
     
        diffs = build_diff(root,i)
        if diffs:
            for i in diffs:
                print("Differences:\n")
                print("Type\tRef_coord\tOrig_base\tLRG_base\tLRG_coord")
                print("%r\t%r\t%r\t%r\t%r\n" % (i.attrib["type"], i.attrib["other_start"], i.attrib["other_sequence"], i.attrib["lrg_sequence"], i.attrib["lrg_start"]))
                


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

