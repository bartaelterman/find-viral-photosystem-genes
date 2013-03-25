from Bio import SeqIO
import re

class SequenceFetcher():
    def readSequences(self, infilename):
	self.fasta = SeqIO.FastaIO.FastaIterator(file(infilename))

    def fetchWithIDMatch(self, pattern):
        matchingSequences = []
	for record in self.fasta:
	    if re.search(pattern, record.description):
		matchingSequences.append(record)
        return matchingSequences
