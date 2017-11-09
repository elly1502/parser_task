#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:45:07 2017

@author: HelenaSpiewak
"""
# modules to import
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from sys import argv
#import glob 

script, xml_file = argv

# quick xml file import
#xml_file =sorted( glob.glob("/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/*.xml"))

# sanity check path of file
#print(xml_file[0])

# load in xml data
tree = ET.parse(xml_file)
root = tree.getroot()

# Pull out genomic sequence
def genomic_seq(root):
   dna_seq = root.find("./fixed_annotation/sequence").text     
   return dna_seq

def find_coding_coordinate(root, trans_name):  
    find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/coding_region/coordinates" 
    start = root.find(find_str).attrib['start']
    end = root.find(find_str).attrib['end']       
    return start, end
    
def coding_region(root, trans_name):
    seq = genomic_seq(root)
    coor = find_coding_coordinate(root, trans_name)
    start = int(coor[0])-1
    stop = int(coor[1])
    return seq[start:stop]

def transcript_comment(root, trans_name):
    find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/comment"
    comment = root.find(find_str).text
    return comment

def build_coord(root):
    all_build = root.findall("./updatable_annotation/annotation_set/[@type='lrg']/mapping")
    builds = {}
    for i in all_build:
        builds[i.get("coord_system")] = i.find("./mapping_span").attrib
    return builds

def build_diff(root, build_num):
    find_string = "./updatable_annotation/annotation_set/[@type='lrg']/mapping/[@coord_system=" + "'" + str(build_num) +  "'" + "]/mapping_span/diff"
    difference = root.findall(find_string)
    return difference

def transcripts(root):
    num_of_t = list()
    t_list = root.findall("./fixed_annotation/transcript")  
    for i in t_list:
        num_of_t.append(i.attrib['name'])
    return num_of_t

if root.tag == "lrg":
    print("""*** XML Parser for Locus Reference Genomic (LRG) files ***\n\nUsage: python xml_parser.py path_to_LRG_file/LRG.xml\n\n\n
          """)
    print("You have inputted "+ str(xml_file) + "\n")
    print("The coding sequence for this xml file:\n")
    
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



         