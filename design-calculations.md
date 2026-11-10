# 1.8 V common-source amplifier — worked design notes

Read Sections 1–10 in order. They show the design choices, calculations, and simulation results. Links lead to the matching [handwritten notes](notes/README.md). Some notebook values have been corrected in the typed notes.

## 1. What I wanted to build

I wanted an inverting voltage amplifier for small analog signals. I used a single NMOS, a resistor at the drain, a resistor at the source, and a 10 kΩ load. My study targets were about 20 dB midband gain, a lower −3 dB frequency near 100 Hz, operation through 100 kHz, and a 1 mW DC supply budget. The 1.8 V supply and 10 kΩ load are study choices. A 2 mV peak, 1 kHz input tests the small-signal behavior. This project studies the circuit in simulation. The large coupling and bypass capacitors are external parts.

The input coupling capacitor lets the signal reach the gate while the gate divider sets DC bias. The source resistor feeds back a change in drain current at DC. The source capacitor reduces that feedback in the passband. The output capacitor passes the AC drain signal to the load and isolates the load from the DC drain voltage.

### Assumptions and result labels

| Item | Meaning in these notes |
|---|---|
| Design choice | A study target, bias choice, or selected component value |
| Hand model | Square-law current equation with an estimated λ, then a small-signal calculation |
| Historical LTspice | Results from the earlier screenshots, circuit files, and logs |
| Selected circuit | 1.8 V, CG = 123 nF, CD = 1 µF, CS = 22.10 µF. Only screenshots of this circuit are used as results. |
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

The earlier sizing work used $t_{ox}=4.1$ nm and $U_0=273.8094\,\mathrm{cm^2/(V\,s)}=0.027381\,\mathrm{m^2/(V\,s)}$.

$$C_{ox}=\frac{3.9\epsilon_0}{t_{ox}}=8.422\,\mathrm{mF/m^2},\qquad
\mu_n C_{ox}\approx230.61\,\mu\mathrm{A/V^2}.$$

The notes use the rounded 230.5 value. At fixed drain voltage, differentiate the saturation current:

$$I_D=\tfrac12\mu_n C_{ox}(W/L)(V_{GS}-V_T)^2(1+\lambda V_{DS}).$$
$$g_m=\mu_n C_{ox}(W/L)(V_{GS}-V_T)(1+\lambda V_{DS}).$$

Divide the equations to cancel the common terms. This gives $g_m/I_D=2/V_{OV}$, so $V_{OV}=2/15=0.1333$ V. The target transconductance is $15(556\,\mu\mathrm A)=8.34$ mS.

Using the original $V_{DS}=0.9$ V target:

$$\frac WL=\frac{2(556\times10^{-6})}{230.5\times10^{-6}(0.1333)^2[1+0.05(0.9)]}\approx260.$$

$$W\approx260(0.36\,\mu\mathrm m)=93.6\,\mu\mathrm m.$$

The original Python sizing omitted the factor 1.045 and gave approximately 97.6 µm. The handwritten calculation included it and the hand design uses 93.6 µm. The current divided by W/L at this target is $556/260=2.138\,\mu\mathrm A$.

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

| Quantity | Hand model with installed parts | Selected 1.8 V LTspice |
|---|---:|---:|
| Gate voltage | 0.63830 V | 0.63830 V |
| Source voltage | 0.10713 V | 0.09968 V |
| Drain voltage | 1.11198 V | 1.15983 V |
| Drain current | 491.44 µA | 457.264 µA |
| Total DC power | 0.8961 mW | 0.8346 mW |
| Midband gain magnitude | 19.45 dB | About 19.6 dB, read from the plot |

Python gives 491.44 µA from the hand-model equation. This is 7.5% above the earlier LTspice result of 457.264 µA. The LTspice current is 17.8% below the original 556 µA target. The screenshot does not establish the bulk connection. A voltage printed for n007 alone does not prove that this terminal has the intended connection. Check the original netlist before making an exact model comparison. Use the simulated $g_m$ to calculate the BSIM $g_m/I_D$.

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


## 6. What the three frequencies mean

A frequency is the number of cycles in one second. Its unit is hertz (Hz).

- **Lower cutoff, fL:** the low-frequency edge of the amplifier passband.
- **Upper cutoff, fH:** the high-frequency edge of the amplifier passband.
- **Transit frequency, fT:** a transistor test result. It is the frequency where the magnitude of its short-circuit current gain becomes one.

The amplifier does not suddenly stop at any of these frequencies. Its output usually gets smaller as frequency moves outside the passband. fT is not the same as fH. A large fT alone does not prove that the complete amplifier meets its bandwidth target.

The **approximately 102 Hz value is the author's reported hand-calculated lower cutoff**, not a Python transit-frequency result. The full substitution that gives 102 Hz has not been located in the supplied note pages. The selected LTspice cursor is at 101.83585 Hz. The separate simplified model in this repo gives 83.13 Hz. These must not be presented as an exact three-way match.

## 7. Why gain falls at low frequency

### Step 1: Understand a capacitor

Capacitor current is $i=C\,dv/dt$. A faster voltage change needs more current. For a sine wave its impedance is

$$Z_C=\frac{1}{j2\pi fC},\qquad |Z_C|=\frac{1}{2\pi fC}.$$

Here $j$ keeps track of phase. At low frequency, a series coupling capacitor has a large impedance. More signal voltage appears across it, so less reaches the next part of the circuit.

### Step 2: Calculate the input loss

The gate sees both divider resistors connected to AC ground:

$$R_G=\frac{182000(100000)}{182000+100000}=64539\ \Omega.$$

For an ideal input voltage source and negligible gate current,

$$H_G(s)=\frac{v_g}{v_{in}}=\frac{R_G}{R_G+1/(sC_G)}
=\frac{sR_GC_G}{1+sR_GC_G}.$$

With $C_G=123$ nF,

$$\tau_G=64539(123\times10^{-9})=7.938\text{ ms},$$
$$f_G=\frac{1}{2\pi\tau_G}=20.05\text{ Hz},$$
$$|H_G(j2\pi f)|=\frac{f}{\sqrt{f^2+f_G^2}}.$$

At 102 Hz this factor is about 0.981, or −0.165 dB. At 20.05 Hz it is 0.707, or −3.010 dB. This is the loss of the input network alone, not the loss of the whole amplifier.

### Step 3: Understand the output capacitor

Use $r_o=42.74$ kΩ from the hand model. With the source approximately at AC ground,

$$R_{left}=R_D\parallel r_o\approx1356\ \Omega.$$

The resistance across the output coupling capacitor is the **sum** of the resistances on its two sides:

$$\tau_D=(R_{left}+R_L)C_D=(1356+10000)(1\times10^{-6})
=11.36\text{ ms},$$
$$f_D\approx\frac{1}{2\pi\tau_D}=14.0\text{ Hz}.$$

This isolated estimate explains the output coupling loss. It does not include interaction with the source network.

### Step 4: Understand the source capacitor

The source resistor makes negative feedback: more drain current raises the source voltage, which reduces $v_{gs}$ and opposes the current change.

$$Z_S=R_S\parallel\frac{1}{sC_S}=\frac{R_S}{1+sR_SC_S}.$$

For an explanation only, neglect $r_o$ and body effect. Then

$$i_d=g_m(v_g-i_dZ_S),$$
$$i_d(1+g_mZ_S)=g_mv_g,$$
$$\frac{v_d}{v_g}\approx-g_m(R_D\parallel R_L)
\frac{1+sR_SC_S}{1+g_mR_S+sR_SC_S}.$$

At low frequency the source resistor reduces gain. At higher frequency the source capacitor provides an easier AC path to ground, so gain increases. This network has both a pole and a zero:

$$f_z=\frac{1}{2\pi R_SC_S}=33.0\text{ Hz},$$
$$f_p\approx\frac{1+g_mR_S}{2\pi R_SC_S}
=\frac{1+0.007865(218)}{2\pi(218)(22.10\times10^{-6})}
\approx89.6\text{ Hz}.$$

These are individual network estimates. Do not add them and call the sum the exact cutoff. Also, multiplying the simulated current by the chosen 15 V⁻¹ does not measure the simulated gm/ID. In note page 22, $15\times457\,\mu A=6.855$ mS; the actual simulated gm must come from the device operating-point data.

### Step 5: Solve all nodes together, without Miller

Let the unknown node voltages be gate, drain, source and output: $\mathbf v=[v_g,v_d,v_s,v_o]^T$. Set $G_G=1/R_G$, $G_D=1/R_D$, $G_S=1/R_S$, $G_L=1/R_L$. KCL means the currents leaving each node add to zero.

$$
\begin{bmatrix}
G_G+sC_G&0&0&0\\
g_m&G_D+g_{ds}+sC_D&-g_m-g_{ds}&-sC_D\\
-g_m&-g_{ds}&G_S+g_m+g_{ds}+sC_S&0\\
0&-sC_D&0&G_L+sC_D
\end{bmatrix}
\mathbf v=
\begin{bmatrix}sC_G\\0\\0\\0\end{bmatrix}v_{in}.
$$

This is the low-frequency hand model. It neglects body effect and the small internal MOS capacitances. It is not a complete BSIM model. Solve the four equations and take $H(s)=v_o/v_{in}$. Poles are roots of the denominator after any common factors are removed. Zeros are roots of the numerator.

For the stated hand-model values, the result can be written as

$$H(s)\approx-9.389\frac{s^2(s+207.56)}
{(s+554.805)(s+125.972)(s+87.807)}.$$

The numerator has two zeros at zero frequency and one at $s=-207.56$ per second. The two zeros at zero mean the gain tends to zero at DC. The three negative poles describe decaying responses, not growing ones.

For hand evaluation at any frequency, put $\omega=2\pi f$:

$$|H(j\omega)|=9.389\frac{\omega^2\sqrt{\omega^2+207.56^2}}
{\sqrt{\omega^2+554.805^2}\sqrt{\omega^2+125.972^2}\sqrt{\omega^2+87.807^2}}.$$

Then calculate $A_{dB}(f)=20\log_{10}|H(j2\pi f)|$. This shows exactly how to calculate the gain decrease within this hand model. The [Python code](scripts/analyze.py) evaluates the same equations and finds the root of

$$|H(j2\pi f_L)|=9.389/\sqrt2.$$

It gives **83.13 Hz**. This is a model result, not a measured value and not the author's reported 102 Hz hand result. We need the original 102 Hz working and actual MOS small-signal values to explain the remaining difference fully.

### Step 6: Read a −3 dB point correctly

A voltage ratio of $1/\sqrt2=0.7071$ gives

$$20\log_{10}(0.7071)=-3.0103\text{ dB}.$$

For the same resistance, power is proportional to voltage squared, so power becomes one half. Use the midband gain from the **same circuit and run**, and subtract 3.0103 dB. The selected cursor reads 16.472597 dB at 101.83585 Hz. The plotted plateau is about 19.6 dB. This is near the crossing, but the cursor alone does not establish the exact cutoff to five decimal places.

## 8. Why gain falls at high frequency

The transistor has small capacitances even when no external capacitors are fitted. These include gate–source, gate–drain and drain–bulk capacitances. At higher frequency they draw more AC current. Together with circuit resistances they change the gain and phase.

### A direct matrix calculation

For this explanation, let the source and bulk be at AC ground and the coupling capacitors be AC shorts. Let $R_{sig}$ be the source resistance, $G_{sig}=1/R_{sig}$, and $G_o=1/R_D+1/R_L+g_{ds}$. Let $C_o=C_{db}+C_L$, where $C_L$ includes any added output capacitance. KCL gives

$$\begin{bmatrix}
G_{sig}+G_G+s(C_{gs}+C_{gd})&-sC_{gd}\\
g_m-sC_{gd}&G_o+s(C_o+C_{gd})
\end{bmatrix}
\begin{bmatrix}v_g\\v_o\end{bmatrix}
=\begin{bmatrix}G_{sig}v_{in}\\0\end{bmatrix}.$$

No Miller approximation is used. Define $a=G_{sig}+G_G$, $b=C_{gs}+C_{gd}$ and $c=C_o+C_{gd}$. Expanding the determinant gives

$$D(s)=aG_o+s(ac+bG_o+g_mC_{gd})+s^2(bc-C_{gd}^2).$$

Thus

$$H(s)=\frac{-G_{sig}(g_m-sC_{gd})}{D(s)}.$$

For $D(s)=d_2s^2+d_1s+d_0$, calculate the poles from

$$p_{1,2}=\frac{-d_1\pm\sqrt{d_1^2-4d_2d_0}}{2d_2}.$$

The numerator gives a right-half-plane zero $z=g_m/C_{gd}$. A zero is not automatically a cutoff. Find fH by solving $|H(j2\pi f_H)|=|H_{mid}|/\sqrt2$ on the falling side of the response.

### The ideal voltage source in this schematic

The selected input source has no shown series resistor. In the ideal-source limit, $v_g=v_{in}$ in this high-frequency simplified model. Use

$$H(s)=\frac{sC_{gd}-g_m}{G_o+s(C_o+C_{gd})}.$$

Define $\omega_p=G_o/(C_o+C_{gd})$ and $\omega_z=g_m/C_{gd}$. Then

$$\frac{|H(j\omega)|}{|H(0)|}
=\sqrt{\frac{1+(\omega/\omega_z)^2}{1+(\omega/\omega_p)^2}}.$$

When the zero is much higher than the pole, this becomes approximately $1/\sqrt{1+(f/f_p)^2}$. The gain loss is then

$$\Delta A_{dB}=-10\log_{10}[1+(f/f_p)^2].$$

| Frequency | Gain compared with midband | Loss |
|---|---:|---:|
| 0.1 fp | 0.995 | 0.043 dB |
| fp | 0.707 | 3.010 dB |
| 10 fp | 0.0995 | 20.043 dB |

These are teaching ratios, not new LTspice results. Including the zero, the half-power equation gives

$$\omega_H=\left(\frac{1}{\omega_p^2}-\frac{2}{\omega_z^2}\right)^{-1/2},$$

provided the bracket is positive. This shows why even a pole frequency and a −3 dB frequency need not be identical.

### What can be reported for this design

The selected screenshot reaches 1 GHz. The gain is still about 18.6 dB there, above the roughly 16.6 dB half-power level. **The shown sweep therefore does not locate the upper cutoff; it supports fH greater than 1 GHz within the shown simulation.** There is no verified numerical fH hand/SPICE match to report yet.

To substitute actual numbers into the matrix, obtain gm, gds, the capacitance data at the bias point, the bulk connection, and any source/load parasitics. For a full model, keep the source and bulk nodes and use the simulator's full conductance and charge-derivative matrices. Do not treat all BSIM capacitance entries as interchangeable two-terminal capacitors.

The 3.705 GHz fT estimate in Section 5 uses the earlier analytical sizing model. It is not a measured upper cutoff. Above fT the device can still respond; its short-circuit current gain is below one under the defining test conditions.

## 9. Why the first cycles look different

A capacitor stores charge. At the start, its stored voltage may differ from the voltage required by the final repeating sine wave. The output contains a repeating part and a decaying part:

$$v_o(t)=V_{pk}\cos(\omega t+\phi)+\sum_k A_ke^{p_kt}.$$

The repeating amplitude is $V_{pk}=V_{in,pk}|H(j\omega)|$. At 1 kHz, with a 2 mV input, the selected hand model gives $V_{pk}=18.711$ mV and $\phi=-174.897^\circ$. This predicts 37.421 mV peak-to-peak. A same-circuit transient result is still needed to verify this prediction.

The constants A are fixed by the initial capacitor voltages. They are not arbitrary adjustments to fit a plot. For the specified cosine starting at +2 mV and the initial state used in the code, take the input change from its initial DC value:

$$U(s)=V_m\left[\frac{s}{s^2+\omega^2}-\frac1s\right]
=\frac{-V_m\omega^2}{s(s^2+\omega^2)}.$$

For each simple pole $p_k$,

$$A_k=\lim_{s\to p_k}(s-p_k)H(s)U(s).$$

Using $K=-9.389$ and $z=-207.56$, this is

$$A_k=\frac{Kp_k^2(p_k-z)}{\prod_{j\ne k}(p_k-p_j)}
\frac{-V_m\omega^2}{p_k(p_k^2+\omega^2)}.$$

The [code](scripts/analyze.py) gives these hand-model terms:

| Pole, per second | Time constant, −1/p | A |
|---:|---:|---:|
| −554.805 | 1.802 ms | +17.925 mV |
| −125.972 | 7.938 ms | +11.789 mV |
| −87.807 | 11.389 ms | −11.077 mV |

At $t=0$, the sine-wave part and these terms sum to zero within rounding, as required by the chosen initial state. If LTspice uses a different initial state, recalculate A.

For one term, $e^{-5}=0.00674$. After five time constants, 0.674% of that term remains. Five time constants do not mean exactly zero error. Here the slowest time constant gives about 57 ms. Because several terms can add or cancel, check the sum of the remaining terms against the allowed error. Do not use a 5 ms cursor as proof that this whole circuit has settled.

## 10. What agrees, and what still needs checking

The hand method explains the inverting gain, DC bias, low-frequency loss and startup. The selected simulation supports a gain near 20 dB and power below 1 mW. The hand-model DC current differs from the screenshot, and the independently calculated lower cutoff differs from the author's reported 102 Hz result. These differences remain visible so the report can be checked.

Next, add the original selected ASC/netlist, the original model card, the complete 102 Hz hand substitution, the MOS small-signal data, a sweep reaching the upper −3 dB crossing, and a 100 ms transient of this same circuit. Do not combine results from another capacitor set.

For background on transistor current gain and frequency response, see [Boris Murmann's open circuit notes](https://bmurmann.github.io/COCOA/contents/partI/partI.3.html). The equations above state their own simplifications; they do not replace the missing model data.
