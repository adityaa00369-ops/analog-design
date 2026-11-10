# 1.8 V simulation setup

A1 and A2 use different input and output coupling capacitors. Both connect the NMOS bulk to ground. The earlier Draft14 log reports a floating node. Connecting the bulk to ground can change the results.

Put your copy of the original model card in this folder as `tsmc081.lib`. This file is needed to run the simulations. Open either netlist in LTspice. The files are set to run AC analysis. To run DC or transient, comment out the active analysis and enable the desired one. Plot `V(out)/V(in)` for AC. The load voltage is `V(out)`. Find the −3 dB points using the midband gain from the same run.

The screenshots show earlier runs. The A1/A2 files still need to be run in LTspice.

The file `draft14-historical.asc` contains the original circuit. Its model path points to `tsmc081.lib` in this folder.

## Schematic and log files

| Run | Portable LTspice schematic | Supplied source and log |
|---|---|---|
| Draft14, 1.8 V | [draft14-historical.asc](draft14-historical.asc) | [Original ASC](historical-originals/Draft14.asc) · [Original log](historical-originals/Draft14.log) |
| Draft6, 1.8 V | Screenshot evidence | [Draft6 captures](../results/evidence.md#draft6--18-v--earlier-capacitor-trials) |

The portable copies use `.include "tsmc081.lib"`. The archived originals preserve the Windows paths. The earlier log reports a floating n007 and zero source and drain perimeters. The A1/A2 files connect the bulk to ground.

The supplied files did not include the 180 nm model card. To run LTspice, place your original `tsmc081.lib` next to the portable schematics and netlists. The Python code uses the hand-model values listed in the design notes.
