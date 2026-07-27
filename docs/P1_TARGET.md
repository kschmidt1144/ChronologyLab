# P1 pre-registration — "The thermodynamic price of a consistent time loop"

**Committed before any derivation was verified or any model run** — the git timestamp of this
file, relative to the results commit, is the proof of pre-registration. The adversarial novelty
scan (three agents; results land in `P1_NOVELTY.md`) runs in parallel; it gates the *novelty
claims* of the write-up, never the math.

## Question

Quantify thesis T3: what does Novikov-style self-consistency **cost**, thermodynamically, for a
dissipative system threading a time loop — and where exactly does the cost attach?

## Fixed setup (chosen in advance)

- **Classical:** finite irreducible continuous-time (or discrete-time) Markov chain; rates
  w(x→y) > 0 obeying local detailed balance with one bath at temperature T; Gibbs stationary
  distribution π. **Loop:** trajectory-level Novikov consistency — the loop junction is an ideal
  identity channel returning the loop variable's microstate from coordinate time τ to time 0;
  consistency event C_x = {x(0) = x = x(τ)}. Medium entropy of a path γ:
  s(γ) = k_B Σ ln[w(x_i→x_{i+1})/w(x_{i+1}→x_i)].
- **Quantum:** the Deutsch condition ρ = Φ(ρ) ("density-matrix consistency") versus
  "record consistency" (pointer-basis value returns around the loop).
- **Assumptions ledger:** A-P1-1 the junction itself adds no dissipation (ideal identity);
  A-P1-2 probabilities are statements in the ordinary path measure of the dynamics (typicality
  reading — same epistemic status as any statistical-mechanics claim about the one actual world);
  A-P1-3 undriven equilibrium bath except where stated.

## Pre-registered targets (each with its falsifier)

- **T1 — Loop-closure cost.** R_τ(x) ≡ P(x(τ)=x | x(0)=x) decays **monotonically** (for
  reversible chains) to π(x) as τ grows; macrostate version R_τ(M) → π(M) =
  exp(−(S_eq − S_M)/k_B) (Einstein weight). Physical reading: *short hops are cheap; loops longer
  than the relaxation time pay the full Boltzmann price of the loop state's persistence.*
  *Falsifier:* any detailed-balance chain with R_τ(x) < π(x) at some τ, or no convergence.
- **T2 — Conditional detailed fluctuation theorem.** Within the consistent ensemble:
  P(s | C_x) / P(−s | C_x) = e^{s/k_B}; hence ⟨e^{−s/k_B}⟩_C = 1, the tail bound
  P(s ≤ −σ | C_x) ≤ e^{−σ/k_B}, and ⟨s⟩_C ≥ 0. Reading: *consistent loops are not
  second-law-violating miracles; anti-thermodynamic loop segments are priced exactly as ordinary
  fluctuations.* *Falsifier:* exact path enumeration violating the ratio in any bin.
- **T3 — No pastward free lunch (corollary of T1).** A loop whose cargo persistently carries
  free-energy excess ΔF above the bath's equilibrium closes with probability → e^{−ΔF/k_BT}:
  a time loop can host a charged battery only at the full Boltzmann tax on its charge.
  *Falsifier:* a compliant model closing more cheaply.
- **T4 — Extensivity.** Independent loop-threading components multiply: R_N = (R_1)^N — the
  macroscopic-traveler suppression exp(−N·δs/k_B), turning Report I's TM5 scale estimate into a
  derived statement. *Falsifier:* sub-extensive scaling in the independent-component model.
- **T5 — Where the price attaches (quantum contrast, numeric).** Deutsch density-matrix
  consistency has **no** such cost (fixed point exists at every coupling tested), while
  record-level (pointer) consistency reproduces the classical exponential suppression. Reading:
  *the thermodynamic price attaches to records/memory, not to time travel as such* — the
  quantitative form of Report I's "you cannot remember completing a closed loop."
  *Falsifier:* a tested coupling with no Deutsch fixed point, or record-closure without decay.

## Planned models

E1 two-state chain (analytic + plot) → T1. E2 exact path enumeration, 3-state detailed-balance
chain, all periodic paths → T2 (exact, bin-by-bin). E3 N independent units → T4.
E4 CTC qubit + thermal environment, partial-swap coupling: Deutsch iteration vs dephased
record-closure → T5. (T3 read off T1's π(x) = e^{−ΔF_x/k_BT}.)

## Success criteria

Every target demonstrated at E1 (derivation) or E2 (exact numeric check) in the stated models;
honest scope section (junction idealization; typicality; trajectory-level Novikov as the
strongest classical reading); write-up as Report II with novelty positioning per the scan.

## Known limits (stated in advance)

This prices consistency *on* a background loop — thermodynamics **of the traveler**, not dynamics
**of the spacetime** (no metric, no backreaction). It is therefore complementary to chronology
protection (C4b), not a contribution to it.
