* Copy /home/croberts/CompChem/LigandMDTemplate/ to a folder in your home directory:
  $ cp -r /home/croberts/CompChem/LigandMDTemplate/ ./
  $ cd LigandMDTemplate

* Use AMBER's ANTECHAMBER program to interpret your ligand MOL2 file:
  $ antechamber -i Ligand.mol2 -fi mol2 -o Ligand.prepc -fo prepc

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
  > source leaprc.water.tip3p
  > source leaprc.gaff
  > loadamberprep Ligand.prepc
  > loadamberparams Ligand.frcmod
  > pdb = loadpdb Ligand.pdb
  > check pdb
  > solvatebox pdb TIP3PBOX 15 0.8
  > saveamberparm pdb SYSTEM.prmtop SYSTEM.rst7
  > savepdb pdb SYSTEM.pdb
  > saveoff pdb LEAP.off
  > quit

* We can skip the first two minimizations, and just
*   modify 2.Minall.namd with our periodic bounds:
* Use nano or other text editor to change DIMX, DIMY, DIMZ, CX, CY, CZ
*   to match the output of the PeriodicParams.py script
  $ PeriodicParams.py SYSTEM.rst7

* Now we can start our simulation, in this case we can skip a few minimizations:
  $ namd2 2.MinAll.namd > 2.log
  $ namd2 3.MD_EqWater.namd > 3.log
  etc.
