# Repeat the selected 1.8 V run

The selected circuit uses VDD = 1.8 V, RG1 = 182 kΩ, RG2 = 100 kΩ, RD = 1.4 kΩ, RS = 218 Ω, RL = 10 kΩ, CG = 123 nF, CD = 1 µF and CS = 22.10 µF. The hand sizing gives L = 0.36 µm and W = 93.6 µm; check the actual instance values in the original schematic.

The original ASC/netlist for this selected run and its `tsmc081.lib` model file have not been supplied here. Other circuit versions and unverified replacement netlists have been removed. A screenshot is not a complete model file.

When the original files are available:

1. Check all four MOS terminals, dimensions and model name against the intended circuit.
2. Run `.op`; save node voltages, supply current, gm, gds and device capacitance data.
3. Run an AC sweep beginning below 100 Hz. Plot output/input voltage. Record the midband gain and both half-power crossings. Extend the sweep beyond 1 GHz as supported by the model to find the upper crossing.
4. Run the 2 mV peak, 1 kHz input for 100 ms, with a maximum step near 2 µs. Save early cycles and late cycles. Compare the late amplitude and phase with AC analysis at 1 kHz.
5. Record model temperature, source resistance, load capacitance and initial-condition settings. Use the same circuit for every comparison.

Changing a bulk connection or device dimensions creates a new run. Do not label it as the old screenshot result.
