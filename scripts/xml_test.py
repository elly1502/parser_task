#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:10:38 2017

@author: HelenaSpiewak
"""

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import glob 
from sys import argv

script, xml_file = argv

# sanity check path of file
print(xml_file)

# load in xml data
tree = ET.parse(xml_file)
print(tree)

for i in tree.iter():
    print(i)

root = tree.getroot()
print(root)
                
for elem in tree.iter():
    print(elem.tag, elem.attrib)
# check that first child of root is fixed_annotation section
if root[0].tag == "fixed_annotation":
    for element in root[0].iter():
        if element.tag == "sequence":
            print("TAG %r, attribute %r and text %r" % (element.tag, element.attrib, element.text))

# extract genomic sequence   
if root[0].tag == "fixed_annotation":
   fixed = root[0]
   
   dna_seq = []
   for elem in fixed:
       if elem.tag == "sequence" and elem.text:
           print(elem.text)
    
    
    
    
    
    
## display dna sequence
#print(dna_seq)
#for i in fixed.iter():
#    print(i.tag, i.text)
################
#for child_of_root in anno:
#    print(child_of_root.tag, child_of_root.attrib)
## refers to genomic sequence
#for i in root.iter("sequence"):
#    print(i.tag, i.text)
#    
#
#data = root.getchildren()[0].getchildren()[7].text
#print(data)
#for elem in root.iter():
#    print(elem.tag, elem.text)
## refers to tag
#fixed = root.getchildren()[0]
#test = ET.SubElement(fixed, "sequence").text
#anno = root.getchildren()[1]
#print(test)
#
#for i in .findall("sequence"):
#    seq = i.find("sequence").get()
#
###########
#    
#try:
#  from lxml import etree
#  print("running with lxml.etree")
#except ImportError:
#  try:
#    # Python 2.5
#    import xml.etree.cElementTree as etree
#    print("running with cElementTree on Python 2.5+")
#  except ImportError:
#    try:
#      # Python 2.5
#      import xml.etree.ElementTree as etree
#      print("running with ElementTree on Python 2.5+")
#    except ImportError:
#      try:
#        # normal cElementTree install
#        import cElementTree as etree
#        print("running with cElementTree")
#      except ImportError:
#        try:
#          # normal ElementTree install
#          import elementtree.ElementTree as etree
#          print("running with ElementTree")
#        except ImportError:
#          print("Failed to import ElementTree from any known place")
## creating xml        
#root = etree.Element("root")
#print(root.tag)
#
#child2 = etree.SubElement(root, "child2")
#child3 = etree.SubElement(root, "child3")
#
## look at the html made
#print(ET.tostring(root))
#
## Elements are lists
#child = root[0]
#print(child.tag)
#print(len(root))
#root.index(root[1])
#children = list(root)
#
#for child in root:
#    print(child.tag)




















