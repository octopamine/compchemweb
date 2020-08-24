HOWTO: Run AutoDock VINA

* Copy /home/croberts/CompChem/VINATemplate/ to a folder in your home directory:
  $ cp -r /home/croberts/CompChem/VINATemplate/ ./NewTemplateFolderName
  $ cd NewTemplateFolderName

* Use "egrep" to extract the protein lines that start with ATOM, TER, or END from the first chain only:
     $ egrep "^ATOM .* A .*|^HETATM .* A .*|^TER|^END" XXXX.pdb > PROTEIN.pdb

* We must convert out PDB and MOL2 files to PDBQT files in preparation for docking.
     $ prepare_receptor4.py -r PROTEIN.pdb    # this creates a new pdbqt, PROTEIN.pdbqt
     $ prepare_ligand4.py -l LIGAND.mol2      # this creates a new pdbqt, LIGAND.pdbqt

* Edit the AutoDockVina.conf file:
     + Make sure your "receptor" and "ligand" lines match your PDBQT files from the previous step.
     + The center coordinates should be approximately in the binding site, and the
       size dimensions should cover the whole binding site. All measurements are in Angstroms.
     + If you don't know where your binding site is, you can dock your ligand to the whole protein.
       Measure the center of the protein using the command: pdb_measure_center.py PROTEIN.pdb
       Measure the dimensions of the protein using the command: pdb_measure_dimensions.py PROTEIN.pdb
     + Change the seed value to any random number.
     + "exhaustiveness" is a qualitative measure of how many cycles of docking search should be performed.
       A value between 8 and 20 is reasonable, but higher numbers require more time.
     + "num_modes" is the maximum number of docked conformations to output.

* Run AutoDockVina
     $ vina --config AutoDockVina.conf
