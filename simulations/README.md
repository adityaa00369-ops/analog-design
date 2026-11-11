# Simulation files: two capacitor versions

| Version | Portable schematic | Original file |
|---|---|---|
| 1: CG 24.7 nF, CD 140.1 nF | [Draft14](draft14-historical.asc) | [Original ASC](historical-originals/Draft14.asc), [original log](historical-originals/Draft14.log) |
| 2: CG 123 nF, CD 1 µF | [Draft6](draft6-historical.asc) | [Original ASC](historical-originals/Draft6.asc) |

Both use a 1.8 V supply and CS = 22.10 µF. The portable copies use a local `tsmc081.lib` include path. Draft6's portable copy also writes micro as `u`; this does not change the values. The original files are preserved as supplied.

The user has supplied the model card text in the discussion. Save that exact text as `tsmc081.lib` beside the portable schematics to run them. The model text includes a note that flicker-noise parameters came from another process; noise has not been validated here.

## Check the bulk before the final comparison

The supplied Draft6 uses `nmos4` at (112,96). The bulk pin is at (160,144). Its wire ends at (160,176), while the source pin is at (160,192). There is no connecting wire across that gap. The earlier Draft14 log also reports a floating node.

These files preserve the historical circuits. They have not been silently corrected. For final reruns, save separate copies and connect the bulk to ground in both. Keep every other value unchanged. This is a wiring correction, separate from the capacitor change.

## Run and compare

1. Run `.op`. Record current and node voltages. Both capacitor versions should give the same DC result when all other values and settings match.
2. Run AC from below the lower edge to beyond the upper edge as supported by the model. Use output/input voltage gain. Measure midband and both half-power crossings in each run.
3. Run a 2 mV peak, 1 kHz input for 100 ms, with a maximum step near 2 µs. Compare early cycles and late cycles separately.
4. Extract gm, gds, gmb and capacitance data. Use these for a matrix calculation without Miller.
5. Record temperature, bulk connection, source/load parasitics and initial-condition settings with the results.

The original Draft6 file enables transient analysis and comments out AC and operating-point analysis. Enable the analysis you need. Renaming a file or changing the bulk connection does not automatically rerun it.
