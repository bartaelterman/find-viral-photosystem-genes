import FetchSequencesFromFasta
import os
import unittest

class TestFetchSequences(unittest.TestCase):
    def setUp(self):
	fasta_content = ">sequence1\nAAAA\n>sequence2\nTTTT\n>sequence3\nCCCC\n>sequence4\nGGGG"
	self.fastafile = "test_fasta.fas"
	fasfile = file(self.fastafile, "w+")
	fasfile.write(fasta_content)
	fasfile.close()
	self.sequenceFetcher = FetchSequencesFromFasta.SequenceFetcher()
	self.sequenceFetcher.readSequences(self.fastafile)
	print "fixture ran"

    """
    def tearDown(self):
	os.remove(self.fastafile)
    """

    def test_fetchNoSequences(self):
	pattern = r"unknown"
	sequences = self.sequenceFetcher.fetchWithIDMatch(pattern)
	self.assertEqual(len(sequences), 0)

    def test_fetchSeq1(self):
	pattern = r"sequence1"
	sequences = self.sequenceFetcher.fetchWithIDMatch(pattern)
	self.assertEqual(len(sequences), 1)
	self.assertEqual(sequences[0].description, "sequence1")
        
    def test_fetchSeq1and2(self):
	pattern = r"1|2"
	sequences = self.sequenceFetcher.fetchWithIDMatch(pattern)
	self.assertEqual(len(sequences), 2)
	self.assertEqual(sequences[0].description, "sequence1")
	self.assertEqual(sequences[1].description, "sequence2")
        
    def test_matchAll(self):
        pattern = r"\d"
	sequences = self.sequenceFetcher.fetchWithIDMatch(pattern)
	self.assertEqual(len(sequences), 4)
	self.assertEqual(sequences[0].description, "sequence1")
	self.assertEqual(sequences[1].description, "sequence2")
	self.assertEqual(sequences[2].description, "sequence3")
	self.assertEqual(sequences[3].description, "sequence4")
