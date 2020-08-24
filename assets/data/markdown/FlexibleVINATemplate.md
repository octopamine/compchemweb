HOWTO: Run AutoDock VINA

* Copy /home/croberts/CompChem/VINATemplate/ to a folder in your home directory:
  $ cp -r /home/croberts/CompChem/FlexibleVINATemplate/ ./NewTemplateFolderName
  $ cd NewTemplateFolderName

* Flexible docking requires an additional step relative to standard docking with VINA
* We first prepare our protein as usual, which produces our Protein.pdbqt file.
  $ prepare_receptor4.py -r Protein.pdb

* We then have to take our protein, and use a different script to prepare for flexible docking:
  $ prepare_flexreceptor4.py -r Protein.pdbqt -s Protein:A:LEU97_PHE101_VAL146_GLU220_SER221_THR252_VAL254_LEU255_LEU304_LEU318_LEU358_ILE359_LEU363_LEU388_MET425_PHE426_HIS468

* The prepare_flexreceptor4.py script takes the -r argument for your protein file, then
*   a -s argument for all of the residues/amino acids that you want to be flexible.
* Notice the format at the beginning of the definition (Protein:A:) specicies the
*   filename without the .pdbqt as well as the chain that the amino acids are on
* Notice the format for each amino acid: the three-letter amino acid name followed by its
*   residue numer from the PDB file (the 6th column)
* As you can see, the different amino acid definitions are separated by an underscore

* Two new files are created: Protein_rigid.pdbqt and Protein_flex.pdbqt
* Those are specified in the vina.conf

* Now lets prepare the ligand:
  $ prepare_ligand4.py -l D-methylphenidate.mol2

* In vina.conf, adjust the search box center and size

* Finally, run vina:
 $ vina --config vina.conf
