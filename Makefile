data/ntinput.00.nsq: data/input.fasta
	makeblastdb -in data/input.fasta -input_type fasta -dbtype nucl -out ntinput
	mv ./ntinput* data/

test/out.xlm: data/ntinput.00.nsq
	./scripts/runblast.py blastn data/psaA.fasta data/ntinput test/out.xml

clean:
	rm data/ntinput.*

all: data/ntinput.00.nsq
