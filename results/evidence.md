# Historical LTspice screenshots

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

## Draft9 · 2 V · separate historical run

| Capture | What to inspect | Original upload |
|---|---|---|
| [01](screenshots/draft9/01-op.png) | Operating point and schematic | `e611c5ef-4321-45f0-9258-0d06a5dce7d9.png` |
| [02](screenshots/draft9/02-ac-midband.png) | AC midband at 1 MHz | `c6e2ba66-72ca-4750-9ad7-9ad6d91c684c.png` |
| [03](screenshots/draft9/03-ac-near-cutoff.png) | End-to-end AC cursor at 293.370 Hz | `d4c3311d-e2dd-4ccb-a2cf-97091652ceb4.png` |
| [04](screenshots/draft9/04-ac-lower-frequency.png) | End-to-end AC cursor at 177.828 Hz | `dc6c4d72-80b0-4ffd-963e-4f33a1e0282d.png` |
| [05](screenshots/draft9/05-ac-input-to-gate.png) | Gate-to-input ratio | `db703003-64c6-43a9-8fcf-1f90fa2a3e91.png` |
| [06](screenshots/draft9/06-ac-gate-to-load.png) | Load-to-gate ratio | `98471ecb-7aa1-4b95-98f2-2a33c5735de7.png` |
| [07](screenshots/draft9/07-ac-gate-to-vgs.png) | Vgs divided by gate voltage | `1a4584b3-2379-4e84-9a12-aaa29b737065.png` |
| [08](screenshots/draft9/08-ac-vgs-to-drain.png) | Drain voltage divided by Vgs | `3a79596f-41cb-489f-a895-e75f9582b7dd.png` |
| [09](screenshots/draft9/09-tran-input.png) | Input V(n005) | `f49524de-300d-48f1-88cc-4eaa948168c7.png` |
| [10](screenshots/draft9/10-tran-gate.png) | Gate V(n006) | `00b126b7-2d93-497a-882d-d2488cb7eefc.png` |
| [11](screenshots/draft9/11-tran-drain.png) | Drain V(n003) | `2bbe141a-f891-42d6-8b40-5605f2dc0c35.png` |
| [12](screenshots/draft9/12-tran-source.png) | Source V(n008) | `5aba19aa-d3e0-4f31-bfb8-27d076eaff80.png` |
| [13](screenshots/draft9/13-tran-load.png) | Load V(n004) | `af56d6c0-845b-474d-9e2b-cfeb180dd43a.png` |

## Reading the AC cursors

Draft14 has a 19.640244 dB midband reference. The 190.694 Hz cursor reads 16.356329 dB, a drop of about 3.28 dB. Draft9 has a 16.57248 dB midband reference. The 293.370 Hz cursor reads 13.507423 dB, a drop of about 3.07 dB. Both cursor locations are close to their respective lower half-power crossings. Draft9 uses a different supply, transistor geometry, and passive values. Its results belong to a separate run.

## Related captures

- [Historical Python sizing terminal](screenshots/python-sizing.png)
- [Original gm/ID plot with the transit-frequency scaling issue discussed in the design notes](screenshots/gmid-ft-original.png)
