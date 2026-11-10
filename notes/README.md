# Original handwritten amplifier notes

Start with the [typed worked notes](../design-calculations.md). Use the table below to find the matching notebook pages by topic. Page numbers identify photos and follow the appendix grouping. The typed notes set the reading sequence.

| If you are reading about… | Open these handwritten pages |
|---|---|
| Specifications and transistor sizing | [10–15](#design-targets-and-transistor-sizing) |
| Circuit intuition and small-signal fundamentals | [01–09](#circuit-and-small-signal-foundations) |
| Resistor values and DC operating point | [16–18](#resistor-selection-and-dc-operating-point) |
| Capacitor values and frequency response | [19–22](#capacitor-sizing-and-frequency-response) |
| Startup and the waveforms at each node | [23–38](#startup-and-signal-flow-from-input-to-load) |

These photos show the original notes, including crossed-out work and early values. Read the typed notes for corrections. The table lists the original filenames.

## Circuit and small-signal foundations

| Page | What to follow | Original upload |
|---|---|---|
| [01](original-pages/01-154625.jpg) | Early circuit notes | `IMG20260402154625(1).jpg` |
| [02](original-pages/02-154709.jpg) | MOSFET relationships and bias notes | `IMG20260402154709(1).jpg` |
| [03](original-pages/03-154824.jpg) | Circuit sketches and DC analysis | `IMG20260402154824(1).jpg` |
| [04](original-pages/04-154834.jpg) | Small-signal model and midband gain | `IMG20260402154834(1).jpg` |
| [05](original-pages/05-154843.jpg) | Input and output coupling networks | `IMG20260402154843(1).jpg` |
| [06](original-pages/06-154855.jpg) | Source-side small-signal equivalent | `IMG20260402154855(1).jpg` |
| [07](original-pages/07-154903.jpg) | Continuation of the source-side calculation | `IMG20260402154903(1).jpg` |
| [08](original-pages/08-154945.jpg) | Small-signal gain and transistor capacitances | `IMG20260402154945(1).jpg` |
| [09](original-pages/09-154952.jpg) | Continuation of the capacitance calculation | `IMG20260402154952(1).jpg` |

## Design targets and transistor sizing

| Page | What to follow | Original upload |
|---|---|---|
| [10](original-pages/10-155036.jpg) | Supply, power, gain, bandwidth, and load targets | `IMG20260402155036.jpg` |
| [11](original-pages/11-155043.jpg) | Design calculations continued | `IMG20260402155043(1).jpg` |
| [12](original-pages/12-155108.jpg) | Bias circuit and device calculations | `IMG20260402155108(1).jpg` |
| [13](original-pages/13-155118.jpg) | Transconductance and sizing calculations | `IMG20260402155118(1).jpg` |
| [14](original-pages/14-155146.jpg) | Hand sizing page from the notebook sequence | `IMG20260402155146(1).jpg` |
| [15](original-pages/15-width.jpg) | Detailed width derivation for the 93.6 µm device | `2da4d863-e860-4148-b8f5-5ab06b29483a.jpg` |

## Resistor selection and DC operating point

| Page | What to follow | Original upload |
|---|---|---|
| [16](original-pages/16-155125.jpg) | Effective drain load and drain resistor | `IMG20260402155125.jpg` |
| [17](original-pages/17-155134.jpg) | DC loop and source resistor | `IMG20260402155134.jpg` |
| [18](original-pages/18-155140.jpg) | Source voltage and gate-divider ratio | `IMG20260402155140.jpg` |

## Capacitor sizing and frequency response

| Page | What to follow | Original upload |
|---|---|---|
| [19](original-pages/19-155150.jpg) | Input coupling capacitor and MOS capacitances | `IMG20260402155150.jpg` |
| [20](original-pages/20-155201.jpg) | Source bypass calculation | `IMG20260402155201(1).jpg` |
| [21](original-pages/21-155208.jpg) | Output coupling calculation and first simulation comparison | `IMG20260402155208.jpg` |
| [22](original-pages/22-155217.jpg) | Combined low-frequency response and revised transconductance notes | `IMG20260402155217.jpg` |

## Startup and signal flow from input to load

| Page | What to follow | Original upload |
|---|---|---|
| [23](original-pages/23-175808.jpg) | Input RC network and amplifier schematic | `IMG20260414175808.jpg` |
| [24](original-pages/24-175818.jpg) | Input network amplitude and phase | `IMG20260414175818.jpg` |
| [25](original-pages/25-175830.jpg) | Initial condition and natural response coefficient | `IMG20260414175830.jpg` |
| [26](original-pages/26-175846.jpg) | Capacitor current and the distinction between DC and AC | `IMG20260414175846.jpg` |
| [27](original-pages/27-175851.jpg) | Capacitor impedance and current phase | `IMG20260414175851.jpg` |
| [28](original-pages/28-175911.jpg) | Frequency response of the input network | `IMG20260414175911.jpg` |
| [29](original-pages/29-175944.jpg) | RC time constant and startup decay | `IMG20260414175944.jpg` |
| [30](original-pages/30-175950.jpg) | Capacitance and settling trade-off | `IMG20260414175950.jpg` |
| [31](original-pages/31-180438.jpg) | Source-side small-signal sketch | `IMG20260414180438.jpg` |
| [32](original-pages/32-180458.jpg) | Source voltage and natural response | `IMG20260414180458.jpg` |
| [33](original-pages/33-181824.jpg) | Source bypass current calculation | `IMG20260414181824.jpg` |
| [34](original-pages/34-182243.jpg) | Drain waveform and output coupling time constant | `IMG20260414182243.jpg` |
| [35](original-pages/35-182249.jpg) | Output time constant and five-time-constant estimate | `IMG20260414182249.jpg` |
| [36](original-pages/36-195437.jpg) | Output capacitor current magnitude and phase | `IMG20260414195437.jpg` |
| [37](original-pages/37-195448.jpg) | Drain voltage and current in transient | `IMG20260414195448.jpg` |
| [38](original-pages/38-200128.jpg) | Load voltage comparison and current reference directions | `IMG20260414200128.jpg` |

## Where the calculations were corrected

- The power-budget calculation includes the gate-divider current.
- The width calculation explains why the earlier Python estimate and the width used in LTspice differ.
- The output coupling capacitor sees the sum of the resistances on its two sides in the isolated network.
- The cutoff calculation uses the combined nodal response, including the source bypass pole and zero.
- The starting capacitor voltages set the extra terms seen during startup. The current sign depends on the chosen current direction.
- The small-signal output resistance connects between drain and source. The corrected analysis states when the source is approximated as AC ground.
