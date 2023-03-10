! Taken from https://github.com/HEP-FCC/FCC-config/blob/spring2021/FCCee/Generator/Pythia8/p8_ee_Z_Zbb_ecm125.cmd
Random:setSeed = on
Main:timesAllowErrors = 5          ! how many aborts before run stops
PDF:lepton = on

! 2) Settings related to output in init(), next() and stat().
Init:showChangedSettings = on      ! list changed settings
Init:showChangedParticleData = off ! list changed particle data
Next:numberCount = 100             ! print message every n events
Next:numberShowInfo = 1            ! print event information n times
Next:numberShowProcess = 1         ! print process record n times
Next:numberShowEvent = 0           ! print event record n times

Beams:idA = 11                   ! first beam, e+ = 11
Beams:idB = -11                   ! second beam, e- = -11

! Beam energy spread: 0.132% x 62.5 GeV = 0.0825 GeV
Beams:allowMomentumSpread  = on
Beams:sigmaPzA = 0.0825
Beams:sigmaPzB = 0.0825

! Vertex smearing :
Beams:allowVertexSpread = on
Beams:sigmaVertexX = 4.50e-3   !  6.4 mum / sqrt2
Beams:sigmaVertexY = 20.0E-6   !  28.3 nm / sqrt2
Beams:sigmaVertexZ = 0.30      !  0.30 mm


! 3) Hard process : ttbar pair production at 100TeV
Beams:eCM = 125  ! CM energy of collision
WeakSingleBoson:ffbar2ffbar(s:gmZ) = on

! 4) Settings for the event generation process in the Pythia8 library.
PartonLevel:ISR = on               ! initial-state radiation
PartonLevel:FSR = on               ! final-state radiation

! 5) Non-standard settings; exemplifies tuning possibilities.
23:onMode   = off
23:onIfAny  = 5
