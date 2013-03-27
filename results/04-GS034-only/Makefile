# Description of the analysis:

# The dependency of the rule `all` is always the last line of this analysis.
# That way, running `make all` will run the entire analysis.

# 1: Fetch only the assemblies from GS034
#	rule: data/GS034.fas

# 2: Create a blastable database of the input fasta file (data/GS-034.fas)
#	rule: data/blastdb_created

# 3: Run tBLASTx with the query (`psaA.fasta`) on the dataset
#	rule: output/psaA_in_GOS_tblastx.xml

# 4: Fetch the GOS assembly sequences that contain psaA.
#	rule: output/GOS_assemblies_containing_psaA.fas

# 5: Create a blastable database containing the GOS assemblies that contain psaA
#	rule: output/blastdb_2_created

# 6: run tBLASTx with nrdB as query on the GOS assemblies that contain psaA
#	rule: output/GOS_psaA_nrdB_hits.xml

# 7: Fetch GOS assembly sequences that contain both psaA and nrdB
#	rule: output/GOS_psaA_nrdB_hits.fas

# ===================================

data/GS034.fas: data/GOS_assembly.fas
	echo -e "Fetching GS034 sequences....\n-------\n"
	../02-ViralRefseq-search/scripts/fetchsequences_wrap.py data/GOS_assembly.fas GS034 > data/GS034.fas

data/blastdb_created: data/GS034.fas
	echo -e "Creating a GS034 blastable database....\n-------\n"
	makeblastdb -in data/GS034.fas -input_type fasta -dbtype nucl -out GS034
	mv ./GS034* data/
	touch data/blastdb_created

output/psaA_in_GOS_tblastx.xml: data/blastdb_created data/psaA.fas
	echo -e "Searching for similarity between GS034 and psaA....\n-------\n"
	../01-blast-search/scripts/runblast.py tblastx data/psaA.fas data/GS034 output/psaA_in_GOS_tblastx.xml

output/GOS_assemblies_containing_psaA.fas: output/psaA_in_GOS_tblastx.xml
	echo -e "Fetching sequences of GS034 assemblies containing psaA....\n-------\n"
	../01-blast-search/scripts/fetchBlastSequences.py hit output/psaA_in_GOS_tblastx.xml ./data/GS034.fas output/GOS_assemblies_containing_psaA.fas

data/blastdb_2_created: output/GOS_assemblies_containing_psaA.fas
	echo -e "Creating a new blastable database with the GS034 assemblies containing psaA....\n-------\n"
	makeblastdb -in output/GOS_assemblies_containing_psaA.fas -input_type fasta -dbtype nucl -out GOS_psaA
	mv ./GOS_psaA* data/
	touch data/blastdb_2_created

output/GOS_psaA_nrdB_hits.xml: data/blastdb_2_created data/nrdB.fas
	echo -e "Searching for similarity between psaA containing GS034 assemblies and nrdB....\n-------\n"
	../01-blast-search/scripts/runblast.py tblastx data/nrdB.fas data/GOS_psaA output/GOS_psaA_nrdB_hits.xml

output/GOS_psaA_nrdB_hits.fas: output/GOS_psaA_nrdB_hits.xml
	echo -e "Fetching sequences of GS034 assemblies containing both psaA and nrdB....\n-------\n"
	../01-blast-search/scripts/fetchBlastSequences.py hit output/GOS_psaA_nrdB_hits.xml output/GOS_assemblies_containing_psaA.fas output/GOS_psaA_nrdB_hits.fas

clean:
	rm data/GS034.*
	rm data/blastdb_created
	rm output/psaA_in_GOS_tblastx.xml
	rm output/GOS_assemblies_containing_psaA.fas
	rm data/blastdb_2_created
	rm output/GOS_psaA_nrdB_hits.xml
	rm output/GOS_psaA_nrdB_hits.fas

all: output/GOS_psaA_nrdB_hits.fas
