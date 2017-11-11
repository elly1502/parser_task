#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:45:07 2017

@author: HelenaSpiewak & DanEgan

Functions for extracting data within a Locus Reference Genomic .xml file.

"""
# Modules to import
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import re
import sys
#import glob

# quick xml file import
#xml_file =sorted( glob.glob("/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/*.xml"))

# sanity check path of file
#print(xml_file[0])

# Load in xml data if LRG file
def load_file(xml_file):
    """Load in XML file and return root"""
    # error if no file given or file doesnt end in .xml
    assert (len(xml_file) > 1), "No file given"
    assert (".xml" in xml_file), "File given is not an .xml file"
    # check that given file has LRG in filename (case insensitive), exit otherwise
    if re.search(r".*LRG_.*.xml", xml_file, re.IGNORECASE):
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

# Get coding region DNA sequence
def coding_region(root, trans_name):
    """ Returns coding region DNA sequence for a transcript in LRG file """
    # Get DNA sequence and coordinates
    seq = genomic_seq(root)
    coor = find_coding_coordinate(root, trans_name)
    # factor in 0 index of python for start coord
    start = int(coor[0])-1
    stop = int(coor[1])
    # slice DNA sequence using start stop coords
    return seq[start:stop]

# Get transcript comments
def transcript_comment(root, trans_name):
    '''Returns comments related to each transcript '''
    # build a string for each specific transcript name to find correct child
    find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/comment"
    if root.find(find_str):
        # if comments exist, get all comments for a transcript
        comment = root.find(find_str).text
    else:
        comment = "None"
    return comment

# Get a list of exon numbers for each transcript
def exons_labels(root, trans_name):
    """ Returns a list of exon labels """
    # build a string for each specific transcript name to find correct child
    find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/exon"
    # get exon child for a transcript
    exons_labels_dic = root.findall(find_str)
    # store exon label values as a list
    ex_list = []
    for k in exons_labels_dic:
            ex_list.append(k.attrib["label"])
    return ex_list

# Get the coordinates of all exons for each transcript
def exons_coord(root, trans_name):
     """ Returns a list of exon coordinates """
     # build a string for each specific transcript name to find correct child
     find_str = "./fixed_annotation/transcript/" + "[@name=" + "'" + trans_name + "'" + "]/exon/coordinates"
     # get all attributes in the first coordinate child in exon parent
     exon_coords = root.find(find_str).attrib
     return exon_coords

# Get the build coordinates
def build_coord(root):
    ''' Returns a dictionary of the attributes from the mapping_span tag  '''
    # extract build info present in xml file
    all_build = root.findall("./updatable_annotation/annotation_set/[@type='lrg']/mapping")
    # store build coordinates in mapping_span tag for each build in a dictionary
    builds = {}
    for i in all_build:
        # key is build name, and value is a dictory of attributes (i.e start, stop coordinates)
        builds[i.get("coord_system")] = i.find("./mapping_span").attrib
    return builds

# Get the build difference information
def build_diff(root, build_num):
    ''' Returns a dictionary of the differences between the genome builds from the diffs tag '''
    # build a string for each specific build name to find correct child
    find_string = "./updatable_annotation/annotation_set/[@type='lrg']/mapping/[@coord_system=" + "'" + str(build_num) +  "'" + "]/mapping_span/diff"
    # store data given in xml under the diff tag for each build
    difference = root.findall(find_string)
    return difference

# Get transcript names
def transcripts(root):
    ''' Returns a list of the transcripts in the LRG file '''
    num_of_t = list()
    # get attributes for each occurance of transcript tag in xml file
    t_list = root.findall("./fixed_annotation/transcript")
    # then store the name each of these transcripts in a list
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
