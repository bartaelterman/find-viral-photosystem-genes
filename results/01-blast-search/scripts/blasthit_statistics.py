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
    hsps_counter = 0
    for rec in blastrecords:
	for alignment in rec.alignments:
	    hsps = alignment.hsps
	    alignments.append(alignment)
	    alignment_title = alignment.title
	    if not alignment_title in hittitles:
		hittitles.append(alignment_title)
	    for hsp in hsps:
		hsps_counter += 1
    return [hittitles, alignments, hsps_counter]

def main():
    infile = parseArguments()
    resulthandle = open(infile)
    blastrecords = NCBIXML.parse(resulthandle)
    allHitTitles, allAlignments, hsps_counter = getHitTitlesAndAlignments(blastrecords)
    print "Number of hits: ", len(allAlignments)
    print "Number of hit sequences: ", len(allHitTitles)
    print "Number of hsps: ", hsps_counter

main()
