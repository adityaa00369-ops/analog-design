# 1.8 V common-source NMOS amplifier

This project follows one amplifier through two capacitor versions. I used hand calculations and LTspice to study DC bias, voltage gain, frequency response and startup.

The goals were about 20 dB gain, a lower cutoff near 100 Hz, operation through 100 kHz and DC power below 1 mW with a 10 kΩ load.

## Why there are two versions

The first capacitor values gave a lower cutoff around 200 Hz. I increased the coupling capacitors to reduce signal loss near 100 Hz. This moved the lower cutoff toward 100 Hz. The larger capacitors can also make startup slower.

| Part | Version 1 | Version 2 |
|---|---:|---:|
| Input capacitor CG | 24.7 nF | 123 nF |
| Output capacitor CD | 140.1 nF | 1 µF |
| Source capacitor CS | 22.10 µF | 22.10 µF |
| Supply, resistors and transistor size | Same 1.8 V amplifier | Same |

The DC calculation is common to both versions because ideal capacitors carry no steady DC current. The AC and startup calculations are different.

## Read in this order

1. [Design targets, assumptions, transistor sizing and DC calculations](design-calculations.md).
2. [Why I changed the capacitors: small steps, equations and comparison](capacitor-revision.md).
3. [Frequency response, matrix equations and startup derivation](design-calculations.md#6-what-the-three-frequencies-mean). The numerical AC example in that file uses Version 2.
4. [Original handwritten notes in topic order](notes/README.md).
5. [Full simulation screenshots in order](results/evidence.md).
6. [Simulation files and the bulk-connection check](simulations/README.md).

## What the results show

Both historical operating-point screenshots show about 457.264 µA drain current. Total supply power is about 0.835 mW. Midband gain is about 19.6 dB. The capacitor revision improves low-frequency transmission; it does not create extra midband gain.

The author reports a hand-calculated lower cutoff near 102 Hz for Version 2. This is **fL, not transistor transit frequency fT**, and it is not attributed to Python. The separate simplified model gives 83.13 Hz for Version 2 and 183.98 Hz for Version 1. These differences are stated openly. The complete 102 Hz hand substitution still needs to be added.

The original uploaded Draft6 schematic has an unconnected bulk terminal. Correcting that is a separate task. Historical screenshots are kept as original evidence, not presented as verified results of a corrected circuit.

## Python calculation

[Open the code](scripts/analyze.py) · [Read the numerical output](results/analytical-values.txt)

```bash
python -m pip install -r requirements.txt
python scripts/analyze.py
```

The code evaluates the hand-model equations for both capacitor versions. It does not run the BSIM model. No generated design graphs are included.
