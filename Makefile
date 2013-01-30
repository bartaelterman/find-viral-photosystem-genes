data/ntinput.nsq: data/input.fasta
	makeblastdb -in data/input.fasta -input_type fasta -dbtype nucl -out ntinput
	mv ./ntinput.n* data/

clean:
	rm data/ntinput.n*

all: data/ntinput.nsq
