# 1.8 V common-source NMOS amplifier

This project explains one amplifier using hand calculations and LTspice. The goals are about 20 dB voltage gain, a lower cutoff near 100 Hz, operation through 100 kHz, and DC power below 1 mW with a 10 kΩ load.

Only the 1.8 V circuit with **CG = 123 nF, CD = 1 µF and CS = 22.10 µF** is used for the simulation results here.

## Read in this order

1. [Worked notes: targets, assumptions, sizing, bias, frequency response and startup](design-calculations.md).
2. [Original handwritten pages, grouped by topic](notes/README.md). The typed notes explain corrections and give the reading order.
3. [Full DC and AC screenshots](results/evidence.md).
4. [Python calculation code](scripts/analyze.py) and [its output](results/analytical-values.txt).
5. [Files still needed to repeat the LTspice run](simulations/README.md).

## Results and their sources

| Quantity | Value | Source |
|---|---:|---|
| Drain current | 457.264 µA | Selected LTspice operating point |
| Supply power | 0.8346 mW | 1.8 V × 463.647 µA from the same operating point |
| Midband voltage gain | About 19.6 dB | Selected AC plot |
| Lower cutoff reported by the author | About 102 Hz | Hand calculation; complete substitution still needs to be added |
| AC cursor near lower cutoff | 101.83585 Hz, 16.472597 dB | Selected screenshot; not an exact half-power measurement |
| Upper cutoff | Not reached in the shown 1 GHz sweep | Selected AC plot |

**102 Hz is a lower cutoff, not the transistor transit frequency fT.** It was reported as a hand result, not a Python result. The separate simplified calculation gives 83.13 Hz; the notes explain why we cannot claim an exact match yet. They also explain why gain falls at both frequency edges and why the circuit does not suddenly stop responding at fT.

![Selected circuit and DC operating point](results/screenshots/draft6/03-op-revised.png)

## Run the calculation

```bash
python -m pip install -r requirements.txt
python scripts/analyze.py
```

The code checks the written hand-model equations. It does not run the 180 nm BSIM model. Its results are estimates, not extra LTspice measurements. The original model file and original schematic for this selected run are still needed.
