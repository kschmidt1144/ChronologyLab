"""P1 computational checks E1-E4 (targets pre-registered in docs/P1_TARGET.md).

Style/palette mirrors toys/run_all.py (dataviz reference palette, slots 1-3,
validated both modes). Units: k_B = 1, T = 1 (energies in units of k_B*T).
"""
import itertools
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


def apply_style(m):
    mpl.rcParams.update({
        "svg.fonttype": "none", "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size": 11, "figure.facecolor": "none", "axes.facecolor": "none",
        "savefig.transparent": True, "axes.edgecolor": m["baseline"],
        "axes.labelcolor": m["secondary"], "xtick.color": m["muted"],
        "ytick.color": m["muted"], "axes.grid": True, "grid.color": m["grid"],
        "grid.linewidth": 0.8, "axes.spines.top": False,
        "axes.spines.right": False, "axes.linewidth": 1.0,
        "legend.frameon": False, "lines.linewidth": 2.0,
    })


def save(fig, name, mode):
    fig.savefig(OUT / f"{name}_{mode}.svg", bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- E1 (T1)
def e1(m, mode):
    dEs = [1.0, 3.0, 6.0]
    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    mono_ok = True
    for dE, c in zip(dEs, m["series"]):
        up, down = np.exp(-dE), 1.0
        lam = up + down
        pi1 = up / lam
        t = np.linspace(0, 8, 600) / lam          # in absolute time
        R = pi1 + (1 - pi1) * np.exp(-lam * t)
        mono_ok &= bool(np.all(np.diff(R) <= 1e-15))
        ax.semilogy(t * lam, R, color=c, label=f"ΔS = {dE} k_B  (loop state's entropy deficit)")
        ax.axhline(pi1, color=m["muted"], linewidth=1.0, linestyle="--")
        ax.annotate(f"Boltzmann floor e^−{dE:g} ≈ {pi1:.4f}", xy=(8, pi1),
                    xytext=(-4, 4), textcoords="offset points", ha="right",
                    color=m["muted"], fontsize=8.5)
    ax.set_xlabel("loop duration τ  (units of relaxation time)")
    ax.set_ylabel("closure probability R_τ")
    ax.legend(fontsize=9, loc="upper right")
    save(fig, "p1_e1_closure", mode)
    if mode == "light":
        results["E1"] = {
            "monotone_decay_verified": mono_ok,
            "floors": {str(d): 1 / (1 + np.exp(d)) for d in dEs},
            "finding": "closure probability decays monotonically to the Boltzmann weight of the "
                       "loop state; short hops cheap, loops beyond t_relax pay exp(-dS/kB) (T1)",
        }


# ---------------------------------------------------------------- E2 (T2a + T2b)
def enumerate_periodic(P, x_star, T):
    """All length-T periodic paths: closure prob + entropy-production distribution."""
    n = P.shape[0]
    probs: dict[float, float] = {}
    PC = 0.0
    for interior in itertools.product(range(n), repeat=T - 1):
        path = (x_star, *interior, x_star)
        p, s = 1.0, 0.0
        for a, b in zip(path[:-1], path[1:]):
            p *= P[a, b]
            if p == 0.0:
                break
            if a != b:
                s += np.log(P[a, b] / P[b, a])
        if p == 0.0:
            continue
        PC += p
        key = round(s, 9)
        probs[key] = probs.get(key, 0.0) + p
    return PC, probs


def e2(m, mode):
    # --- T2a: undriven (single bath, detailed balance) => s = 0 on EVERY loop
    E = np.array([0.0, 1.0, 2.0])
    n = 3
    P_eq = np.zeros((n, n))
    for x in range(n):
        for y in range(n):
            if x != y:
                P_eq[x, y] = 0.5 * min(1.0, np.exp(-(E[y] - E[x])))
        P_eq[x, x] = 1.0 - P_eq[x].sum()
    PC_eq, probs_eq = enumerate_periodic(P_eq, x_star=2, T=8)
    max_abs_s_eq = max(abs(s) for s in probs_eq)

    # --- T2b: driven 3-ring (affinity f per hop) => contentful conditional DFT
    f = 1.5
    a_fwd, a_bwd = 0.40, 0.40 * np.exp(-f)
    P_dr = np.zeros((3, 3))
    for x in range(3):
        P_dr[x, (x + 1) % 3] = a_fwd
        P_dr[x, (x - 1) % 3] = a_bwd
        P_dr[x, x] = 1.0 - a_fwd - a_bwd
    PC_dr, probs_dr = enumerate_periodic(P_dr, x_star=0, T=9)
    pts, dev = [], 0.0
    for s in sorted(probs_dr):
        if s > 1e-12 and -s in probs_dr:
            lhs = np.log(probs_dr[s] / probs_dr[-s])
            dev = max(dev, abs(lhs - s))
            pts.append((s, lhs))
    ift = sum(p * np.exp(-s) for s, p in probs_dr.items()) / PC_dr
    mean_s = sum(p * s for s, p in probs_dr.items()) / PC_dr

    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    ss = np.array([q[0] for q in pts]); ll = np.array([q[1] for q in pts])
    lim = ss.max() * 1.15
    ax.plot([0, lim], [0, lim], color=m["muted"], linestyle="--", linewidth=1.2)
    ax.annotate("slope 1 (theorem)", xy=(lim * 0.70, lim * 0.70), xytext=(6, -16),
                textcoords="offset points", color=m["muted"], fontsize=9)
    ax.scatter(ss, ll, s=52, color=m["series"][0], zorder=5,
               label=f"driven ring: every entropy bin, all {3 ** 8:,} periodic paths")
    ax.annotate("undriven chain (2,187 loops):\nevery single loop has s = 0 exactly\n"
                "— C2a's reversibility, now a theorem here",
                xy=(0, 0), xytext=(14, 40), textcoords="offset points",
                color=m["secondary"], fontsize=9,
                arrowprops=dict(arrowstyle="->", color=m["muted"], lw=1))
    ax.set_xlabel("entropy produced around the loop  s / k_B")
    ax.set_ylabel("ln [ P(s | loop) / P(−s | loop) ]")
    ax.legend(fontsize=9, loc="lower right")
    save(fig, "p1_e2_dft", mode)
    if mode == "light":
        results["E2"] = {
            "T2a_undriven": {"loops": 2187, "P_closure": PC_eq,
                             "max_abs_entropy_production": max_abs_s_eq},
            "T2b_driven": {"loops": int(3 ** 8), "P_closure": PC_dr,
                           "max_DFT_deviation": dev, "integral_FT_value": ift,
                           "mean_s_given_closure": mean_s},
            "finding": "T2a sharpening: undriven consistent loops have s = 0 EXACTLY "
                       "(telescoping) — dissipation around a closed trajectory is identically "
                       "zero, C2a as a theorem in this class; T2b: with driving, the conditional "
                       "detailed FT holds bin-by-bin, <e^-s>_C = 1, <s>_C >= 0",
        }


# ---------------------------------------------------------------- E3 (T4)
def e3(m, mode):
    dE, tau_over_trelax = 1.0, 3.0
    up, down = np.exp(-dE), 1.0
    lam = up + down
    pi1 = up / lam
    R1 = pi1 + (1 - pi1) * np.exp(-tau_over_trelax)
    delta = -np.log(R1)
    N = np.arange(1, 1001)
    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    ax.plot(N, N * delta / np.log(10), color=m["series"][0])
    ax.set_xlabel("independent components N that must all close the loop")
    ax.set_ylabel("−log₁₀ closure probability")
    ax.annotate(f"slope: {delta:.3f} k_B per component\n"
                f"N = 10³ → P ≈ 10^−{1000 * delta / np.log(10):.0f}\n"
                f"1 g of matter (5×10²² units) → P ≈ 10^−{5.01e22 * delta / np.log(10):.1e}",
                xy=(600, 600 * delta / np.log(10)), xytext=(-160, 30),
                textcoords="offset points", color=m["secondary"], fontsize=9)
    save(fig, "p1_e3_extensivity", mode)
    if mode == "light":
        results["E3"] = {
            "R1": R1, "delta_per_component_kB": delta,
            "log10_P_N1000": -1000 * delta / np.log(10),
            "log10_P_one_gram": -5.013854599950046e22 * delta / np.log(10),
            "finding": "independent components multiply: R_N = R_1^N — the macroscopic-traveler "
                       "suppression, now derived rather than assumed (T4)",
        }


# ---------------------------------------------------------------- E4 (T5)
def e4(m, mode):
    SWAP = np.zeros((4, 4)); SWAP[0, 0] = SWAP[3, 3] = 1; SWAP[1, 2] = SWAP[2, 1] = 1
    I4 = np.eye(4)

    def tdist(a, b):
        return 0.5 * np.abs(np.linalg.eigvalsh(a - b)).sum()

    def phi(rho, lam, dE):
        pe = 1 / (1 + np.exp(dE))
        env = np.diag([1 - pe, pe])
        U = np.cos(lam) * I4 + 1j * np.sin(lam) * SWAP
        big = U @ np.kron(env, rho) @ U.conj().T
        return big.reshape(2, 2, 2, 2).trace(axis1=0, axis2=2)

    rng = np.random.default_rng(11)

    def rand_rho():
        v = rng.normal(size=3); v = 0.97 * v / np.linalg.norm(v)
        sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
        return 0.5 * (np.eye(2) + v[0] * sx + v[1] * sy + v[2] * sz)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.6))
    dE_A = 2.0
    conv = {}
    for lam, c in zip([0.3, 0.8, 1.5], m["series"]):
        r = rand_rho()
        ds = []
        for _ in range(300):
            r2 = phi(r, lam, dE_A)
            ds.append(tdist(r2, r))
            r = r2
        conv[str(lam)] = ds[-1]
        ax1.semilogy(np.maximum(ds, 1e-17), color=c, label=f"coupling λ = {lam}")
    ax1.set_xlabel("Deutsch iteration")
    ax1.set_ylabel("successive-iterate trace distance")
    ax1.legend(fontsize=9, loc="upper right")

    lam_B = 0.6
    floors = {}
    for dE, c in zip([1.0, 3.0, 6.0], m["series"]):
        pe = 1 / (1 + np.exp(dE))
        rho = np.diag([0.0, 1.0])       # record: excited pointer state
        Rn = []
        for _ in range(41):
            Rn.append(rho[1, 1].real)
            rho = np.diag(np.diag(phi(rho, lam_B, dE)))   # dephase = keep the record classical
        floors[str(dE)] = pe
        ax2.semilogy(Rn, color=c, label=f"ΔS = {dE} k_B")
        ax2.axhline(pe, color=m["muted"], linewidth=1.0, linestyle="--")
    ax2.set_xlabel("loop dwell (junction passes)")
    ax2.set_ylabel("record-closure probability")
    ax2.legend(fontsize=9, loc="upper right")
    save(fig, "p1_e4_quantum", mode)
    if mode == "light":
        results["E4"] = {
            "deutsch_final_successive_distance": conv,
            "record_floors_boltzmann": floors,
            "finding": "Deutsch (density-matrix) consistency converges at every coupling — no "
                       "thermodynamic gate; record-level closure decays to the Boltzmann floor: "
                       "the price attaches to records, not to the loop (T5)",
        }


for mode_name, mval in MODES.items():
    apply_style(mval)
    e1(mval, mode_name)
    e2(mval, mode_name)
    e3(mval, mode_name)
    e4(mval, mode_name)

(OUT / "results.json").write_text(json.dumps(results, indent=2))
print("wrote", len(list(OUT.glob("*.svg"))), "SVGs +", OUT / "results.json")
