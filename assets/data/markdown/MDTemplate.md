* Copy /home/croberts/CompChem/MDTemplate/ to a folder in your home directory:
  $ cp -r /home/croberts/CompChem/MDTemplate/ .

* Use "egrep" to extract the protein lines that start with ATOM, TER, or END:
     $ egrep "^ATOM .* A .*|^TER|^END" 6F25.pdb > Protein.pdb

* Now we can use AMBER's TLEAP to create a parameterized system:
  $ tleap
  > source leaprc.protein.ff14SB
  > source leaprc.water.tip3p
  > system = loadpdb Protein.pdb
  > check system
  > addions system Na+ 0
  > solvatebox system TIP3PBOX 15 0.8
  > saveamberparm system SYSTEM.prmtop SYSTEM.rst7
  > savepdb system SYSTEM.pdb
  > saveoff system LEAP.off
  > quit

* Use nano or other text editor to change DIMX, DIMY, DIMZ, CX, CY, CZ
* within the file 0.MinWater.namd to match the output of the PeriodicParams.py script:
  $ PeriodicParams.py SYSTEM.rst7

* Create fixed atom files by executing these commands:
  $ CreateFixedBackbonePDB.py SYSTEM.pdb
  $ CreateMobileWaterPDB.py SYSTEM.pdb

* Now we can start our simulation, starting with minimizations, then moving on to simulalations:
  $ namd2 0.MinWater.namd > 0.log
  $ namd2 1.MinNotBackbone.namd > 1.log
  $ namd2 2.MinAll.namd > 2.log
  $ namd2 3.MD_EqWater.namd > 3.log
  $ namd2 4.MD_Eq200K.namd > 4.log
  $ namd2 5.MD_Eq250K.namd > 5.log
  $ namd2 6.MD_Eq300K.namd > 6.log
  $ namd2 7.MD_ProductionRun.namd > 7.log
