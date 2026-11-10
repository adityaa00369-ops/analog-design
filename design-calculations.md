# 1.8 V common-source amplifier — worked design notes

Follow Sections 1–8 from specifications through simulation. Where available, links point to the matching groups in the [handwritten appendix](notes/README.md). The typed derivations incorporate corrections and additional checks, so some values differ from the draft notebook.

## 1. What I wanted to build

I wanted an inverting voltage amplifier for small analog signals. I used a single NMOS, a resistor at the drain, a resistor at the source, and a 10 kΩ load. My study targets were about 20 dB midband gain, a lower −3 dB frequency near 100 Hz, operation through 100 kHz, and a 1 mW DC supply budget. The 1.8 V supply and 10 kΩ load are study choices. A 2 mV peak, 1 kHz input tests the small-signal behavior. The large external capacitors make this a schematic-level analog fundamentals project.

The input coupling capacitor lets the signal reach the gate while the gate divider sets DC bias. The source resistor feeds back a change in drain current at DC. The source capacitor reduces that feedback in the passband. The output capacitor passes the AC drain signal to the load and isolates the load from the DC drain voltage.

### Assumptions and result labels

| Item | Meaning in these notes |
|---|---|
| Design choice | A study target, bias choice, or selected component value |
| Hand model | Saturation square law with an estimated channel-length modulation factor, followed by a linearization |
| Historical LTspice | Results read from the supplied screenshots and associated schematic or log |
| Controlled LTspice decks | New reproducible inputs with explicit bulk ground. Numerical results are pending. |
| NMOS model | Supplied CMOSN BSIM3 v3.1 Level 49 card, 27 °C nominal. The model file is a local dependency. |
| Hand threshold | 0.3662 V card parameter plus the historical script’s assumed 40 mV offset. This fixed offset is a proxy, not an extracted threshold or a body-effect derivation. |
| Hand mobility and CLM | μₙCₒₓ ≈ 230.5 µA/V² and λ = 0.05 V⁻¹. λ is an estimate. |
| Low-frequency matrix | Ideal input source and ideal R/C components. Includes finite output conductance. Neglects incremental body coupling and intrinsic capacitances. |
| Initial state | The recorded cosine input starts at +2 mV. For the calculated startup, the circuit starts from the DC solution with that source value and zero node perturbations. |

## 2. Start from gain and power

[Specifications and sizing notes, pages 10–15](notes/README.md#design-targets-and-transistor-sizing)

20 dB means a voltage gain magnitude of 10 because 20 log₁₀(10) = 20 dB.

In the original sizing, I used $I_D\approx 1\,\mathrm{mW}/1.8\,\mathrm V=556\,\mu\mathrm A$. To check the whole budget, add the current in the gate divider:

$$I_{\rm div}=\frac{1.8}{182000+100000}=6.383\,\mu\mathrm A.$$

$$I_{D,\max}=\frac{1\,\mathrm{mW}}{1.8\,\mathrm V}-I_{\rm div}=549.17\,\mu\mathrm A.$$

The historical 556 µA is the sizing target. At 556 µA plus the divider, power would be 1.012 mW. The final historical SPICE circuit draws less current and meets the total budget.

## 3. Work backward from gm/ID to device size

[Sizing notes, pages 10–15](notes/README.md#design-targets-and-transistor-sizing) · [Original width calculation](notes/original-pages/15-width.jpg)

I selected $g_m/I_D=15\,\mathrm{V^{-1}}$ and $L=0.36\,\mu\mathrm m$. These are design choices. The original Python plot explores bias sensitivity and does not establish an optimum or a BSIM operating region.

The card gives $t_{ox}=4.1$ nm and $U_0=273.8094\,\mathrm{cm^2/(V\,s)}=0.027381\,\mathrm{m^2/(V\,s)}$.

$$C_{ox}=\frac{3.9\epsilon_0}{t_{ox}}=8.422\,\mathrm{mF/m^2},\qquad
\mu_n C_{ox}\approx230.61\,\mu\mathrm{A/V^2}.$$

The notes use the rounded 230.5 value. At fixed drain voltage, differentiate the saturation current:

$$I_D=\tfrac12\mu_n C_{ox}(W/L)(V_{GS}-V_T)^2(1+\lambda V_{DS}).$$
$$g_m=\mu_n C_{ox}(W/L)(V_{GS}-V_T)(1+\lambda V_{DS}).$$

Divide the equations to cancel the common terms. This gives $g_m/I_D=2/V_{OV}$, so $V_{OV}=2/15=0.1333$ V. The target transconductance is $15(556\,\mu\mathrm A)=8.34$ mS.

Using the original $V_{DS}=0.9$ V target:

$$\frac WL=\frac{2(556\times10^{-6})}{230.5\times10^{-6}(0.1333)^2[1+0.05(0.9)]}\approx260.$$

$$W\approx260(0.36\,\mu\mathrm m)=93.6\,\mu\mathrm m.$$

The original Python sizing omitted the factor 1.045 and gave approximately 97.6 µm. The handwritten calculation included it and Draft14 uses 93.6 µm. The normalized current for this rounded geometry at the target is $556/260=2.138\,\mu\mathrm A$.

## 4. Derive the resistors and solve the actual DC bias

[Small-signal foundations, pages 01–09](notes/README.md#circuit-and-small-signal-foundations) · [DC bias notes, pages 16–18](notes/README.md#resistor-selection-and-dc-operating-point)

At midband the source is nearly at AC ground. KCL at the drain gives
$g_m v_g + v_d(1/R_D+1/R_L+g_{ds})=0$.
Thus the effective load required for gain 10 is $10/(8.34\,\mathrm{mS})=1.199\,\mathrm{k\Omega}$.
With the original approximate $r_o=1/(\lambda I_D)\approx36\,\mathrm{k\Omega}$, solve
$1/R_D=1/(1.199\,\mathrm{k\Omega})-1/R_L-1/r_o$.
This gives about 1.42 kΩ. The installed value is 1.4 kΩ.

The original headroom allocation sets $V_{DS}=0.9$ V. Then
$R_S=(1.8-0.9)/(556\,\mu\mathrm A)-1.4\,\mathrm{k\Omega}\approx219\,\Omega$,
close to the installed 218 Ω. The resulting nominal $V_S$ is about 121 mV.
With the hand threshold proxy, the gate target is approximately
$0.4062+0.1333+0.1212=0.6607$ V. For a 100 kΩ lower resistor, that target would require about 172 kΩ above it. The installed 182 kΩ instead gives

$$V_G=1.8\frac{100}{182+100}=0.638298\,\mathrm V.$$

Use the installed values to predict what the actual circuit will do. The capacitors are open at DC. The gate draws negligible current. KVL gives

$$V_S=218I_D,\qquad V_D=1.8-1400I_D,\qquad V_{DS}=1.8-1618I_D.$$

Substitute into the hand current equation, with current in amperes:

$$I_D=0.029965(0.638298-218I_D-0.4062)^2[1+0.05(1.8-1618I_D)].$$

Solve on the branch where $V_{GS}>V_T$. This gives 491.44 µA. Then $V_{OV}=0.12496$ V and $V_{DS}=1.00485$ V. The latter exceeds $V_{OV}$, consistent with the assumed saturation equation. The hand-model derivatives at that point are

$$g_m=2I_D/V_{OV}=7.865\,\mathrm{mS},\qquad
g_{ds}=\frac{\lambda I_D}{1+\lambda V_{DS}}=23.40\,\mu\mathrm S.$$

$$r_o=1/g_{ds}\approx42.74\,\mathrm{k\Omega},\qquad g_m/I_D\approx16.00\,\mathrm{V^{-1}}.$$

| Quantity | Hand model with installed parts | Historical Draft14 LTspice |
|---|---:|---:|
| Gate voltage | 0.63830 V | 0.63830 V |
| Source voltage | 0.10713 V | 0.09968 V |
| Drain voltage | 1.11198 V | 1.15983 V |
| Drain current | 491.44 µA | 457.264 µA |
| Total DC power | 0.8961 mW | 0.8346 mW |
| Midband gain magnitude | 19.45 dB | 19.64 dB at 31.62 kHz |

The hand current prediction is 7.5% above the historical LTspice result, relative to LTspice. The simulation is 17.8% below the original sizing target. These comparisons answer different questions. The LTspice log flags n007 as floating. Check the fourth MOS terminal before assigning that warning to the bulk or attributing the current mismatch to a specific effect. The actual BSIM $g_m/I_D$ requires the simulated $g_m$.

## 5. Correct the device transit-frequency estimate

For the original analytical bias, $g_m\approx8.33$ mS and the Python width is about 97.6 µm. The script used about 277.5 fF for $C_{gs}$ and about 80 fF for $C_{gd}$. For a consistent estimate use $C_{gg}\approx C_{gs}+C_{gd}$ in the curve and the marker. The original curve mixed current normalized by $W/L$ with capacitance normalized by $W$.

Let $J_L=I_D/(W/L)$ and $c_{gg}=C_{gg}/W$. Since $I_D/W=J_L/L$,

$$f_T\approx\frac{g_m}{2\pi C_{gg}}
=\frac{(g_m/I_D)J_L}{2\pi L c_{gg}}.$$

At the script's original sizing point this is approximately **3.71 GHz**, compared with 4.78 GHz from its $C_{gs}$-only marker. For the fabricated-device model, $f_T$ would be extracted in a separate short-circuit current-gain AC test with drain, source, and bulk at AC ground. The transistor's $f_T$ and the amplifier's voltage bandwidth describe different tests.

The corrected script plots square-law sensitivity over a limited range near the design. The old script stitched together an exponential and a square law and capped the displayed efficiency after computing transit frequency. The new plot uses one consistent approximation and makes no weak-inversion or optimality claim. At fixed $L$ in this approximation, $J_L\propto (g_m/I_D)^{-2}$. Higher efficiency then needs more width at the same current, and the estimated $f_T$ decreases. A BSIM sweep is needed to quantify that trade-off across inversion.

## 6. Capacitors and the combined AC response

[Capacitor notes, pages 19–22](notes/README.md#capacitor-sizing-and-frequency-response)

| Part | A1 original | A2 revised |
|---|---:|---:|
| Input coupling $C_G$ | 24.7 nF | 123 nF |
| Output coupling $C_D$ | 140.1 nF | 1 µF |
| Source bypass $C_S$ | 22.10 µF | 22.10 µF |

At the gate, $R_G=182\,\mathrm{k\Omega}\parallel100\,\mathrm{k\Omega}=64.54\,\mathrm{k\Omega}$. The ideal-source input corner is $1/(2\pi R_GC_G)$. In A1 it is 99.8 Hz, so it already uses almost the full −3 dB allowance at 100 Hz. In A2 it is about 20.0 Hz.

For the isolated output coupling estimate with the source AC grounded, the resistance across the series capacitor is $(R_D\parallel r_o)+R_L$, about 11.36 kΩ. The individual corner is approximately 100 Hz for A1 and 14 Hz for A2. The parallel combination $R_D\parallel r_o\parallel R_L$ is the midband load for gain, while the series sum is the resistance seen across the output capacitor under this approximation.

To reproduce the original coupling capacitor estimates, start with an individual corner of 100 Hz for each branch and solve for capacitance.

$$
C_G=\frac{1}{2\pi(64.54\,\mathrm{k\Omega})(100\,\mathrm{Hz})}
\approx24.66\,\mathrm{nF},\qquad
C_D=\frac{1}{2\pi(11.36\,\mathrm{k\Omega})(100\,\mathrm{Hz})}
\approx140.1\,\mathrm{nF}.
$$

At 100 Hz each of these two networks is already near its own half-power point. Even two independent half-power sections would give a combined magnitude of about 0.5, or −6 dB. The full circuit also has source degeneration, so use the combined matrix to find the actual half-power frequency.

For the bypass branch, ignoring $g_{ds}$ temporarily makes source KCL easy to see:

$$(1/R_S+sC_S)v_s=g_m(v_g-v_s).$$

Thus $v_{gs}/v_g=(s+1/R_SC_S)/(s+(1/R_S+g_m)/C_S)$. At low frequency the resistor reduces $v_{gs}$ through feedback. At higher frequency the capacitor reduces source motion. This explains the bypass pole and zero. It also explains why the bypass network alone leaves a finite gain at low frequency.

### Solve KCL at each node

Write $G_X=1/R_X$, use node order gate, drain, source, load, and use $s$ for complex frequency. At the low frequencies of interest, the intrinsic capacitances are omitted in the numerical hand model. Each row is the sum of currents leaving its node:

$$
\begin{bmatrix}
G_G+sC_G&0&0&0\\
g_m&G_D+g_{ds}+sC_D&-g_m-g_{ds}&-sC_D\\
-g_m&-g_{ds}&G_S+g_m+g_{ds}+sC_S&0\\
0&-sC_D&0&G_L+sC_D
\end{bmatrix}
\begin{bmatrix}v_g\\v_d\\v_s\\v_o\end{bmatrix}
=
\begin{bmatrix}sC_Gv_{in}\\0\\0\\0\end{bmatrix}.
$$

The transistor conductance term uses $v_d-v_s$. For a higher-frequency model, stamp $C_{gd}$ directly between gate and drain, $C_{gs}$ between gate and source, and the junction capacitances between their actual terminals. A capacitor between two nodes adds $+C$ to both diagonal entries of the capacitance matrix and $-C$ to both off-diagonal entries. For a grounded bulk, the channel body term is $g_{mb}(0-v_s)$ and enters the drain and source rows with opposite signs. An externally floating bulk requires its own node equation. The supplied evidence does not establish the needed junction geometry or small-signal values for a verified high-frequency prediction.

For the reduced matrix $G+sC$, the poles are the finite roots of $\det(G+sC)=0$. Eliminating the nodes gives

$$H(s)=K\frac{s^2(s-z)}{\prod_k(s-p_k)},\qquad
K=-\frac{g_m}{G_D+G_L+g_{ds}},\qquad z=-\frac1{R_SC_S}.$$

The two zeros at the origin come from the coupling capacitors. The bypass zero is $-207.57\,\mathrm{s^{-1}}$, or 33.04 Hz on a frequency scale. Find the combined cutoff by solving $|H(j2\pi f)|=|K|/\sqrt{2}$.

| Result | A1 | A2 |
|---|---:|---:|
| Reduced matrix poles in s⁻¹ | −638.67, −627.31, −544.45 | −554.81, −125.97, −87.81 |
| Hand combined lower cutoff | 183.98 Hz | 83.13 Hz |
| Historical LTspice lower cutoff | Near 200 Hz | Near 102 Hz from earlier screenshot |
| Hand gain at 100 Hz | 11.38 dB | 17.14 dB |
| Hand midband gain | 19.45 dB | 19.45 dB |

A1's 190.694 Hz cursor is 3.284 dB below its 19.640 dB reference, so it is close to and below the exact −3.010 dB crossing. A2's 101.84 Hz cursor is also near the crossing. The older A2 screenshot establishes the capacitor values and response, but the editable A2 schematic was reconstructed from A1 and those values. Use the new paired runs for a controlled comparison and a strict 100 Hz pass/fail.

## 7. Transient calculation and initial conditions

[Transient notes, pages 23–38](notes/README.md#startup-and-signal-flow-from-input-to-load)

The 90° source phase produces $v_{in}=V_m\cos(\omega t)$, with $V_m=2$ mV and $\omega=2\pi(1000)$. The DC solution starts with that source at +2 mV, so the input *change* relative to the initial solution is $V_m[\cos(\omega t)-1]$. The DC supply and gate-divider bias are already present. The initial voltages across the capacitors set how the signal starts.

### First solve the gate by itself

$\tau_G=R_GC_G=1.594$ ms for A1. Its transfer function is $s\tau_G/(1+s\tau_G)$. At 1 kHz it gives 1.990 mV peak and a 5.70° lead. Write the gate voltage as

$$V_G(t)=0.638298+0.001990\cos(\omega t+5.70^\circ)+Ae^{-t/\tau_G}.$$

Since the simulated gate begins at its bias, the periodic and natural terms cancel at zero. Hence $A=-1.990\cos(5.70^\circ)\,\mathrm{mV}\approx-1.980$ mV. At 5 ms the result is about 640.19 mV. The cursor reads 640.1901 mV. At $5\tau_G\approx7.97$ ms, about 13 µV of this gate startup term remains.

### Then solve the load using all three modes

Multiply the matrix transfer function by the Laplace transform of the input perturbation:

$$V_o(s)=H(s)V_m\left(\frac{s}{s^2+\omega^2}-\frac1s\right).$$

The poles at $\pm j\omega$ give the periodic sine wave. Each real circuit pole $p_k$ gives a term $A_ke^{p_kt}$. Multiply by $s-p_k$ and evaluate at $p_k$:

$$
A_k=
\frac{Kp_k^2(p_k-z)}{\prod_{j\ne k}(p_k-p_j)}
\left(\frac{-V_m\omega^2}{p_k(p_k^2+\omega^2)}\right).
$$

| Case | Modal coefficients in mV, in pole order from the previous table | Steady load waveform in mV |
|---|---|---|
| A1 | +4781.94, −5201.94, +437.94 | $18.531\cos(\omega t-165.43^\circ)$ |
| A2 | +17.925, +11.789, −11.077 | $18.711\cos(\omega t-174.90^\circ)$ |

The large individual A1 coefficients come from the closely spaced poles. They cancel strongly. At time zero their sum cancels the periodic output, and the calculated load starts at 0 V. Evaluate with full precision from the script because rounding the individual terms affects their sum.

The early cycles differ from the periodic waveform because the capacitor voltages start at their DC values and the natural modes take time to decay. For a single exponential, five time constants leave 0.67% of that term. Here the slowest modal time constants are about 1.84 ms for A1 and 11.39 ms for A2. Five times those values gives about 9.2 ms and 57 ms. For a multi-mode waveform, measure the actual residual against a stated tolerance. A 100 ms run leaves time to measure later cycles for both versions.

A1's historical load trace gives about 38 mV peak-to-peak in later cycles and a first positive peak near 25.5 mV. The hand model predicts 37.06 mV peak-to-peak for the periodic part. Use the two extrema of a later cycle to measure gain. The early peak includes the startup response.

## 8. Verification and interpretation

[LTspice evidence and cursor readings](results/evidence.md)

The historical 1.8 V circuit approaches the 20 dB target and uses about 0.835 mW. Increasing both coupling capacitors improves the low-frequency response while the midband gain is approximately unchanged. The larger output capacitor also introduces a longer time scale in the reduced model. The original plots and analytical model agree on the direction of the cutoff change. Their exact cutoffs differ.

For a controlled rerun use the provided A1 and A2 decks, with the same explicit bulk ground. Record DC node voltages and supply current, actual MOS $g_m$ and $g_{ds}$ if available, midband gain, both −3 dB edges if captured, gain at 100 Hz and 100 kHz, and the last five cycles of the 1 kHz transient. Keep these results separate from the historical runs because a bulk connection can change the bias and AC response. The current model-card noise coefficients were substituted from another process according to the card. No process-specific noise, layout, corner, or hardware results are claimed.
