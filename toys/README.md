# Toys — miniature computational models (Stage 2, mini versions)

These are **deliberately small** versions of TM1–TM6 from `../docs/CLAIMS.md §6`, built to settle
the *structural* questions of specific leaves at evidence level E2 (explicit computation). Full
versions remain available as follow-ups if any verdict needs more force.

Run: `uv run --with numpy --with matplotlib python toys/run_all.py`
Outputs: `toys/out/*.svg` (each figure in light + dark variants) + `toys/out/results.json`
(the numbers quoted in the report).

## Pre-registered can/cannot preambles (written before first run)

- **TM1 (loop-map stability).** CAN: exhibit an explicit contracting loop map whose consistent
  history is a stable attractor — a counterexample to the universal claim "any mismatch drives the
  history to ∞ or extinction" (C4c); map the expanding and marginal regimes (C4d). CANNOT: say
  which regime real spacetime loops occupy.
- **TM2 (consistency-equation root counting).** CAN: show in a bounded-deflection self-interaction
  model that a consistent solution *always* exists (continuity + boundedness ⇒ fixed point) while
  uniqueness fails beyond a coupling threshold (C3b, C3c, C5b — structure only). CANNOT: stand in
  for real billiard dynamics (it is a schematic consistency equation, not mechanics).
- **TM3 (qubit CTC).** CAN: verify Deutsch's grandfather resolution end-to-end (fixed point exists;
  with a little decoherence the maximally mixed state is the unique attractor) and the P-CTC
  cancellation (postselection probability cos²(θ/2) → exactly 0 at the perfect paradox) (C2b, C3b,
  C6a). CANNOT: decide whether nature implements D-CTCs, P-CTCs, or neither.
- **TM4 (chronology-horizon cartoon).** CAN: make the per-circuit-gain structure of the
  Kim–Thorne/Hawking dispute vivid (g<1 bounded, g=1 linear, g>1 geometric divergence) (C4a, C4b).
  CANNOT: resolve the dispute (that is a quantum-gravity question).
- **TM5 (suppression scale).** CAN: put an order-of-magnitude number on the fluctuation cost of a
  conspiratorial macroscopic arrangement (C2a, C5c). CANNOT: price a real trip; the number is a
  scale demonstration, not a bound derived from a specific spacetime.
- **TM6 (winding-number interference).** CAN: demonstrate the C6b mechanism exactly — summing
  amplitudes over loop windings, e^{i·N·ΔE·τ/ħ}, produces a Dirichlet kernel that concentrates all
  weight on ΔE = 0 as windings grow: "paths with unequal energy cancel out," made literal.
  CANNOT: show that real time loops sum this way (same mathematics as a resonant cavity — which is
  precisely the point and precisely the limitation).
