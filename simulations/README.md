# 1.8 V simulation setup

The A1 and A2 netlists differ only in the input and output coupling capacitances and their title. Both tie the NMOS bulk to ground for an explicit shared-substrate configuration. The supplied Draft14 log flagged a floating node. A rerun with grounded bulk may give different results from the archived screenshots.

Put your copy of the original model card in this folder as `tsmc081.lib`. The model is a separate dependency. Open either netlist in LTspice. The decks enable AC by default. To run DC or transient, comment out the active analysis and enable the desired one. Plot `V(out)/V(in)` for AC. The load voltage is `V(out)`. Use each run's own midband reference for its band edges.

The output screenshots in this project are from historical runs. These prepared decks still need LTspice verification.

The archived `draft14-historical.asc` preserves the original wiring and settings with a portable model include. It is provided for traceability.

## Schematic and log files

| Run | Portable LTspice schematic | Supplied source and log |
|---|---|---|
| Draft14, 1.8 V | [draft14-historical.asc](draft14-historical.asc) | [Original ASC](historical-originals/Draft14.asc) · [Original log](historical-originals/Draft14.log) |
| Draft6, 1.8 V | Screenshot evidence | [Draft6 captures](../results/evidence.md#draft6--18-v--earlier-capacitor-trials) |

The portable copies use `.include "tsmc081.lib"`. The archived originals preserve the Windows paths. The historical logs flag a floating n007 and zero source and drain perimeters. The prepared A1/A2 netlists use a defined bulk connection.

The 180 nm model card itself was unavailable in the supplied files. To reproduce the LTspice runs, place the exact `tsmc081.lib` next to the portable schematics and netlists. The Python analysis can run with its documented analytical parameters.
