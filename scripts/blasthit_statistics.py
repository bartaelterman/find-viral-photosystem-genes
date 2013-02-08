#!/usr/bin/python
from Bio.Blast import NCBIXML
import sys

def parseArguments():
    if len(sys.argv) != 2:
	print "usage: ./blasthit_statistics.py <blasthits_xml_file>"
	sys.exit(-1)
    infile = sys.argv[1]
    return infile

def getHitTitlesAndAlignments(blastrecords):
    hittitles = []
    alignments = []
    for rec in blastrecords:
	for alignment in rec.alignments:
	    alignments.append(alignment)
	    alignment_title = alignment.title
	    if not alignment_title in hittitles:
		hittitles.append(alignment_title)
    return [hittitles, alignments]

def main():
    infile = parseArguments()
    resulthandle = open(infile)
    blastrecords = NCBIXML.parse(resulthandle)
    allHitTitles, allAlignments = getHitTitlesAndAlignments(blastrecords)
    print "Number of hits: ", len(allAlignments)
    print "Number of hit sequences: ", len(allHitTitles)

main()
