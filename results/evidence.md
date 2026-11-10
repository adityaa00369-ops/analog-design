# 1.8 V LTspice screenshots

Each link opens the original full-resolution PNG with its cursor and schematic visible. Captures are grouped by run, then ordered by operating point, AC, and transient. The source filename records which upload was used. These are historical runs. The controlled A1/A2 decks use a grounded bulk and have separate verification status.

## Draft14 · 1.8 V · original coupling capacitors

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

## Draft6 · 1.8 V · earlier capacitor trials

| Capture | What to inspect | Original upload |
|---|---|---|
| [01](screenshots/draft6/01-schematic.png) | Schematic overview | `Screenshot 2026-04-02 162906(1).png` |
| [02](screenshots/draft6/02-op-earlier.png) | Operating point, earlier capacitor trial | `Screenshot 2026-04-02 163049(1).png` |
| [03](screenshots/draft6/03-op-revised.png) | Operating point, 123 nF input and 1 µF output capacitors | `Screenshot 2026-04-02 163638(1).png` |
| [04](screenshots/draft6/04-ac-earlier.png) | AC cursor at 205.152 Hz, earlier capacitor trial | `Screenshot 2026-04-02 163152(1).png` |
| [05](screenshots/draft6/05-ac-revised.png) | AC cursor at 101.836 Hz, revised capacitor trial | `Screenshot 2026-04-02 163731(1).png` |
| [06](screenshots/draft6/06-tran-drain-current.png) | Drain resistor current | `Screenshot 2026-04-02 163317(1).png` |
| [07](screenshots/draft6/07-tran-drain-voltage.png) | Drain voltage | `Screenshot 2026-04-02 163412(1).png` |

## Reading the AC cursors

Draft14 has a 19.640244 dB midband reference. The 190.694 Hz cursor reads 16.356329 dB, a drop of about 3.28 dB. This cursor lies close to the lower half-power crossing. The exact half-power level is approximately 16.630 dB. The earlier Draft6 captures document capacitor trials at the same 1.8 V supply.

## Related captures

- [Historical Python sizing terminal](screenshots/python-sizing.png)
- [Original gm/ID plot with the transit-frequency scaling issue discussed in the design notes](screenshots/gmid-ft-original.png)
