# 1.8 V common-source NMOS amplifier in 180 nm CMOS

I designed this amplifier to study gain, DC bias, frequency response, and the first few cycles after a signal starts. I used hand calculations, Python, and LTspice.

The target was about 20 dB gain, a lower cutoff near 100 Hz, operation through 100 kHz, and less than 1 mW of DC power. The load is 10 kΩ.

Draft14 is the main 1.8 V design. Draft6 shows earlier tests at the same supply voltage. A1 and A2 use different input and output coupling capacitors.

## Where the values come from

Python solves the hand-model equations for drain current and estimates the transistor transit frequency. The results depend on the assumptions written in the notes.

| Value | Result | Source |
|---|---:|---|
| Original drain-current target | About 556 µA | 1 mW divided by 1.8 V, before adding the bias-divider current |
| Drain current from the hand model | 491.44 µA | Python calculation |
| Transistor transit frequency, fT | About 3.705 GHz | Python estimate at the chosen gm/ID of 15 V⁻¹ |
| A2 lower cutoff, fL | 83.13 Hz | hand calculation and spice simulation results |
| A2 lower cutoff, fL | About 102 Hz | Earlier LTspice screenshot |
| Draft14 drain current | 457.264 µA | LTspice operating point |
| Draft14 total DC power | About 0.835 mW | 1.8 V multiplied by the LTspice supply current |
| Draft14 midband gain | 19.64 dB | LTspice AC analysis |

The value near 102 Hz describes where the amplifier gain falls at low frequency. The transistor transit frequency describes the device's current-gain speed.

[Open the Python code](scripts/analyze.py) · [Read the Python results](results/analytical-values.txt) · [See the 102 Hz LTspice capture](results/screenshots/draft6/05-ac-revised.png)

## Read the work in this order

1. [Design targets and assumptions](design-calculations.md#1-what-i-wanted-to-build).
2. [Gain and power](design-calculations.md#2-start-from-gain-and-power).
3. [Choose gm/ID and calculate the transistor width](design-calculations.md#3-work-backward-from-gmid-to-device-size).
4. [Calculate the resistors and DC voltages](design-calculations.md#4-derive-the-resistors-and-solve-the-actual-dc-bias).
5. [Calculate the transistor transit frequency](design-calculations.md#5-correct-the-device-transit-frequency-estimate).
6. [Calculate the capacitors, gain, and cutoff](design-calculations.md#6-capacitors-and-the-combined-ac-response).
7. [Explain the first few signal cycles](design-calculations.md#7-transient-calculation-and-initial-conditions).
8. [Compare the calculations with LTspice](design-calculations.md#8-verification-and-interpretation).

[Read the handwritten notes](notes/README.md) · [Open the full LTspice screenshots](results/evidence.md) · [Open the simulation files](simulations/README.md)

![Draft14 circuit and DC operating point](results/screenshots/draft14/01-op.png)

## Run the Python code

Install the packages and run the calculation.

```bash
python -m pip install -r requirements.txt
python scripts/analyze.py
```

The code prints the DC values, gain, lower cutoff, poles, startup terms, and transit-frequency estimate.

The LTspice files need your original `tsmc081.lib` model file. The A1/A2 files use a grounded bulk. They still need to be checked in LTspice.
