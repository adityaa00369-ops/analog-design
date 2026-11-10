"""Analytical model of the 1.8 V common-source amplifier. All values are SI."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import eigvals
from scipy.optimize import brentq

RESULTS = Path(__file__).resolve().parents[1] / "results"
RD, RS, RL = 1400, 218, 10000
RG = 1 / (1 / 182000 + 1 / 100000)
VDD, LENGTH, WIDTH = 1.8, 0.36e-6, 93.6e-6
KP, LAMBDA = 230.5e-6, 0.05
VT = 0.3662 + 0.04  # Historical Python threshold proxy, not BSIM extraction.
CS = 22.10e-6
VG = VDD * 100 / 282
BETA = KP * WIDTH / LENGTH
ID = brentq(
    lambda i: i - BETA / 2 * (VG - RS*i - VT)**2
    * (1 + LAMBDA*(VDD - (RD+RS)*i)),
    0, (VG-VT)/RS, xtol=1e-15,
)
VOV = VG - RS*ID - VT
VDS = VDD - (RD+RS)*ID
GM = 2*ID/VOV
GDS = LAMBDA*ID/(1+LAMBDA*VDS)
C_PER_WIDTH = 2/3 * (3.9*8.8541878128e-12/4.1e-9)*LENGTH + 2*8.23e-10
OMEGA = 2*np.pi*1000
VM = 0.002
CASES = {"A1": (24.7e-9, 140.1e-9), "A2": (123e-9, 1e-6)}


def response(cg, cd):
    # Nodes [gate, drain, source, load]. The ideal source drives CG.
    conductance = np.diag([1/RG, 1/RD, 1/RS, 1/RL])
    drain_current = np.array([GM, GDS, -GM-GDS, 0])
    conductance[1] += drain_current
    conductance[2] -= drain_current
    capacitance = np.diag([cg, cd, CS, cd])
    capacitance[1, 3] = capacitance[3, 1] = -cd
    drive = np.array([cg, 0, 0, 0])

    def transfer(s):
        return np.linalg.solve(conductance+s*capacitance, s*drive)[3]

    roots = eigvals(-conductance, capacitance)
    poles = sorted(p.real for p in roots if np.isfinite(p))
    assert len(poles) == 3 and max(poles) < 0
    gain = -GM / (1/RD + 1/RL + GDS)
    zero = -1/(RS*CS)
    # V_in starts at +VM in the DC solution. Perturbation is VM*(cos(wt)-1).
    # At each pole p, multiply V_o(s) by s-p and evaluate at p.
    amplitudes = [
        gain*p*p*(p-zero)/np.prod([p-q for q in poles if q != p])
        * (-VM*OMEGA**2/(p*(p*p+OMEGA**2)))
        for p in poles
    ]
    edge = brentq(lambda f: abs(transfer(2j*np.pi*f))-abs(gain)/np.sqrt(2), 1, 1e4)
    return transfer, poles, amplitudes, gain, edge


def main():
    RESULTS.mkdir(exist_ok=True)
    print(f"ID={ID*1e6:.3f} uA; VG={VG:.6f} V; VS={RS*ID:.6f} V; "
          f"VD={VDD-RD*ID:.6f} V; VDS={VDS:.6f} V; VOV={VOV:.6f} V")
    print(f"gm={GM*1e3:.4f} mS; gds={GDS*1e6:.4f} uS; "
          f"gm/ID={GM/ID:.4f} /V; power={VDD*(ID+VDD/282000)*1e3:.4f} mW")
    fig, (ax, time_ax) = plt.subplots(2, 1, figsize=(9, 7), layout="constrained")
    frequency = np.geomspace(1, 1e5, 700)
    time = np.linspace(0, 0.06, 4500)
    for name, (cg, cd) in CASES.items():
        transfer, poles, amps, gain, edge = response(cg, cd)
        steady = VM*transfer(1j*OMEGA)
        assert abs(steady.real+sum(amps)) < 1e-9
        print(f"{name}: gain={20*np.log10(abs(gain)):.4f} dB; fL={edge:.3f} Hz; "
              f"1 kHz={2*abs(steady)*1e3:.3f} mVpp, phase={np.angle(steady, deg=True):.3f} deg; "
              f"100 Hz={20*np.log10(abs(transfer(200j*np.pi))):.3f} dB")
        print("  poles (1/s), startup terms (mV):", list(zip(poles, np.array(amps)*1e3)))
        wave = np.real(steady*np.exp(1j*OMEGA*time))
        wave += sum(a*np.exp(p*time) for p, a in zip(poles, amps))
        ax.semilogx(frequency, [20*np.log10(abs(transfer(2j*np.pi*f))) for f in frequency], label=name)
        ax.scatter(edge, 20*np.log10(abs(gain)/np.sqrt(2)))
        time_ax.plot(time*1e3, wave*1e3, label=name)
    ax.set(title="Hand-model frequency response", xlabel="Frequency (Hz)", ylabel="Gain (dB)")
    time_ax.set(title="Hand-model startup at 1 kHz", xlabel="Time (ms)", ylabel="Load voltage (mV)", xlim=(0, 16))
    for panel in (ax, time_ax):
        panel.grid(alpha=.25)
        panel.legend()
    fig.savefig(RESULTS/"analytical-response.png", dpi=180)

    # Restrict this analytical plot to square-law sensitivity around the design.
    # A continuous weak-to-strong BSIM characterization requires a separate device sweep.
    ratios = np.linspace(5, 15, 301)
    density = KP/2*(2/ratios)**2
    ft = ratios*density/(2*np.pi*LENGTH*C_PER_WIDTH)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4), layout="constrained")
    left.plot(ratios, density*1e6)
    right.plot(ratios, ft/1e9)
    for panel, y, label in ((left, density*1e6, "ID/(W/L) (µA)"), (right, ft/1e9, "Estimated fT (GHz)")):
        panel.scatter(15, y[-1], color="tab:orange", label="Selected bias")
        panel.set(xlabel="gm/ID (1/V)", ylabel=label)
        panel.grid(alpha=.25)
        panel.legend()
    fig.suptitle("Square-law sizing sensitivity with 180 nm model-card inputs")
    fig.savefig(RESULTS/"gmid-ft-corrected.png", dpi=180)
    print(f"Historical sizing estimate with consistent Cgg: fT={ft[-1]/1e9:.4f} GHz")


if __name__ == "__main__":
    main()
