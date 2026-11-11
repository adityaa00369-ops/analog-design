# Full screenshots for the two 1.8 V versions

Every image is kept at its original size, without cropping. Read DC first, then AC, then transient. These are historical runs. They do not show a verified bulk-grounded rerun.

## Version 1: CG 24.7 nF, CD 140.1 nF, CS 22.10 µF


| Capture | What to inspect | Original upload |
|---|---|---|
| [01](screenshots/draft14/01-op.png) | Operating point with n007 highlighted | `image(20261105-180235).png` |
| [02](screenshots/draft14/02-op-alternate.png) | Operating point and schematic | `d3ddaaf3-5c50-4e0f-8084-e00fbfb3f817.png` |
| [03](screenshots/draft14/03-ac-midband.png) | AC midband at 31.6228 kHz | `image.png` |
| [04](screenshots/draft14/04-ac-low-frequency.png) | AC cursor at 190.694 Hz | `image(1).png` |
| [05](screenshots/draft14/05-tran-input.png) | Input V(n005) | `image(2).png` |
| [06](screenshots/draft14/06-tran-gate-early.png) | Gate V(n006), early cursor | `image(5).png` |
| [07](screenshots/draft14/07-tran-gate-second-cycle.png) | Gate V(n006), second-cycle cursor | `image(4).png` |
| [08](screenshots/draft14/08-tran-gate-later.png) | Gate V(n006), 5 ms cursor | `image(3).png` |
| [09](screenshots/draft14/09-tran-drain-early.png) | Drain V(n003), first peak | `image(6).png` |
| [10](screenshots/draft14/10-tran-drain-later.png) | Drain V(n003), later cursor | `image(7).png` |
| [11](screenshots/draft14/11-tran-source-initial.png) | Source V(n008), initial level | `image(10).png` |
| [12](screenshots/draft14/12-tran-source-early.png) | Source V(n008), early minimum | `image(20261105-175856).png` |
| [13](screenshots/draft14/13-tran-source-middle.png) | Source V(n008), 4.24 ms cursor | `image(20261105-180042).png` |
| [14](screenshots/draft14/14-tran-source-later.png) | Source V(n008), 8.23 ms cursor | `image(20261105-180003).png` |
| [15](screenshots/draft14/15-tran-load-first-peak.png) | Load V(n004), first peak | `image(8).png` |
| [16](screenshots/draft14/16-tran-load-later.png) | Load V(n004), later cursor | `image(9).png` |


## Version 2: CG 123 nF, CD 1 µF, CS 22.10 µF

| Step | Full screenshot | What to read |
|---|---|---|
| 1. DC | [Operating point](screenshots/draft6/03-op-revised.png) | Drain current, supply current and node voltages |
| 2. AC | [Lower-frequency response](screenshots/draft6/05-ac-revised.png) | Cursor at 101.83585 Hz and 16.472597 dB |

A transient screenshot confirmed to use Version 2 is still needed for a direct startup comparison. Do not use Version 1's transient as Version 2 evidence.

## How to compare the cursors

Version 1 has a 19.640244 dB midband reference. Its 190.694 Hz cursor reads 16.356329 dB: a drop of about 3.28 dB. Version 2's cursor is also near the lower crossing. To measure exactly, subtract 3.0103 dB from the midband gain of the same run and find that level.

[Read why the capacitors changed](../capacitor-revision.md). The later high-frequency screenshots supplied in the discussion show a Version 2 cursor near 1.93 GHz. Confirm its same-run midband reference and bulk connection before treating it as a final upper-cutoff result.
