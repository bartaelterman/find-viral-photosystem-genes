#!/usr/bin/python
import sys
import datetime

if len(sys.argv) != 5:
    print "usage: runblast.py blastn/tblastx <infasta> <blastdb> <outfile>"
    print "    This program will run blastn or tblastx"
    print "    and return the results in xml."
    sys.exit(-1)

program, infas, blastdb, outfile = sys.argv[1:5]

print "starting program at: ", datetime.datetime.now()
if program == "blastn":
    from Bio.Blast.Applications import NcbiblastnCommandline
    e_value = 0.001
    blast_cline = NcbiblastnCommandline(query=infas, db=blastdb, evalue=e_value, outfmt=5, out=outfile)
elif program == "tblastx":
    from Bio.Blast.Applications import NcbitblastxCommandline
    e_value = 10 ** -20
    blast_cline = NcbitblastxCommandline(query=infas, db=blastdb, evalue=e_value, outfmt=5, out=outfile)
else:
    print "unknown program given: ", program
    print "should be 'blastn' or 'tblastx'"
    sys.exit(-1)
stdin, stdout = blast_cline()

print "program ended successfully at: ", datetime.datetime.now()
