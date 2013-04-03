#!/usr/bin/python
import sys
from Bio.Blast import NCBIXML

###########################################################
# input: BLAST xml output
# output: tsv-file
# output-column 1: query sequence definition
# output-column 2: hit sequence definition
# output-column 3: query start
# output-column 4: query end
# output-column 5: hit start
# output-column 6: hit end
# output-column 7: reverse complement
# output-column 8: e-value
# output-column 9: bitscore
# output-column 10: similarity
###########################################################

def blastresults2tabformat(outputfile):
    resultHandle = open(outputfile)
    blastRecords = NCBIXML.parse(resultHandle)
    print "\t".join(["query", "hit", "query-start", "query-end", "hit-start", "hit-end", "rev-comp", "e-value", "bitsore", "similarity"]) + "\n"
    for blastrecord in blastRecords:
	query = blastrecord.query
	if len(blastrecord.alignments) > 0:
	    for alignment in blastrecord.alignments:
		hit = alignment.title
		for hsp in alignment.hsps:
		    query_start = str(hsp.query_start)
		    query_end= str(hsp.query_end)
		    hit_start = str(hsp.sbjct_start)
		    hit_end= str(hsp.sbjct_end)
		    rev_comp = "dunnow"
		    expect = str(hsp.expect)
		    bits = str(hsp.bits)
		    similarity = str(float(hsp.positives) / hsp.align_length)
		    print "\t".join([query, hit, query_start, query_end, hit_start, hit_end, rev_comp, expect, bits, similarity]) + "\n"

def main():
    blastresultsfile = sys.argv[1]
#    printBlastResults(blastresultsfile)
#    showFirstBlastResult(blastresultsfile)
    blastresults2tabformat(blastresultsfile)

if len(sys.argv) != 2:
    print "usage: ./parsexmlblast.py <blastresultsfile>\n"
    print "    Make sure the blastresultsfile is in xml.\n"
    sys.exit(-1)

main()
