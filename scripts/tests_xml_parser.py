#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:31:09 2017

@author: HelenaSpiewak
"""

from xml_parser import *
import unittest


class loadTestCase(unittest.TestCase):
    """Test for loading in xml file"""
    
    def test_load_file(self):
        """Does correct test LRG return a root with two children?"""
        self.assertIs(len(load_file('/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml')), 2)
    
    def test_load_non_LRG_file(self):
        """ Does LRG file with wrong file name cause exit? """
        with self.assertRaises(SystemExit):
            load_file('/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/test_xml/L_1008.xml')
    
    def test_load_non_xml_file(self):
        """ Does non xml file name cause error? """
        with self.assertRaises(AssertionError):
            load_file('/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/test_xml/L.xl')

class genomic_seq_TestCase(unittest.TestCase):
    """Test for genomic_seq function in xml_parser.py`."""

    def test_is_string_genomic_seq(self):
        """Does test LRG xml return a string?"""
        self.assertIsInstance(genomic_seq(ET.parse('/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml').getroot()), str)
    
class finding_coord_TestCase(unittest.TestCase):
    """ Tests for extracting coding region coordinates """
    
    def test_int_find_coding_coordinate(self):
        """ Tests whether variables and be converted into int """
        self.assertIsInstance(find_coding_coordinate(ET.parse('/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml').getroot(), "t1"), tuple) 

class test_trans(unittest.TestCase):
    """ Test for function related to different transcripts in xml_parser.xml """
    
    def test_coding_region(self):
        """ Test that coding region returns str """
        self.assertIsInstance(coding_region(ET.parse('/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml').getroot(), "t1"), str)

    def test_transcipt_comments(self):
        """ Test that comments returned """
        self.assertIsInstance(transcript_comment(ET.parse('/Users/HelenaSpiewak/Programming_STP_Y2/parser_task/data/LRG_public_xml_files/LRG_1.xml').getroot(), "t1"), str)
        
if __name__ == '__main__':
    unittest.main()