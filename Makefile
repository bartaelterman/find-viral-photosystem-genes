data/ntinput.00.nsq: data/input.fasta
	makeblastdb -in data/input.fasta -input_type fasta -dbtype nucl -out ntinput
	mv ./ntinput* data/

results/01-blast-search/output/photosynthesis_in_GOS.xml: data/ntinput.00.nsq
	./results/01-blast-search/scripts/runblast.py tblastx data/photosynthesis_genes.fas data/ntinput results/01-blast-search/output/photosynthesis_in_GOS.xml

test/out.xml: data/ntinput.00.nsq
	./results/01-blast-search/scripts/runblast.py blastn data/psaA.fasta data/ntinput test/out.xml

clean:
	rm data/ntinput.*

all: data/ntinput.00.nsq
