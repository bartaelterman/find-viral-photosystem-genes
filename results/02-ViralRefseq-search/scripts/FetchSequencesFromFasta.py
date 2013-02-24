from Bio import SeqIO
import re

class SequenceFetcher():
    def readSequences(self, infilename):
        self.records = list(SeqIO.parse(infilename, "fasta"))

    def fetchWithIDMatch(self, pattern):
        matchingSequences = []
	for record in self.records:
	    if re.search(pattern, record.id):
		matchingSequences.append(record)
        return matchingSequences
