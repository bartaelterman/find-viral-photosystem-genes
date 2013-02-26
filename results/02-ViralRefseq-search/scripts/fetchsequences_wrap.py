#!/usr/bin/python
import FetchSequencesFromFasta as f
import sys
from Bio import SeqIO
from StringIO import StringIO

shorthelpmsg = "usage: ./fetchsequences_wrap.py <fastafile> <id pattern>\n  or ./fetchsequences_wrap.py -h"
longhelpmsg = "  This script will fetch sequences from the given fastafile whose id match \
the regular expression pattern provided"

if (len(sys.argv) != 3):
    print shorthelpmsg
    if (len(sys.argv) == 2):
	if (sys.argv[1] == "-h"):
	    print longhelpmsg
    sys.exit(-1)

fasfilename, pattern = sys.argv[1:]
seqfetcher = f.SequenceFetcher()
seqfetcher.readSequences(fasfilename)
records = seqfetcher.fetchWithIDMatch(pattern)
out_handle = StringIO()
SeqIO.write(records, sys.stdout, "fasta")
#data = out_handle.getvalue()
#print data.strip()
