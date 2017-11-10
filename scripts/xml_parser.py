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
import re
import sys
#from sys import argv
#import glob 

#script, xml_file = argv

# quick xml file import
#xml_file =sorted( glob.glob("/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/*.xml"))

# sanity check path of file
#print(xml_file[0])

# load in xml data if LRG file
def load_file(xml_file):
    """Load in XML file and return root"""
    # error if no file given or file doesnt end in .xml
    assert (len(xml_file) > 1), "No file given"
    assert (".xml" in xml_file), "File given is not an .xml file"
    
    if re.search(r".*LRG_.*.xml", xml_file):
        tree = ET.parse(xml_file)
        return tree.getroot()
    else: 
        message = "Error: File %r is not an LRG file. Programme will close!" % xml_file
        return sys.exit(message)

# Pull out genomic sequence
def genomic_seq(root):
    """ Returns genomic DNA sequence of root LRG file 
    Usage: genomic_seq(root) """
    dna_seq = root.find("./fixed_annotation/sequence").text
    return dna_seq

# Get start and stop coordinates for a transcript
def find_coding_coordinate(root, trans_name):  
    """ Returns start and end coordinates for a transcript in LRG file """
    # build a str to point to correct child in tree for specific transcript
    find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/coding_region/coordinates" 
    # Get start and stop attributes
    start = root.find(find_str).attrib['start']
    end = root.find(find_str).attrib['end']       
    return start, end
    
def coding_region(root, trans_name):
    """ Returns coding region DNA sequence for a transcript in LRG file """
    # Get DNA sequence and coordinates
    seq = genomic_seq(root)
    coor = find_coding_coordinate(root, trans_name)
    # factor in 0 index of pyhton for start coord
    start = int(coor[0])-1
    stop = int(coor[1])
    # slice DNA sequence using start stop coords
    return seq[start:stop]

def transcript_comment(root, trans_name):
    
    find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/comment"
    comment = root.find(find_str).text
    return comment

def exons_labels(root, trans_name):
    """ Returns a list of exon labels """
    find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/exon"
    exons_labels_dic = root.findall(find_str)
    ex_list = []
    for k in exons_labels_dic:
            ex_list.append(k.attrib["label"])
    return ex_list

def exons_coord(root, trans_name):
     """ Returns a list of exon coordinates """
     find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/exon/coordinates"
     exon_coords = root.find(find_str).attrib
     return exon_coords

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


# To do:
# exons
# Assets
# Tests
# docstrings
# tidy up the interface
# also write output to text file
                
                

         