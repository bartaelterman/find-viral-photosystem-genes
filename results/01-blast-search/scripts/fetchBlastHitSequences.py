#!/usr/bin/python

from Bio.Blast import NCBIXML
import os
import sys
from Bio import SeqIO
cwd = os.path.realpath(__file__)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(cwd))))
sys.path.append(project_root + "/results/02-ViralRefseq-search/scripts/")
import FetchSequencesFromFasta

def checkarguments():
    if len(sys.argv) != 4:
	print "usage: ./fetchBlastHitSequences.py <blasthitsfile> <hitsequencesfile> <outfile>"
	sys.exit(-1)

def getBlastHitDefinitions(hitsfile):
    blast_records = NCBIXML.parse(file(hitsfile))
    definitions = []
    for record in blast_records:
	alignments = record.alignments
	for alignment in alignments:
	    definition = alignment.hit_def
	    if definition not in definitions:
		definitions.append(definition)
    return definitions

def cleanDefs(hitdefs):
    outdefs = []
    for hitdef in hitdefs:
	new_def = hitdef.replace("|", "\\|")
	outdefs.append(new_def)
    return outdefs

def createAndSearchPattern(patterns, seq_fetcher):
    pattern = "|".join(patterns)
    print "search for pattern: ", pattern
    return seq_fetcher.fetchWithIDMatch(pattern)

def getAllhitSequences(seqfile, patterns):
    seq_fetcher = FetchSequencesFromFasta.SequenceFetcher()
    seq_fetcher.readSequences(seqfile)
    maxpattern = len(patterns)
    print "maxpatterns: ", maxpattern
    i = 0
    tmppatterns = []
    sequences = []
    for pattern in patterns:
	i += 1
	tmppatterns.append(pattern)
	if i == 99:
	    sequences += createAndSearchPattern(tmppatterns, seq_fetcher)
	    i = 0
	    tmppatterns = []
    if len(tmppatterns) != 0:
	sequences += createAndSearchPattern(tmppatterns, seq_fetcher)
    return sequences

def writeToOutfile(hitseqs, outfilename):
    SeqIO.write(hitseqs, outfilename, "fasta")

def main():
    checkarguments()
    blasthitsfile, hitsequencesfile, outfilename  = sys.argv[1:]
    hitdefs = getBlastHitDefinitions(blasthitsfile)
    clean_hitdefs = cleanDefs(hitdefs)
    hitsequences = getAllhitSequences(hitsequencesfile, clean_hitdefs)
    writeToOutfile(hitsequences, outfilename)

main()
