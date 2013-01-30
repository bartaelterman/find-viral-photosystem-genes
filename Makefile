data/blastdb: data
	/usr/local/ncbi/blast/bin/makeblastdb -in data/psaA.fasta -input_type fasta -dbtype nucl -out ntpsaA
	mv ./ntpsaA.n* data/
