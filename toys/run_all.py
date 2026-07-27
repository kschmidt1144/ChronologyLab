"""Mini-toys TM1-TM6 for the Chronology Lab report.

Emits each figure as light+dark SVG pairs (transparent background; the report
supplies the chart surface) plus results.json with the quoted numbers.
Palette: dataviz reference palette, categorical slots 1-3 (validated both modes).
"""
import json
from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

MODES = {
    "light": dict(primary="#0b0b0b", secondary="#52514e", muted="#898781",
                  grid="#e1e0d9", baseline="#c3c2b7",
                  series=["#2a78d6", "#eb6834", "#1baf7a"]),
    "dark": dict(primary="#ffffff", secondary="#c3c2b7", muted="#898781",
                 grid="#2c2c2a", baseline="#383835",
                 series=["#3987e5", "#d95926", "#199e70"]),
}
results: dict = {}


def apply_style(m: dict) -> None:
    mpl.rcParams.update({
        "svg.fonttype": "none",
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size": 11,
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.transparent": True,
        "axes.edgecolor": m["baseline"],
        "axes.labelcolor": m["secondary"],
        "axes.titlecolor": m["secondary"],
        "xtick.color": m["muted"],
        "ytick.color": m["muted"],
        "axes.grid": True,
        "grid.color": m["grid"],
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 1.0,
        "legend.frameon": False,
        "lines.linewidth": 2.0,
    })


def save(fig, name: str, mode: str) -> None:
    fig.savefig(OUT / f"{name}_{mode}.svg", bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- TM1
def tm1(m, mode):
    n = np.arange(0, 26)
    dev0 = 0.5
    cases = [(0.7, "contracting |Λ|=0.7 → consistency is an attractor"),
             (1.3, "expanding |Λ|=1.3 → mismatch blows up"),
             (1.0, "marginal |Λ|=1 → mismatch persists")]
    fig, ax = plt.subplots(figsize=(8.4, 3.5))
    for (lam, label), c in zip(cases, m["series"]):
        dev = dev0 * lam ** n
        ax.semilogy(n, dev, color=c, label=label)
        ax.annotate(f"|Λ|={lam}", xy=(n[-1], dev[-1]), xytext=(4, 0),
                    textcoords="offset points", color=c, fontsize=10, va="center")
    ax.set_xlabel("loop iterations n (meta-time / solver steps)")
    ax.set_ylabel("mismatch |xₙ − x*|")
    ax.set_xlim(0, 31)
    ax.legend(loc="upper left", fontsize=9)
    save(fig, "tm1_loopmap", mode)
    if mode == "light":
        results["tm1"] = {
            "deviation_after_25_iter": {"0.7": dev0 * 0.7 ** 25, "1.3": dev0 * 1.3 ** 25, "1.0": dev0},
            "finding": "contraction => unique stable consistent history (Banach); "
                       "expansion => blow-up; dichotomy incomplete as impossibility argument",
        }


# ---------------------------------------------------------------- TM2
def tm2(m, mode):
    u, wc, sig = 1.0, 0.4, 0.15

    def f(w, k):
        return u - k * np.exp(-((w - wc) ** 2) / (2 * sig ** 2))

    w = np.linspace(-0.4, 1.8, 4001)
    kappas = [0.15, 0.55, 1.0]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.5))
    ax1.plot(w, w, color=m["muted"], linewidth=1.2, linestyle="--")
    ax1.annotate("w = f(w) line", xy=(1.55, 1.55), color=m["muted"], fontsize=9,
                 ha="right", va="bottom")
    for k, c in zip(kappas, m["series"]):
        ax1.plot(w, f(w, k), color=c, label=f"coupling κ={k}")
    ax1.set_xlabel("assumed emerging velocity w")
    ax1.set_ylabel("produced velocity f(w)")
    ax1.legend(fontsize=9, loc="lower right")

    ks = np.linspace(0, 1.2, 481)
    counts = []
    for k in ks:
        h = w - f(w, k)
        counts.append(int(np.sum(np.diff(np.signbit(h)) != 0)))
    ax2.step(ks, counts, color=m["series"][0], where="mid")
    ax2.set_xlabel("coupling strength κ")
    ax2.set_ylabel("number of consistent solutions")
    ax2.set_yticks([1, 2, 3])
    ax2.set_ylim(0.5, 3.6)
    save(fig, "tm2_roots", mode)
    if mode == "light":
        counts_arr = np.array(counts)
        k_multi = ks[counts_arr > 1]
        results["tm2"] = {
            "min_solutions_over_scan": int(counts_arr.min()),
            "max_solutions_over_scan": int(counts_arr.max()),
            "multiplicity_onset_kappa": float(k_multi[0]) if len(k_multi) else None,
            "finding": "existence never fails (min 1 root across full scan; bounded continuous "
                       "self-map => fixed point); uniqueness fails above a coupling threshold",
        }


# ---------------------------------------------------------------- TM3
def tm3(m, mode):
    eps = 0.15  # depolarizing strength
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    rng = np.random.default_rng(7)

    def rand_rho():
        v = rng.normal(size=3)
        v = 0.98 * v / np.linalg.norm(v)
        sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
        return 0.5 * (I2 + v[0] * sx + v[1] * sy + v[2] * sz)

    def step(r):
        return (1 - eps) * (X @ r @ X.conj().T) + eps * I2 / 2

    def tdist(a, b):
        ev = np.linalg.eigvalsh(a - b)
        return 0.5 * np.sum(np.abs(ev))

    iters = np.arange(0, 31)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.5))
    for idx, c in enumerate(m["series"]):
        r = rand_rho()
        ds = []
        for _ in iters:
            ds.append(tdist(r, I2 / 2))
            r = step(r)
        ax1.semilogy(iters, np.maximum(ds, 1e-16), color=c,
                     label=f"random initial state {idx + 1}")
    ax1.set_xlabel("loop iterations")
    ax1.set_ylabel("trace distance to fixed point I/2")
    ax1.legend(fontsize=9, loc="upper right")

    theta = np.linspace(0, np.pi, 400)
    p = np.cos(theta / 2) ** 2
    ax2.plot(theta, p, color=m["series"][0])
    ax2.scatter([np.pi], [0.0], s=42, color=m["series"][1], zorder=5)
    ax2.annotate("perfect grandfather:\namplitude sums to 0",
                 xy=(np.pi, 0.0), xytext=(-118, 26), textcoords="offset points",
                 color=m["secondary"], fontsize=9,
                 arrowprops=dict(arrowstyle="->", color=m["muted"], lw=1))
    ax2.set_xlabel("paradox strength θ  (π = full flip)")
    ax2.set_ylabel("P-CTC postselection weight")
    ax2.set_xticks([0, np.pi / 2, np.pi], ["0", "π/2", "π"])
    save(fig, "tm3_qubit", mode)
    if mode == "light":
        results["tm3"] = {
            "deutsch_fixed_point": "I/2 (maximally mixed), unique attractor once eps>0 decoherence added",
            "contraction_factor_per_iter": 1 - eps,
            "pctc_weight_at_full_paradox": 0.0,
            "pctc_weight_formula": "cos^2(theta/2) = |Tr U|^2 / 4 for U = Rx(theta)",
            "finding": "Deutsch consistency always solvable (grandfather -> mixed state); "
                       "P-CTC literally cancels the paradoxical branch (weight exactly 0)",
        }


# ---------------------------------------------------------------- TM4
def tm4(m, mode):
    N = np.arange(0, 41)
    fig, ax = plt.subplots(figsize=(8.4, 3.5))
    labels = ["g=0.8 defocusing wins → pile-up bounded",
              "g=1.0 marginal → linear growth",
              "g=1.2 blueshift wins → geometric divergence"]
    for g, c, lab in zip([0.8, 1.0, 1.2], m["series"], labels):
        E = np.array([np.sum(g ** np.arange(0, n + 1)) for n in N])
        ax.semilogy(N, E, color=c, label=lab)
    ax.set_xlabel("circuits N through the about-to-form time machine")
    ax.set_ylabel("accumulated energy density (arb.)")
    ax.legend(fontsize=9, loc="upper left")
    save(fig, "tm4_horizon", mode)
    if mode == "light":
        results["tm4"] = {
            "sum_at_N40": {"0.8": float(np.sum(0.8 ** np.arange(41))),
                           "1.0": 41.0,
                           "1.2": float(np.sum(1.2 ** np.arange(41)))},
            "finding": "whether the machine self-destroys is exactly the question g >= 1 or < 1 "
                       "per circuit — the Kim-Thorne vs Hawking dispute in one dial",
        }


# ---------------------------------------------------------------- TM5 (numbers only; report renders a stat tile)
def tm5():
    n_atoms_per_gram_carbon = 6.02214076e23 / 12.011
    dS_over_k = n_atoms_per_gram_carbon * 1.0  # O(1) k_B per particle, conservative
    log10_P = -dS_over_k / np.log(10)
    results["tm5"] = {
        "atoms_per_gram_carbon": n_atoms_per_gram_carbon,
        "dS_over_kB_per_gram": dS_over_k,
        "log10_suppression_per_gram_per_pass": log10_P,
        "planck_times_age_of_universe_log10": 61,
        "finding": "a 1 k_B-per-atom conspiratorial arrangement of ONE GRAM costs "
                   "P ~ 10^(-2.2e22): 'almost all' in the fluctuation measure, but never exactly 0",
    }


# ---------------------------------------------------------------- TM6
def tm6(m, mode):
    phi = np.linspace(-np.pi, np.pi, 4001)
    fig, ax = plt.subplots(figsize=(8.4, 3.5))
    fwhm = {}
    for Mw, c in zip([5, 20, 100], m["series"]):
        num = np.sin((Mw + 1) * phi / 2)
        den = np.sin(phi / 2)
        A = np.where(np.abs(den) < 1e-12, Mw + 1.0, num / np.where(np.abs(den) < 1e-12, 1, den))
        Anorm = np.abs(A) / (Mw + 1)
        ax.plot(phi, Anorm, color=c, label=f"{Mw} windings")
        above = phi[Anorm >= 0.5]
        fwhm[str(Mw)] = float(above.max() - above.min())
    ax.set_xlabel("energy mismatch phase per circuit  φ = ΔE·τ/ħ")
    ax.set_ylabel("|summed amplitude| (normalized)")
    ax.set_xticks([-np.pi, 0, np.pi], ["−π", "0", "π"])
    ax.legend(fontsize=9, loc="upper right")
    ax.annotate("only ΔE = 0 survives\nas windings → ∞", xy=(0, 1.0),
                xytext=(28, -18), textcoords="offset points",
                color=m["secondary"], fontsize=9,
                arrowprops=dict(arrowstyle="->", color=m["muted"], lw=1))
    save(fig, "tm6_winding", mode)
    if mode == "light":
        results["tm6"] = {
            "fwhm_by_windings": fwhm,
            "finding": "summing over loop windings is a Dirichlet kernel: weight concentrates on "
                       "exact energy match as windings grow — the claim's cancellation mechanism, "
                       "realized as interference (same math as a resonant cavity)",
        }


for mode_name, mval in MODES.items():
    apply_style(mval)
    tm1(mval, mode_name)
    tm2(mval, mode_name)
    tm3(mval, mode_name)
    tm4(mval, mode_name)
    tm6(mval, mode_name)
tm5()

(OUT / "results.json").write_text(json.dumps(results, indent=2))
print("wrote", len(list(OUT.glob("*.svg"))), "SVGs +", OUT / "results.json")
