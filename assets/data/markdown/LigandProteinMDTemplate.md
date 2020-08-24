* Copy /home/croberts/CompChem/LigandMDTemplate/ to a folder in your **home** directory:
  $ cp -r /home/croberts/CompChem/LigandProteinMDTemplate/ ./

* Use "egrep" to extract the protein lines that start with ATOM, TER, or END:
     $ egrep "^ATOM|^TER|^END" YOURPROTEIN.pdb > Protein_ATOMS.pdb

* Use "tleap" to add hydrogen atoms and clean up structure.
     $ tleap
     > source leaprc.protein.ff14SB
     > pdb = loadpdb Protein_ATOMS.pdb
     > savepdb pdb Protein.pdb
     > quit

* Use VMD to open both your Protein.pdb and Ligand.mol2 file,
*   and position the ligand where you'd like it to start in the simulation
* Use the Mouse->Move->Fragment menu item, then use your mouse to move the ligand
* Save the ligand in its new position as Ligand_inPosition.mol2
* Unfortunately, VMD ignores double/triple bonds, so open your Ligand_inPosition.mol2
*   and fix any bonds

* Use AMBER's ANTECHAMBER program to interpret your ligand MOL2 file:
  $ antechamber -i Ligand_inPosition.mol2 -fi mol2 -o Ligand.prepc -fo prepc

* Many new files are created after antechamber is done.
* The most important are Ligand.prepc and NEWPDB.PDB
* Let's rename NEWPDB.PDB to match our naming scheme:
  $ mv NEWPDB.PDB Ligand.pdb

* Now we'll use AMBER's PARMCHK program to make sure we have all parameters for our ligand:
  $ parmchk -i Ligand.prepc -f prepc -o Ligand.frcmod

* We should now examine the resulting file, Ligand.frcmod
* If there are any lines that prompt us for parameters, we must fill them in manually.

* Now we can use AMBER's TLEAP to create a parameterized system:
  $ tleap
  > source leaprc.protein.ff14SB
  > source leaprc.water.tip3p
  > source leaprc.gaff
  > host = loadpdb Protein.pdb
  > check host
  > loadamberprep Ligand.prepc
  > loadamberparams Ligand.frcmod
  > guest = loadpdb Ligand.pdb
  > check guest
  > system = combine {host guest}
  > addions system Na+ 0
  > solvatebox system TIP3PBOX 15 0.8
  > saveamberparm system SYSTEM.prmtop SYSTEM.rst7
  > savepdb system SYSTEM.pdb
  > saveoff system LEAP.off
  > quit

* Use nano or other text editor to change DIMX, DIMY, DIMZ, CX, CY, CZ
* to match the output of the PeriodicParams.py script
  $ PeriodicParams.py SYSTEM.pdb

* Create fixed atom files USING NEW SCRIPTS!
  $ CreateFixedBackbonePDB.py SYSTEM.pdb
  $ CreateMobileWaterPDB.py SYSTEM.pdb

* Now we can start our simulation, in this case we can skip a few minimizations:
  $ namd2 0.MinWater.namd > 0.log
  $ namd2 1.MinNotBackbone.namd > 1.log
  $ namd2 2.MinAll.namd > 2.log
  $ namd2 3.MD_EqWater.namd > 3.log
  etc.
