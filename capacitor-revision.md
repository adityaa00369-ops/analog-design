# Why I changed the coupling capacitors

## 1. One amplifier, two capacitor versions

The supply is 1.8 V in both versions. The transistor size and resistors stay the same. Only the input and output coupling capacitors change.

| Part | Version 1: first calculation | Version 2: revised calculation |
|---|---:|---:|
| Input coupling capacitor CG | 24.7 nF | 123 nF |
| Output coupling capacitor CD | 140.1 nF | 1 µF |
| Source bypass capacitor CS | 22.10 µF | 22.10 µF |
| RD / RS / RL | 1.4 kΩ / 218 Ω / 10 kΩ | Same |
| Gate divider | 182 kΩ and 100 kΩ | Same |
| MOS hand size W / L | 93.6 µm / 0.36 µm | Same |

The goal was a lower cutoff near 100 Hz. The first version gave a cutoff around 200 Hz in simulation. The revised version moved it toward 100 Hz. Both versions belong in the project: the first result explains why the design was changed.

## 2. Why the DC calculation stays the same

A capacitor stores charge: $Q=CV$. Its current is

$$i_C=C\frac{dv_C}{dt}.$$

At DC steady state, voltage does not change. Therefore $dv_C/dt=0$ and $i_C=0$. An ideal capacitor acts as an open circuit in the DC calculation.

Changing only CG and CD does not change the final DC current or node voltages. It changes stored charge and the time needed to reach a repeating waveform. The same DC analysis applies to both versions, provided all other values and connections are identical.

## 3. Why the AC calculation changes

Frequency means cycles per second. For a sine wave, the size of capacitor impedance is

$$|Z_C|=\frac{1}{2\pi fC}.$$

At the same frequency, a larger capacitor has a smaller impedance. A series coupling capacitor then loses less of the signal across itself. More of the low-frequency signal reaches the next node.

The main reason for the change was to reduce loss near 100 Hz. Startup also changes, but larger capacitors do not automatically make startup faster or better.

## 4. Derive the first input capacitor

The supply is AC ground. The two gate resistors appear in parallel:

$$R_G=\frac{182000\times100000}{182000+100000}=64539\ \Omega.$$

For an ideal input voltage source and negligible gate current,

$$\frac{v_g}{v_{in}}=\frac{R_G}{R_G+1/(sC_G)}
=\frac{sR_GC_G}{1+sR_GC_G}.$$

Here $s=j2\pi f$ when calculating sine-wave response. The input network's corner is

$$f_G=\frac{1}{2\pi R_GC_G}.$$

Setting this individual corner to 100 Hz gives

$$C_G=\frac{1}{2\pi(64539)(100)}=24.66\text{ nF}\approx24.7\text{ nF}.$$

This is the input network's corner, not the whole amplifier's cutoff.

## 5. Derive the first output capacitor

For an isolated output-network estimate, treat the source as AC ground. Use the approximate hand-model output resistance $r_o=42.74$ kΩ from the worked notes:

$$R_{left}=R_D\parallel r_o
=\frac{1400\times42740}{1400+42740}\approx1356\ \Omega.$$

The output capacitor sees the sum of the resistance on its two sides:

$$R_{eq,D}=R_{left}+R_L\approx11356\ \Omega.$$

Setting this individual corner to 100 Hz gives

$$C_D\approx\frac{1}{2\pi(11356)(100)}\approx140.2\text{ nF}.$$

This is close to the chosen 140.1 nF. The small difference depends on the output resistance and rounding used. This calculation explains the value; it is not an exact reconstruction of every original notebook substitution.

## 6. Why the whole amplifier did not cut off at 100 Hz

At its own corner, one high-pass network passes $1/\sqrt2=0.7071$ of the signal amplitude. This is a loss of 3.0103 dB.

If two independent high-pass networks both have a 100 Hz corner, their combined amplitude at 100 Hz is

$$0.7071\times0.7071=0.5,$$

and their combined gain change is

$$20\log_{10}(0.5)=-6.02\text{ dB}.$$

This example shows the problem: each network uses part of the allowed signal loss. The source-bypass network also affects our amplifier. The full circuit can reach a total loss of 3 dB at a higher frequency than either coupling network alone.

Our circuit has interacting networks. We therefore solve the complete node equations in the [worked notes](design-calculations.md), rather than adding corner frequencies and calling the sum exact.

## 7. Why use 123 nF for the revised input?

With this value,

$$f_G=\frac{1}{2\pi(64539)(123\times10^{-9})}=20.05\text{ Hz}.$$

The input corner is now about five times below the 100 Hz target. The amplitude ratio is

$$|H_G(f)|=\frac{1}{\sqrt{1+(f_G/f)^2}}.$$

The positive loss in dB is

$$L_G=10\log_{10}[1+(f_G/f)^2].$$

At 100 Hz,

$$L_G=10\log_{10}[1+(20.05/100)^2]\approx0.171\text{ dB}.$$

So the input network loses only about 0.17 dB at the target frequency.

We can also work backward from an allowed loss $L_G$:

$$f_G=f_{target}\sqrt{10^{L_G/10}-1},$$

$$C_G=\frac{1}{2\pi R_Gf_G}.$$

An allowed loss near 0.17 dB at 100 Hz leads to about 123 nF. The allowed loss is a design choice; the capacitor follows from the equation.

This is a clear mathematical reason for the revised value. The original notes should be checked before claiming that this exact loss allowance was the rule used at the time.

## 8. Why use 1 µF for the revised output?

Using the same isolated resistance estimate,

$$f_D\approx\frac{1}{2\pi(11356)(1\times10^{-6})}=14.0\text{ Hz}.$$

At 100 Hz the isolated output-network loss is

$$L_D\approx10\log_{10}[1+(14/100)^2]=0.084\text{ dB}.$$

The two isolated coupling losses now total about

$$0.171+0.084=0.255\text{ dB}.$$

They use only a small part of the total 3 dB loss allowance. The unchanged source-bypass network now has more influence on the lower cutoff. The complete matrix still decides the actual combined result.

There is no single compulsory pair of capacitor values. Other pairs can meet an allowed-loss target. We must also consider capacitor size and settling time. The selected values reduce coupling loss enough that making them much larger gives less benefit near 100 Hz.

## 9. What happens to gain?

| Quantity | Effect of increasing only CG and CD |
|---|---|
| Final DC current and voltages | Stay the same for ideal capacitors |
| Gain near the low-frequency edge | Increases because coupling loss is smaller |
| Midband gain | Approximately unchanged |
| Upper cutoff | Usually changes little if coupling capacitors already act as shorts there |
| Startup | Changes; some decay terms can last longer |

At midband, with the source approximately at AC ground,

$$A_M\approx-g_m(R_D\parallel R_L\parallel r_o).$$

The minus sign means the output is inverted. CG and CD do not appear in this approximation because they already pass the AC signal with little voltage drop.

## 10. Why startup can become slower

For a simple RC network, $\tau=RC$. One time constant is the time for a natural decay term to fall to $e^{-1}=36.8\%$ of its starting value.

Input network:

$$\tau_{G1}=64539(24.7\times10^{-9})=1.594\text{ ms},$$
$$\tau_{G2}=64539(123\times10^{-9})=7.938\text{ ms}.$$

Isolated output estimate:

$$\tau_{D1}=11356(140.1\times10^{-9})\approx1.591\text{ ms},$$
$$\tau_{D2}=11356(1\times10^{-6})\approx11.36\text{ ms}.$$

Larger capacitors improve low-frequency transmission but store more charge for the same voltage. Their interaction with the resistances can make some startup terms decay more slowly.

The complete output is

$$v_o(t)=V_{pk}\cos(\omega t+\phi)+\sum_k A_ke^{p_kt}.$$

The first part is the final repeating signal. The other terms come from the initial capacitor voltages. Changing capacitors changes both the poles $p_k$ and the initial-condition coefficients $A_k$. Early peaks can change in different ways; do not judge steady-state gain from the first peak.

At five time constants, $e^{-5}=0.00674$: 0.674% of that individual decay term remains. For the whole circuit, use its actual poles and check the sum of the remaining terms.

## 11. Compare calculations and evidence honestly

| Quantity | Version 1 | Version 2 |
|---|---:|---:|
| Simplified-model midband gain | 19.45 dB | 19.45 dB |
| Simplified-model lower cutoff | 183.98 Hz | 83.13 Hz |
| Historical AC evidence | Cursor at 190.694 Hz is near the lower crossing | Cursor at 101.836 Hz is near the lower crossing |
| Author's description of cutoff | Around 200 Hz | Around 100 Hz; reported hand result about 102 Hz |
| Hand-model 1 kHz output, 2 mV peak input | 37.06 mV peak-to-peak | 37.42 mV peak-to-peak |
| Slowest hand-model time constant | About 1.84 ms | About 11.39 ms |

The [Python code](scripts/analyze.py) evaluates the hand-model equations for both capacitor sets. These are predictions, not new BSIM simulations. The exact 102 Hz hand substitution still needs to be added. The displayed AC cursors are near cutoff; use the midband gain from each same run to measure its exact half-power crossing.

The original Draft6 file has an unconnected bulk terminal. Both versions must use the same defined bulk connection before we make a final physical comparison. Grounding the bulk is a separate correction, not part of the capacitor experiment. Keep the original evidence and label any corrected reruns clearly.

## 12. The reason for the change, in simple words

The first capacitors each caused noticeable signal loss near 100 Hz. Together with the source network, they made the whole amplifier lose too much signal there. I increased the input and output coupling capacitors to reduce that loss. The lower cutoff moved toward the target. The midband gain stayed nearly the same. The trade-off is larger capacitors and potentially longer startup settling.
