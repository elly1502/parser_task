# parser_task

The parser_task directory contains three files: run.py, xml_parser.py and tests_xml_parser.py

run.py calls functions defined in xml_parser.py to do the following:
  1. Loads the xml_file
  2. Prints the number of transcripts
  3. Prints each transcript in relation to LRG sequence and any comments related to the sequence
  4. Prints the build information within the LRG file including: reference co-ordinates of the builds and any differences between the builds

The test_xml_parser.py performs unit tests on the functions in the xml_parser.py to ensure that each function is returning the correct type

### Example use
Input: python run.py ../data/LRG_public_xml_files/LRG_13.xml
Output to console:
****** XML Parser for Locus Reference Genomic (LRG) files (v1) ******

~~~~~~~~~~~~~~~~~~~~

~~ TRANSCRIPT DATA ~~

The LRG file ../data/LRG_public_xml_files/LRG_13.xml has the following 2 transcript(s):
t1, t2

The coding region for 't1' is:
ATGGGCTTCC.....TTCAAGCCTGA

Comments for transcript 't1':
None
~~~~~~~~~~~~~~~~~~~~

The coding region for 't2' is:
ATGGGCTTC.....AATGCCAACTAA

Comments for transcript 't2':
None
~~~~~~~~~~~~~~~~~~~~

~~ BUILD DIFFERENCE DATA ~~

In build 'GRCh37.p13'
Locus maps to coordinates: start '42576' and end '55193'.
Sequence differences for build 'GRCh37.p13':
Type	Ref_coord	Orig_base	LRG_base	LRG_coord
'mismatch'	'14991539'	'A'	'G'	'7294'

In build 'GRCh38.p7'
Locus maps to coordinates: start '14964669' and end '14977286'.
Sequence differences for build 'GRCh38.p7':
No sequence differences to report.

~~~~~~~~~~~~~~~~~~~~
