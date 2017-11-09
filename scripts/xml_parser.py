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

script, xml_file = argv

# sanity check path of file
print(xml_file)

# load in xml data
tree = ET.parse(xml_file)
root = tree.getroot()

# Pull out genomic sequence
def genomic_seq(root):
   
    if root[0].tag == "fixed_annotation":
        fixed = root[0]
        dna_seq = []
   
        for elem in fixed:
            if elem.tag == "sequence" and elem.text:
                dna_seq.append(elem.text)
    return dna_seq

print(genomic_seq(root))

         