data/viralGenomes.nsq: data/viralGenomes.fas
	makeblastdb -in data/viralGenomes.fas -input_type fasta -dbtype nucl -out viralGenomes 
	mv viralGenomes.n* data/

output/viral-photos-tblastx.xml: data/viralGenomes.nsq
	mkdir output
	../01-blast-search/scripts/runblast.py tblastx data/photosynthesis_genes.fas data/viralGenomes output/viral-photos-tblastx.xml

clean:
	rm -rf output
	rm data/viralGenomes.n*
