# Description of the analysis:

# The dependency of the rule `all` is always the last line of this analysis.
# That way, running `make all` will run the entire analysis.

# 1: create a blastable database of your input fasta file (for me, those are GOS assemblies)
#	rule: data/ntinput.00.nsq

# 2: run tBLASTx with the query (`psaA.fasta`) on the dataset
#	rule: results/01-blast-search/output/psaA_in_GOS_tblastx.xml

# 3: run tBLASTx with the query (`psbA.fasta`) on the dataset
#	rule: results/01-blast-search/output/psbA_in_GOS_tblastx.xml

# 4: Fetch the GOS assembly sequences that contain photosynthesis genes
#	rule: results/01-blast-search/output/GOS_assemblies_containing_photo_genes.fas

# 5: run tBLASTx with query GOS_assemblies_containing_photo_genes.fas on viralGenomes.fas
#	rule: results/02-ViralRefseq-search/output/GOS_photo_hits_viral.xml

# 6: Fetch GOS assembly sequences that contain both photosynthesis and viral genes
#	rule: results/02-ViralRefseq-search/output/GOS_photo_and_viral.fas

# ===================================


data/blastdb_created: data/input.fasta
	makeblastdb -in data/input.fasta -input_type fasta -dbtype nucl -out ntinput
	mv ./ntinput* data/
	touch data/blastdb_created

results/01-blast-search/output/psaA_in_GOS_tblastx.xml: data/blastdb_created
	./results/01-blast-search/scripts/runblast.py tblastx data/photosynthesis_genes/psaA.fasta data/ntinput results/01-blast-search/output/psaA_in_GOS_tblastx.xml

results/01-blast-search/output/psbA_in_GOS_tblastx.xml: data/blastdb_created
	./results/01-blast-search/scripts/runblast.py tblastx data/photosynthesis_genes/psbA.fasta data/ntinput results/01-blast-search/output/psbA_in_GOS_tblastx.xml

results/01-blast-search/output/GOS_assemblies_containing_photo_genes.fas: results/01-blast-search/output/psaA_in_GOS_tblastx.xml results/01-blast-search/output/psbA_in_GOS_tblastx.xml
	./results/01-blast-search/scripts/fetchBlastSequences.py hit ./results/01-blast-search/output/psaA_in_GOS_tblastx.xml ./data/input.fasta ./results/01-blast-search/output/GOS_assemblies_containing_psaA.fas
	./results/01-blast-search/scripts/fetchBlastSequences.py hit ./results/01-blast-search/output/psbA_in_GOS_tblastx.xml ./data/input.fasta ./results/01-blast-search/output/GOS_assemblies_containing_psbA.fas
	cat ./results/01-blast-search/output/GOS_assemblies_containing_psaA.fas ./results/01-blast-search/output/GOS_assemblies_containing_psbA.fas > ./results/01-blast-search/output/GOS_assemblies_containing_photo_genes.fas

results/02-ViralRefseq-search/data/viralGenomes.nsq: data/viralGenomes.fas
	makeblastdb -in data/viralGenomes.fas -input_type fasta -dbtype nucl -out viralGenomes
	mv ./viralGenomes* results/02-ViralRefseq-search/data/

results/02-ViralRefseq-search/output/GOS_photo_hits_viral.xml: results/02-ViralRefseq-search/data/viralGenomes.nsq results/01-blast-search/output/GOS_assemblies_containing_photo_genes.fas
	./results/01-blast-search/scripts/runblast.py tblastx ./results/01-blast-search/output/GOS_assemblies_containing_photo_genes.fas ./results/02-ViralRefseq-search/data/viralGenomes results/02-ViralRefseq-search/output/GOS_photo_hits_viral.xml

results/02-ViralRefseq-search/output/GOS_photo_and_viral.fas: results/02-ViralRefseq-search/output/GOS_photo_hits_viral.xml
	./results/01-blast-search/scripts/fetchBlastSequences.py query results/02-ViralRefseq-search/output/GOS_photo_hits_viral.xml ./results/01-blast-search/output/GOS_assemblies_containing_photo_genes.fas results/02-ViralRefseq-search/output/GOS_photo_and_viral.fas

test/out.xml: data/blastdb_created
	./results/01-blast-search/scripts/runblast.py blastn data/psaA.fasta data/ntinput test/out.xml

clean:
	rm data/ntinput.*
	rm results/01-blast-search/output/psaA_in_GOS_tblastx.xml
	rm results/01-blast-search/output/psbA_in_GOS_tblastx.xml
	rm results/01-blast-search/output/GOS_assemblies_containing_photo_genes.fas
	rm results/02-ViralRefseq-search/data/viralGenomes.n*
	rm results/02-ViralRefseq-search/output/GOS_photo_hits_viral.xml
	rm results/02-ViralRefseq-search/output/GOS_photo_and_viral.fas

all: results/02-ViralRefseq-search/output/GOS_photo_and_viral.fas
