# 1.8 V common-source amplifier — worked design notes

Read Sections 1–8 in order. They show the design choices, calculations, and simulation results. Links lead to the matching [handwritten notes](notes/README.md). Some notebook values have been corrected in the typed notes.

## 1. What I wanted to build

I wanted an inverting voltage amplifier for small analog signals. I used a single NMOS, a resistor at the drain, a resistor at the source, and a 10 kΩ load. My study targets were about 20 dB midband gain, a lower −3 dB frequency near 100 Hz, operation through 100 kHz, and a 1 mW DC supply budget. The 1.8 V supply and 10 kΩ load are study choices. A 2 mV peak, 1 kHz input tests the small-signal behavior. This project studies the circuit in simulation. The large coupling and bypass capacitors are external parts.

The input coupling capacitor lets the signal reach the gate while the gate divider sets DC bias. The source resistor feeds back a change in drain current at DC. The source capacitor reduces that feedback in the passband. The output capacitor passes the AC drain signal to the load and isolates the load from the DC drain voltage.

### Assumptions and result labels

| Item | Meaning in these notes |
|---|---|
| Design choice | A study target, bias choice, or selected component value |
| Hand model | Square-law current equation with an estimated λ, then a small-signal calculation |
| Historical LTspice | Results from the earlier screenshots, circuit files, and logs |
| Controlled LTspice decks | New simulation files with the bulk connected to ground. These files still need to be run. |
| NMOS model | CMOSN BSIM3 v3.1 Level 49, with a nominal temperature of 27 °C. LTspice needs the original model file. |
| Hand threshold | 0.3662 V card parameter plus the historical script’s assumed 40 mV offset. The 40 mV is an assumption in the earlier code. It has not been checked against the model at this bias. |
| Hand mobility and CLM | μₙCₒₓ ≈ 230.5 µA/V² and λ = 0.05 V⁻¹. λ is an estimate. |
| Low-frequency matrix | Ideal input source and ideal R/C components. Includes finite output conductance. Leaves out small-signal body effect and the internal transistor capacitances. |
| Initial state | The recorded cosine input starts at +2 mV. For the calculated startup, the circuit starts from the DC solution with that source value and zero changes in the other node voltages. |

## 2. Start from gain and power

[Specifications and sizing notes, pages 10–15](notes/README.md#design-targets-and-transistor-sizing)

20 dB means a voltage gain magnitude of 10 because 20 log₁₀(10) = 20 dB.

In the original sizing, I used $I_D\approx 1\,\mathrm{mW}/1.8\,\mathrm V=556\,\mu\mathrm A$. To check the whole budget, add the current in the gate divider:

$$I_{\rm div}=\frac{1.8}{182000+100000}=6.383\,\mu\mathrm A.$$

$$I_{D,\max}=\frac{1\,\mathrm{mW}}{1.8\,\mathrm V}-I_{\rm div}=549.17\,\mu\mathrm A.$$

The earlier sizing target was 556 µA. At 556 µA plus the divider, power would be 1.012 mW. The earlier LTspice run draws less current and stays below 1 mW.

## 3. Work backward from gm/ID to device size

[Sizing notes, pages 10–15](notes/README.md#design-targets-and-transistor-sizing) · [Original width calculation](notes/original-pages/15-width.jpg)

I selected $g_m/I_D=15\,\mathrm{V^{-1}}$ and $L=0.36\,\mu\mathrm m$. These are design choices. The earlier Python calculation used a simple device equation. A sweep with the BSIM model is still needed to check the operating region and find the best bias for a stated goal.

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

The original Python sizing omitted the factor 1.045 and gave approximately 97.6 µm. The handwritten calculation included it and Draft14 uses 93.6 µm. The current divided by W/L at this target is $556/260=2.138\,\mu\mathrm A$.

## 4. Derive the resistors and solve the actual DC bias

[Small-signal foundations, pages 01–09](notes/README.md#circuit-and-small-signal-foundations) · [DC bias notes, pages 16–18](notes/README.md#resistor-selection-and-dc-operating-point)

At midband the source is nearly at AC ground. KCL at the drain gives
$g_m v_g + v_d(1/R_D+1/R_L+g_{ds})=0$.
The combined load needed for a gain of 10 is $10/(8.34\,\mathrm{mS})=1.199\,\mathrm{k\Omega}$.
With the original approximate $r_o=1/(\lambda I_D)\approx36\,\mathrm{k\Omega}$, solve
$1/R_D=1/(1.199\,\mathrm{k\Omega})-1/R_L-1/r_o$.
This gives about 1.42 kΩ. The installed value is 1.4 kΩ.

The original voltage choice sets $V_{DS}=0.9$ V. Then
$R_S=(1.8-0.9)/(556\,\mu\mathrm A)-1.4\,\mathrm{k\Omega}\approx219\,\Omega$,
close to the installed 218 Ω. The calculated $V_S$ is about 121 mV.
Using the assumed threshold, the gate target is approximately
$0.4062+0.1333+0.1212=0.6607$ V. For a 100 kΩ lower resistor, that target would require about 172 kΩ above it. The installed 182 kΩ instead gives

$$V_G=1.8\frac{100}{182+100}=0.638298\,\mathrm V.$$

Use the installed values to predict what the actual circuit will do. The capacitors are open at DC. The gate current is close to zero. KVL gives

$$V_S=218I_D,\qquad V_D=1.8-1400I_D,\qquad V_{DS}=1.8-1618I_D.$$

Substitute into the hand current equation, with current in amperes:

$$I_D=0.029965(0.638298-218I_D-0.4062)^2[1+0.05(1.8-1618I_D)].$$

Solve on the branch where $V_{GS}>V_T$. This gives 491.44 µA. Then $V_{OV}=0.12496$ V and $V_{DS}=1.00485$ V. Here $V_{DS}>V_{OV}$, so the result fits the saturation condition used in the hand model. Taking the current derivatives gives

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

Python gives 491.44 µA from the hand-model equation. This is 7.5% above the earlier LTspice result of 457.264 µA. The LTspice current is 17.8% below the original 556 µA target. The log reports a floating n007. Check the fourth MOS terminal and rerun the circuit to understand the difference. Use the simulated $g_m$ to calculate the BSIM $g_m/I_D$.

[Python code for these calculations](scripts/analyze.py)

## 5. Correct the device transit-frequency estimate

The original Python calculation used $g_m\approx8.33$ mS and a width of about 97.6 µm. It estimated $C_{gs}\approx277.5$ fF and $C_{gd}\approx80$ fF. Add both capacitances to estimate $C_{gg}$.

$$C_{gg}\approx C_{gs}+C_{gd}.$$

Let $J_L=I_D/(W/L)$ be the current divided by W/L. Let $c_{gg}=C_{gg}/W$ be the gate capacitance per unit width. Since $I_D/W=J_L/L$,

$$f_T\approx\frac{g_m}{2\pi C_{gg}}
=\frac{(g_m/I_D)J_L}{2\pi L c_{gg}}.$$

The Python code gives **3.705 GHz** at the chosen $g_m/I_D=15\,\mathrm{V^{-1}}$. This is a hand-model estimate. The earlier 4.78 GHz value used only $C_{gs}$ in the denominator.

[Open the Python code used for the estimate](scripts/analyze.py)

To check $f_T$ with the BSIM model, use a separate AC current-gain test. Hold the drain, source, and bulk at AC ground. Find the frequency where the magnitude of output current divided by input current reaches one.

At fixed $L$, the square-law equation gives $J_L\propto(g_m/I_D)^{-2}$. At the same drain current, a higher $g_m/I_D$ then needs a wider device. The larger gate capacitance lowers the estimated $f_T$. A sweep with the BSIM model is needed to check this trade-off over a wider range of bias.

## 6. Capacitors and the combined AC response

[Capacitor notes, pages 19–22](notes/README.md#capacitor-sizing-and-frequency-response)

| Part | A1 original | A2 revised |
|---|---:|---:|
| Input coupling $C_G$ | 24.7 nF | 123 nF |
| Output coupling $C_D$ | 140.1 nF | 1 µF |
| Source bypass $C_S$ | 22.10 µF | 22.10 µF |

At the gate, $R_G=182\,\mathrm{k\Omega}\parallel100\,\mathrm{k\Omega}=64.54\,\mathrm{k\Omega}$. The ideal-source input corner is $1/(2\pi R_GC_G)$. In A1 it is 99.8 Hz, so it already uses almost the full −3 dB allowance at 100 Hz. In A2 it is about 20.0 Hz.

To estimate the output coupling corner by itself with the source AC grounded, the resistance across the series capacitor is $(R_D\parallel r_o)+R_L$, about 11.36 kΩ. The individual corner is approximately 100 Hz for A1 and 14 Hz for A2. The parallel combination $R_D\parallel r_o\parallel R_L$ is the midband load for gain, while the series sum is the resistance seen across the output capacitor under this approximation.

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

Write $G_X=1/R_X$, use node order gate, drain, source, load, and use $s$ for complex frequency. This low-frequency hand model leaves out the internal transistor capacitances. Each row is the sum of currents leaving its node:

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

The transistor conductance term uses $v_d-v_s$. For a higher-frequency calculation, add $C_{gd}$ directly between gate and drain, $C_{gs}$ between gate and source, and the junction capacitances between their actual terminals. A capacitor between two nodes adds $+C$ to both diagonal entries of the capacitance matrix and $-C$ to both off-diagonal entries. For a grounded bulk, the channel body term is $g_{mb}(0-v_s)$ and enters the drain and source rows with opposite signs. If the bulk is floating, add a node equation for it. A checked high-frequency result needs the device capacitances and junction dimensions from the actual simulation.

For the reduced matrix $G+sC$, the poles are the finite roots of $\det(G+sC)=0$. Solving the node equations gives

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

A1's 190.694 Hz cursor is 3.284 dB below its 19.640 dB reference, so it is close to and below the exact −3.010 dB crossing. A2's 101.84 Hz cursor is also near the crossing. The earlier A2 screenshot shows the capacitor values and the response. The A2 simulation file was made using A1 and those capacitor values. Run both files with the same bulk connection to check whether they meet the 100 Hz target.

Python gives **83.13 Hz** for the A2 lower cutoff. The value near **102 Hz** comes from the earlier LTspice screenshot. This is the amplifier lower cutoff, $f_L$. The transistor transit-frequency estimate, $f_T$, is about **3.705 GHz**.

[Python code](scripts/analyze.py) · [LTspice capture near 102 Hz](results/screenshots/draft6/05-ac-revised.png)

## 7. Transient calculation and initial conditions

[Transient notes, pages 23–38](notes/README.md#startup-and-signal-flow-from-input-to-load)

The 90° source phase produces $v_{in}=V_m\cos(\omega t)$, with $V_m=2$ mV and $\omega=2\pi(1000)$. The DC solution starts with that source at +2 mV, so the input *change* relative to the initial solution is $V_m[\cos(\omega t)-1]$. The DC supply and gate-divider bias are already present. The initial voltages across the capacitors set how the signal starts.

### First solve the gate by itself

$\tau_G=R_GC_G=1.594$ ms for A1. Its transfer function is $s\tau_G/(1+s\tau_G)$. At 1 kHz it gives 1.990 mV peak and a 5.70° lead. Write the gate voltage as

$$V_G(t)=0.638298+0.001990\cos(\omega t+5.70^\circ)+Ae^{-t/\tau_G}.$$

Since the simulated gate begins at its bias, the periodic and natural terms cancel at zero. Hence $A=-1.990\cos(5.70^\circ)\,\mathrm{mV}\approx-1.980$ mV. At 5 ms the result is about 640.19 mV. The cursor reads 640.1901 mV. At $5\tau_G\approx7.97$ ms, about 13 µV of this gate startup term remains.

### Then solve the load using all three modes

Multiply the matrix transfer function by the Laplace transform of the change in the input voltage:

$$V_o(s)=H(s)V_m\left(\frac{s}{s^2+\omega^2}-\frac1s\right).$$

The poles at $\pm j\omega$ give the periodic sine wave. Each real circuit pole $p_k$ gives a term $A_ke^{p_kt}$. Multiply by $s-p_k$ and evaluate at $p_k$:

$$
A_k=
\frac{Kp_k^2(p_k-z)}{\prod_{j\ne k}(p_k-p_j)}
\left(\frac{-V_m\omega^2}{p_k(p_k^2+\omega^2)}\right).
$$

| Case | Exponential coefficients in mV, using the pole order above | Steady load waveform in mV |
|---|---|---|
| A1 | +4781.94, −5201.94, +437.94 | $18.531\cos(\omega t-165.43^\circ)$ |
| A2 | +17.925, +11.789, −11.077 | $18.711\cos(\omega t-174.90^\circ)$ |

The large individual A1 coefficients come from the closely spaced poles. They cancel strongly. At time zero their sum cancels the periodic output, and the calculated load starts at 0 V. Use the full values from the Python code. Rounding these large terms can give the wrong sum.

The first few cycles include extra exponential terms. These terms come from the starting capacitor voltages and decrease with time. For a single exponential, five time constants leave 0.67% of that term. Here the slowest time constants are about 1.84 ms for A1 and 11.39 ms for A2. Five times those values gives about 9.2 ms and 57 ms. With several exponential terms, check the total remaining error against the error limit you choose. A 100 ms run leaves time to measure later cycles for both versions.

A1's historical load trace gives about 38 mV peak-to-peak in later cycles and a first positive peak near 25.5 mV. The hand model predicts 37.06 mV peak-to-peak for the periodic part. Use the two extrema of a later cycle to measure gain. The early peak includes the startup response.

## 8. Verification and interpretation

[LTspice evidence and cursor readings](results/evidence.md)

The earlier 1.8 V circuit gives nearly 20 dB gain and uses about 0.835 mW. Increasing both coupling capacitors improves the low-frequency response while the midband gain is approximately unchanged. The larger output capacitor also makes one startup term decay more slowly in the hand model. Both the calculation and the earlier LTspice plots show a lower cutoff with larger coupling capacitors. The exact values differ.

Run the A1 and A2 files with the same bulk connection to ground. Record DC node voltages and supply current, actual MOS $g_m$ and $g_{ds}$ if available, midband gain, both −3 dB edges if captured, gain at 100 Hz and 100 kHz, and the last five cycles of the 1 kHz transient. Label these as new runs because changing the bulk connection can change the DC bias and AC response. The earlier model information says its noise values came from another process. Noise, layout, process corners, and hardware tests still need separate work.
