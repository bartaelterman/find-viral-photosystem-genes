data/ntinput.nsq: data/input.fasta
	/usr/local/ncbi/blast/bin/makeblastdb -in data/input.fasta -input_type fasta -dbtype nucl -out ntinput
	mv ./ntinput.n* data/

clean:
	rm data/ntinput.n*
